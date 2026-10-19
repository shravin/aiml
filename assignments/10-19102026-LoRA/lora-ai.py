import hashlib
import math
import random
from functools import partial
from typing import Any

import torch
from peft import LoraConfig, TaskType, get_peft_model
from torch.utils.data import DataLoader
from transformers import AutoModelForCausalLM, AutoTokenizer

from train_eval_texts import eval_texts, train_texts

MODEL_NAME = "/home/ravin/aidev/models/Qwen2.5-1.5B"
DEVICE_CHOICE = "auto"  # Choose "cpu", "cuda", or "auto".
SEED = 42

# Change these values to try different LoRA configurations and run lengths.
LORA_RANK = 8
LORA_ALPHA = 16
TRAINING_STEPS = 60

LORA_DROPOUT = 0.0
MAX_LENGTH = 96
BATCH_SIZE = 1
LEARNING_RATE = 5e-4
MERGE_LORA = False

TEST_PROMPTS = [
    "Predictive maintenance is",
    "When bearing temperature increases,",
    "Vibration monitoring helps engineers",
]


def initialize() -> torch.device:
    if DEVICE_CHOICE == "auto":
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    elif DEVICE_CHOICE == "cuda":
        if not torch.cuda.is_available():
            raise RuntimeError('CUDA unavailable. Choose "cpu" or "auto".')
        device = torch.device("cuda")
    elif DEVICE_CHOICE == "cpu":
        device = torch.device("cpu")
    else:
        raise ValueError('DEVICE_CHOICE must be "cpu", "cuda", or "auto".')

    if LORA_RANK <= 0 or LORA_ALPHA <= 0:
        raise ValueError("LORA_RANK and LORA_ALPHA must be positive.")
    if TRAINING_STEPS <= 0:
        raise ValueError("TRAINING_STEPS must be positive.")
    if not train_texts or not eval_texts:
        raise ValueError("Training and evaluation text lists must not be empty.")
    if not set(train_texts).isdisjoint(eval_texts):
        raise ValueError("Training and evaluation texts must not overlap.")

    random.seed(SEED)
    torch.manual_seed(SEED)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(SEED)

    print("Device:", device)
    if device.type == "cuda":
        print("GPU:", torch.cuda.get_device_name(0))

    print("LoRA rank:", LORA_RANK)
    print("LoRA alpha:", LORA_ALPHA)
    print("Scaling factor:", LORA_ALPHA / LORA_RANK)
    print("Training examples:", len(train_texts))
    print("Evaluation examples:", len(eval_texts))
    return device


def load_model(device: torch.device) -> tuple[Any, Any]:
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        local_files_only=True,
    )
    if tokenizer.eos_token is None:
        raise ValueError("The tokenizer must define an EOS token.")
    tokenizer.pad_token = tokenizer.eos_token

    base_model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        local_files_only=True,
        attn_implementation="eager",
    ).to(device)
    base_model.config.pad_token_id = tokenizer.pad_token_id
    base_model.config.use_cache = False
    return tokenizer, base_model


def collate_texts(texts: list[str], tokenizer: Any) -> dict[str, torch.Tensor]:
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


def load_loaders(tokenizer: Any) -> tuple[DataLoader, DataLoader]:
    collate_fn = partial(collate_texts, tokenizer=tokenizer)
    train_loader = DataLoader(
        train_texts,
        batch_size=BATCH_SIZE,
        shuffle=True,
        collate_fn=collate_fn,
    )
    eval_loader = DataLoader(
        eval_texts,
        batch_size=BATCH_SIZE,
        shuffle=False,
        collate_fn=collate_fn,
    )
    return train_loader, eval_loader


def inspect_target_modules(base_model: Any) -> None:
    print("\nAttention projections selected for LoRA:")
    for name, module in base_model.named_modules():
        if name.endswith("c_attn") or name.endswith(("q_proj", "v_proj")):
            print(name, tuple(module.weight.shape))


@torch.no_grad()
def evaluate_loss(
    current_model: Any,
    eval_loader: DataLoader,
    device: torch.device,
) -> float:
    current_model.eval()
    loss_sum = 0.0
    token_count = 0

    for batch in eval_loader:
        batch = {key: value.to(device) for key, value in batch.items()}
        output = current_model(**batch)
        valid_tokens = (batch["labels"][:, 1:] != -100).sum().item()
        loss_sum += output.loss.item() * valid_tokens
        token_count += valid_tokens

    if token_count == 0:
        raise ValueError("Evaluation data contains no tokens to score.")
    return loss_sum / token_count


@torch.no_grad()
def complete_text(
    current_model: Any,
    prompt: str,
    tokenizer: Any,
    device: torch.device,
) -> str:
    current_model.eval()
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    output_ids = current_model.generate(
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


def record_baseline(
    base_model: Any,
    tokenizer: Any,
    eval_loader: DataLoader,
    device: torch.device,
) -> tuple[float, dict[str, str]]:
    original_loss = evaluate_loss(base_model, eval_loader, device)
    original_completions = {
        prompt: complete_text(base_model, prompt, tokenizer, device)
        for prompt in TEST_PROMPTS
    }

    print(f"Original evaluation loss: {original_loss:.4f}")
    print(f"Original perplexity: {math.exp(original_loss):.2f}")
    for prompt, answer in original_completions.items():
        print("\nPROMPT:", prompt)
        print("CONTINUATION:", answer)
    return original_loss, original_completions


def attach_lora(base_model: Any, device: torch.device) -> Any:
    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=LORA_RANK,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        target_modules=["q_proj", "v_proj"],
        fan_in_fan_out=False,
        bias="none",
        init_lora_weights=True,
    )
    model = get_peft_model(base_model, lora_config).to(device)
    model.print_trainable_parameters()

    trainable_parameters = [
        name
        for name, parameter in model.named_parameters()
        if parameter.requires_grad
    ]
    if not trainable_parameters or not all(
        "lora_" in name for name in trainable_parameters
    ):
        raise RuntimeError("Expected only LoRA parameters to be trainable.")
    return model


def inspect_lora_parameters(model: Any) -> None:
    projection_name, projection = next(
        (
            (name, module)
            for name, module in model.named_modules()
            if hasattr(module, "lora_A") and "default" in module.lora_A
        ),
        (None, None),
    )
    if projection is None:
        raise RuntimeError("No LoRA projection was added to the model.")

    matrix_a = projection.lora_A["default"].weight
    matrix_b = projection.lora_B["default"].weight
    print("Selected projection:", projection_name)
    print("LoRA A shape:", tuple(matrix_a.shape))
    print("LoRA B shape:", tuple(matrix_b.shape))
    print("Parameters in A:", matrix_a.numel())
    print("Parameters in B:", matrix_b.numel())
    print(
        "Parameters in original projection:",
        projection.base_layer.weight.numel(),
    )
    print("LoRA scaling:", projection.scaling["default"])
    print("Initial B magnitude:", matrix_b.detach().abs().max().item())


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


def verify_initialized_model(
    model: Any,
    eval_loader: DataLoader,
    device: torch.device,
    original_loss: float,
) -> tuple[dict[str, str], dict[str, torch.Tensor]]:
    initialized_loss = evaluate_loss(model, eval_loader, device)
    print(f"Original loss:         {original_loss:.6f}")
    print(f"Initialized LoRA loss: {initialized_loss:.6f}")
    if not math.isclose(
        original_loss,
        initialized_loss,
        rel_tol=1e-5,
        abs_tol=1e-5,
    ):
        raise AssertionError("Initialized LoRA changed the baseline loss.")

    frozen_before = frozen_fingerprints(model)
    lora_before = {
        name: parameter.detach().cpu().clone()
        for name, parameter in model.named_parameters()
        if parameter.requires_grad
    }
    print("Verified: initialized LoRA preserves the baseline.")
    return frozen_before, lora_before


def train_model(
    model: Any,
    train_loader: DataLoader,
    device: torch.device,
) -> list[dict[str, Any]]:
    trainable_parameters = [
        parameter for parameter in model.parameters() if parameter.requires_grad
    ]
    optimizer = torch.optim.AdamW(
        trainable_parameters,
        lr=LEARNING_RATE,
        weight_decay=0.0,
    )
    training_history: list[dict[str, Any]] = []
    iterator = iter(train_loader)
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

        training_history.append({"step": step, "training_loss": loss.item()})
        if step == 1 or step % 5 == 0 or step == TRAINING_STEPS:
            print(
                f"Step {step}/{TRAINING_STEPS} "
                f"| Loss: {loss.item():.4f}"
            )

    print("\nLoRA training complete.")
    return training_history


def verify_training_changes(
    model: Any,
    frozen_before: dict[str, str],
    lora_before: dict[str, torch.Tensor],
) -> None:
    frozen_after = frozen_fingerprints(model)
    changed_frozen = [
        name
        for name, fingerprint in frozen_before.items()
        if fingerprint != frozen_after.get(name)
    ]
    changed_lora = []
    for name, parameter in model.named_parameters():
        if parameter.requires_grad:
            after = parameter.detach().cpu()
            before = lora_before[name]
            changed_lora.append(
                (
                    name,
                    not torch.equal(after, before),
                    (after - before).abs().mean().item(),
                )
            )

    print("\nLoRA parameter changes:")
    for name, changed, mean_absolute_change in changed_lora:
        print(
            f"{name}: changed={changed}, "
            f"mean absolute change={mean_absolute_change:.8f}"
        )
    print("Changed frozen tensors:", len(changed_frozen))
    if changed_frozen:
        raise AssertionError("Training changed frozen base-model parameters.")
    if not any(changed for _, changed, _ in changed_lora):
        raise AssertionError("Training did not change any LoRA parameters.")
    print("Verified: LoRA parameters changed; original parameters stayed identical.")


def compare_results(
    model: Any,
    tokenizer: Any,
    eval_loader: DataLoader,
    device: torch.device,
    original_loss: float,
    original_completions: dict[str, str],
) -> None:
    trained_loss = evaluate_loss(model, eval_loader, device)
    print("\nEvaluation results:")
    print(
        f"Before LoRA training | loss={original_loss:.6f} "
        f"| perplexity={math.exp(original_loss):.2f}"
    )
    print(
        f"After LoRA training  | loss={trained_loss:.6f} "
        f"| perplexity={math.exp(trained_loss):.2f}"
    )
    print("Evaluation loss reduction:", f"{original_loss - trained_loss:.4f}")

    for prompt in TEST_PROMPTS:
        print("\nPROMPT:", prompt)
        print("\nBEFORE:", original_completions[prompt])
        print("\nAFTER:", complete_text(model, prompt, tokenizer, device))
        print("=" * 70)


def verify_merge(
    model: Any,
    tokenizer: Any,
    device: torch.device,
) -> Any:
    model.eval()
    probe_inputs = tokenizer(
        "Vibration monitoring helps engineers",
        return_tensors="pt",
    ).to(device)
    with torch.no_grad():
        logits_before_merge = model(**probe_inputs).logits.detach().clone()

    merged_model = model.merge_and_unload(safe_merge=True)
    merged_model.eval()
    with torch.no_grad():
        logits_after_merge = merged_model(**probe_inputs).logits

    max_difference = (logits_before_merge - logits_after_merge).abs().max().item()
    print("Maximum logit difference after merging:", max_difference)
    torch.testing.assert_close(
        logits_before_merge,
        logits_after_merge,
        rtol=1e-4,
        atol=1e-4,
    )
    print("Verified: merging preserves predictions within numerical tolerance.")
    print(
        "Remaining LoRA parameter tensors:",
        sum("lora_" in name for name, _ in merged_model.named_parameters()),
    )
    return merged_model


def main() -> None:
    device = initialize()
    tokenizer, base_model = load_model(device)
    train_loader, eval_loader = load_loaders(tokenizer)
    print("Model loaded.")

    inspect_target_modules(base_model)
    original_loss, original_completions = record_baseline(
        base_model,
        tokenizer,
        eval_loader,
        device,
    )

    model = attach_lora(base_model, device)
    inspect_lora_parameters(model)
    frozen_before, lora_before = verify_initialized_model(
        model,
        eval_loader,
        device,
        original_loss,
    )

    train_model(model, train_loader, device)
    compare_results(
        model,
        tokenizer,
        eval_loader,
        device,
        original_loss,
        original_completions,
    )
    verify_training_changes(model, frozen_before, lora_before)

    if MERGE_LORA:
        verify_merge(model, tokenizer, device)


if __name__ == "__main__":
    main()
