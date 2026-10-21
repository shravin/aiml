import argparse
import hashlib
import math
import random
from functools import partial
from typing import Any

import torch
from torch.utils.data import DataLoader


MODEL_NAME = "/home/ravin/aidev/models/distilgpt2"
SEED = 42
LORA_RANK = 4
LORA_ALPHA = 8
MAX_LENGTH = 96
BATCH_SIZE = 1
TRAINING_STEPS = 30
LEARNING_RATE = 5e-4

TRAIN_TEXTS = [
    "Predictive maintenance uses equipment condition data to plan "
    "maintenance before a failure occurs.",
    "Preventive maintenance follows a planned schedule based on "
    "time or equipment usage.",
    "Vibration monitoring helps engineers identify changes in "
    "the condition of rotating machinery.",
    "Bearing faults can produce characteristic vibration patterns. "
    "Engineers examine frequency information and operating conditions.",
    "An increase in bearing temperature may indicate lubrication "
    "problems, increased load, or other developing issues.",
    "Root mean square vibration summarizes the magnitude of a "
    "vibration signal over a measurement interval.",
    "A condition monitoring baseline describes normal equipment "
    "behavior under known operating conditions.",
    "Sensor trends should be compared with operating speed and load "
    "because these factors can influence measurements.",
    "A single abnormal reading does not confirm a machine fault. "
    "Additional measurements help support a diagnosis.",
    "Lubrication reduces friction and wear between moving surfaces. "
    "Incorrect lubrication can contribute to bearing damage.",
    "Shaft misalignment can increase vibration and mechanical stress "
    "in rotating equipment.",
    "Maintenance decisions should combine sensor measurements, "
    "inspection findings, and equipment history.",
]

EVAL_TEXTS = [
    "Condition-based maintenance uses observations of machine health "
    "to decide when maintenance is needed.",
    "A technician investigating elevated vibration should consider "
    "changes in load, speed, alignment, and bearing condition.",
    "Rising bearing temperature is a symptom that requires further "
    "investigation rather than an immediate fault diagnosis.",
    "Comparing measurements with a normal operating baseline helps "
    "identify changes in equipment condition.",
]

TEST_PROMPTS = [
    "Predictive maintenance is",
    "When bearing temperature increases,",
    "Vibration monitoring helps engineers",
]


def initialize(device_choice: str) -> torch.device:
    if device_choice == "auto":
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    elif device_choice == "cuda":
        if not torch.cuda.is_available():
            raise RuntimeError(
                'CUDA is unavailable. Choose "--device cpu" for the '
                "conceptual exercise or use a supported GPU environment."
            )
        device = torch.device("cuda:0")
    elif device_choice == "cpu":
        device = torch.device("cpu")
    else:
        raise ValueError('Device must be "auto", "cpu", or "cuda".')

    if not TRAIN_TEXTS or not EVAL_TEXTS:
        raise ValueError("Training and evaluation texts must not be empty.")
    if not set(TRAIN_TEXTS).isdisjoint(EVAL_TEXTS):
        raise ValueError("Training and evaluation texts must not overlap.")

    random.seed(SEED)
    torch.manual_seed(SEED)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(SEED)

    print("Device:", device)
    if device.type == "cuda":
        print("GPU:", torch.cuda.get_device_name(device))
    return device


def run_quantization_demo() -> None:
    weights = torch.tensor(
        [-0.95, -0.72, -0.43, -0.18, 0.06, 0.29, 0.57, 0.91],
        dtype=torch.float32,
    )
    bits = 4
    levels = 2**bits
    minimum = weights.min()
    maximum = weights.max()
    scale = (maximum - minimum) / (levels - 1)
    codes = (
        torch.round((weights - minimum) / scale)
        .clamp(0, levels - 1)
        .to(torch.uint8)
    )
    reconstructed = codes.float() * scale + minimum

    print("\nCPU-friendly uniform quantization demo")
    print(
        f"{'Original':>12} {'Code':>8} {'Reconstructed':>16} "
        f"{'Absolute error':>16}"
    )
    for original, code, restored, error in zip(
        weights, codes, reconstructed, (weights - reconstructed).abs()
    ):
        print(
            f"{original.item():12.3f} {code.item():8d} "
            f"{restored.item():16.3f} {error.item():16.6f}"
        )
    print("Number of available levels:", levels)
    print(
        "Mean absolute reconstruction error:",
        f"{(weights - reconstructed).abs().mean().item():.6f}",
    )
    print("Demo codes use uint8; packed 4-bit storage can fit two codes per byte.")

    parameter_count = 1_000_000
    print("\nIdeal weight-only storage for 1,000,000 parameters")
    for name, bits_per_weight in (
        ("FP32", 32),
        ("FP16", 16),
        ("Packed 4-bit", 4),
    ):
        size_mib = parameter_count * bits_per_weight / 8 / 1024**2
        print(f"{name:>12}: {size_mib:.3f} MiB")
    print("Estimates exclude quantization metadata and other training memory.")


def load_model(
    model_name: str,
    device: torch.device,
) -> tuple[Any, Any]:
    try:
        import bitsandbytes as bnb
        from peft import (
            LoraConfig,
            TaskType,
            get_peft_model,
            prepare_model_for_kbit_training,
        )
        from transformers import (
            AutoModelForCausalLM,
            AutoTokenizer,
            BitsAndBytesConfig,
        )
    except ImportError as error:
        raise RuntimeError(
            "GPU QLoRA requires bitsandbytes, transformers, and peft. "
            "Install them in the active environment, or run with "
            '"--device cpu" for the quantization demonstration.'
        ) from error

    if device.type != "cuda":
        raise ValueError("The QLoRA model-loading path requires CUDA.")

    compute_dtype = (
        torch.bfloat16
        if torch.cuda.is_bf16_supported()
        else torch.float16
    )
    # quantization_config = BitsAndBytesConfig(
    #     load_in_4bit=True,
    #     bnb_4bit_quant_type="nf4",
    #     bnb_4bit_use_double_quant=True,
    #     bnb_4bit_compute_dtype=compute_dtype,
    # )

    quantization_config = BitsAndBytesConfig(load_in_8bit=True)
    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        local_files_only=True,
    )
    if tokenizer.eos_token is None:
        raise ValueError("The tokenizer must define an EOS token.")
    tokenizer.pad_token = tokenizer.eos_token

    base_model = AutoModelForCausalLM.from_pretrained(
        model_name,
        local_files_only=True,
        quantization_config=quantization_config,
        device_map={"": device.index or 0},
        torch_dtype=compute_dtype,
        attn_implementation="eager",
    )
    base_model.config.pad_token_id = tokenizer.pad_token_id
    base_model.config.use_cache = False

    quantized_layer_count = sum(
        isinstance(module, bnb.nn.Linear8bitLt)
        for module in base_model.modules()
    )
    if quantized_layer_count == 0:
        raise RuntimeError(
            "No model layers were converted to 8-bit linear layers. "
            "Check model architecture and bitsandbytes support."
        )
    print("8-bit linear layers:", quantized_layer_count)
    print("Compute dtype:", compute_dtype)
    print(
        "Loaded model footprint:",
        f"{base_model.get_memory_footprint() / 1024**2:.2f} MiB",
    )

    base_model = prepare_model_for_kbit_training(
        base_model,
        use_gradient_checkpointing=False,
    )
    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=LORA_RANK,
        lora_alpha=LORA_ALPHA,
        lora_dropout=0.0,
        target_modules=["c_attn"],
        fan_in_fan_out=False,
        bias="none",
    )
    model = get_peft_model(base_model, lora_config)
    model.print_trainable_parameters()

    trainable_names = [
        name
        for name, parameter in model.named_parameters()
        if parameter.requires_grad
    ]
    if not trainable_names or not all(
        "lora_" in name for name in trainable_names
    ):
        raise RuntimeError("Expected only LoRA parameters to be trainable.")

    print("Trainable LoRA parameters:")
    for name, parameter in model.named_parameters():
        if parameter.requires_grad:
            print(f"  {name}: {tuple(parameter.shape)} ({parameter.dtype})")
    return tokenizer, model


def collate_texts(
    texts: list[str],
    tokenizer: Any,
) -> dict[str, torch.Tensor]:
    batch = tokenizer(
        [text + tokenizer.eos_token for text in texts],
        padding=True,
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt",
    )
    labels = batch["input_ids"].clone()
    labels[batch["attention_mask"] == 0] = -100
    batch["labels"] = labels
    return batch


def create_loaders(tokenizer: Any) -> tuple[DataLoader, DataLoader]:
    collate_fn = partial(collate_texts, tokenizer=tokenizer)
    train_loader = DataLoader(
        TRAIN_TEXTS,
        batch_size=BATCH_SIZE,
        shuffle=True,
        collate_fn=collate_fn,
    )
    eval_loader = DataLoader(
        EVAL_TEXTS,
        batch_size=BATCH_SIZE,
        shuffle=False,
        collate_fn=collate_fn,
    )
    return train_loader, eval_loader


@torch.no_grad()
def evaluate_loss(
    model: Any,
    eval_loader: DataLoader,
    device: torch.device,
) -> float:
    model.eval()
    loss_sum = 0.0
    token_count = 0

    for batch in eval_loader:
        batch = {key: value.to(device) for key, value in batch.items()}
        output = model(**batch)
        valid_tokens = (batch["labels"][:, 1:] != -100).sum().item()
        loss_sum += output.loss.item() * valid_tokens
        token_count += valid_tokens

    if token_count == 0:
        raise ValueError("Evaluation data contains no tokens to score.")
    return loss_sum / token_count


@torch.no_grad()
def complete_text(
    model: Any,
    prompt: str,
    tokenizer: Any,
    device: torch.device,
) -> str:
    model.eval()
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    output_ids = model.generate(
        **inputs,
        max_new_tokens=45,
        do_sample=False,
        use_cache=True,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )
    prompt_length = inputs["input_ids"].shape[1]
    return tokenizer.decode(
        output_ids[0, prompt_length:],
        skip_special_tokens=True,
    ).strip()


def frozen_fingerprints(model: Any) -> dict[str, str]:
    return {
        name: hashlib.sha256(
            parameter.detach()
            .cpu()
            .contiguous()
            .reshape(-1)
            .view(torch.uint8)
            .numpy()
            .tobytes()
        ).hexdigest()
        for name, parameter in model.named_parameters()
        if not parameter.requires_grad
    }


def train_model(
    model: Any,
    train_loader: DataLoader,
    device: torch.device,
) -> None:
    trainable_parameters = [
        parameter for parameter in model.parameters() if parameter.requires_grad
    ]
    optimizer = torch.optim.AdamW(
        trainable_parameters,
        lr=LEARNING_RATE,
        weight_decay=0.0,
    )
    iterator = iter(train_loader)
    if device.type == "cuda":
        torch.cuda.reset_peak_memory_stats(device)
    model.train()

    for step in range(1, TRAINING_STEPS + 1):
        try:
            batch = next(iterator)
        except StopIteration:
            iterator = iter(train_loader)
            batch = next(iterator)

        batch = {key: value.to(device) for key, value in batch.items()}
        optimizer.zero_grad(set_to_none=True)
        loss = model(**batch).loss
        loss.backward()
        torch.nn.utils.clip_grad_norm_(trainable_parameters, max_norm=1.0)
        optimizer.step()

        if step == 1 or step % 5 == 0 or step == TRAINING_STEPS:
            print(f"Step {step}/{TRAINING_STEPS} | Loss: {loss.item():.4f}")

    print(
        "\nPeak allocated GPU memory during training:",
        f"{torch.cuda.max_memory_allocated(device) / 1024**2:.2f} MiB",
    )


def verify_training(
    model: Any,
    frozen_before: dict[str, str],
    lora_before: dict[str, torch.Tensor],
) -> None:
    frozen_after = frozen_fingerprints(model)
    if frozen_before != frozen_after:
        raise AssertionError("A frozen parameter unexpectedly changed.")

    changed_lora = [
        name
        for name, parameter in model.named_parameters()
        if parameter.requires_grad
        and not torch.equal(
            parameter.detach().cpu(),
            lora_before[name],
        )
    ]
    if not changed_lora:
        raise AssertionError("Training did not change any LoRA parameters.")

    print("\nChanged LoRA tensors:", len(changed_lora))
    print("Verified: frozen base parameters stayed identical.")


def run_gpu_training(model_name: str, device: torch.device) -> None:
    print("\nLoading quantized model and setting up LoRA...")
    tokenizer, model = load_model(model_name, device)
    train_loader, eval_loader = create_loaders(tokenizer)

    before_loss = evaluate_loss(model, eval_loader, device)
    before_answers = {
        prompt: complete_text(model, prompt, tokenizer, device)
        for prompt in TEST_PROMPTS
    }
    print(f"Quantized baseline loss: {before_loss:.4f}")

    frozen_before = frozen_fingerprints(model)
    lora_before = {
        name: parameter.detach().cpu().clone()
        for name, parameter in model.named_parameters()
        if parameter.requires_grad
    }
    train_model(model, train_loader, device)

    after_loss = evaluate_loss(model, eval_loader, device)
    print("\nEvaluation results:")
    print(
        f"Quantized model before training | loss={before_loss:.6f} "
        f"| perplexity={math.exp(before_loss):.2f}"
    )
    print(
        f"Quantized model with trained LoRA | loss={after_loss:.6f} "
        f"| perplexity={math.exp(after_loss):.2f}"
    )
    for prompt in TEST_PROMPTS:
        print("\nPROMPT:", prompt)
        print("\nBEFORE:", before_answers[prompt])
        print("\nAFTER:", complete_text(model, prompt, tokenizer, device))
        print("=" * 70)

    verify_training(model, frozen_before, lora_before)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Demonstrate quantization and optionally train a QLoRA model."
    )
    parser.add_argument(
        "--device",
        choices=("auto", "cpu", "cuda"),
        default="auto",
        help="Use the CPU quantization demo or CUDA QLoRA training (default: auto).",
    )
    parser.add_argument(
        "--model-name",
        default=MODEL_NAME,
        help="Local model directory used for GPU training.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    device = initialize(args.device)
    run_quantization_demo()

    if device.type == "cuda":
        run_gpu_training(args.model_name, device)
    else:
        print(
            "\nCPU conceptual exercise completed. Actual 4-bit QLoRA training "
            "requires a supported NVIDIA GPU."
        )


if __name__ == "__main__":
    main()
