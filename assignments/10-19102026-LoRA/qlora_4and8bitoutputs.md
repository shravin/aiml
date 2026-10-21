8 bit
---
```
/home/ravin/anaconda3/envs/aicondaenv/bin/python /home/ravin/aidev/aiml/assignments/10-19102026-LoRA/qlora-8bit.py
Device: cuda
GPU: NVIDIA GeForce RTX 5090 Laptop GPU

CPU-friendly uniform quantization demo
    Original     Code    Reconstructed   Absolute error
      -0.950        0           -0.950         0.000000
      -0.720        2           -0.702         0.018000
      -0.430        4           -0.454         0.024000
      -0.180        6           -0.206         0.026000
       0.060        8            0.042         0.018000
       0.290       10            0.290         0.000000
       0.570       12            0.538         0.032000
       0.910       15            0.910         0.000000
Number of available levels: 16
Mean absolute reconstruction error: 0.014750
Demo codes use uint8; packed 4-bit storage can fit two codes per byte.

Ideal weight-only storage for 1,000,000 parameters
        FP32: 3.815 MiB
        FP16: 1.907 MiB
Packed 4-bit: 0.477 MiB
Estimates exclude quantization metadata and other training memory.

Loading quantized model and setting up LoRA...
[transformers] `torch_dtype` is deprecated! Use `dtype` instead!
Loading weights: 100%|██████████| 76/76 [00:00<00:00, 237.37it/s]
8-bit linear layers: 24
Compute dtype: torch.bfloat16
Loaded model footprint: 115.74 MiB
trainable params: 73,728 || all params: 81,986,304 || trainable%: 0.0899
Trainable LoRA parameters:
  base_model.model.transformer.h.0.attn.c_attn.lora_A.default.weight: (4, 768) (torch.float32)
  base_model.model.transformer.h.0.attn.c_attn.lora_B.default.weight: (2304, 4) (torch.float32)
  base_model.model.transformer.h.1.attn.c_attn.lora_A.default.weight: (4, 768) (torch.float32)
  base_model.model.transformer.h.1.attn.c_attn.lora_B.default.weight: (2304, 4) (torch.float32)
  base_model.model.transformer.h.2.attn.c_attn.lora_A.default.weight: (4, 768) (torch.float32)
  base_model.model.transformer.h.2.attn.c_attn.lora_B.default.weight: (2304, 4) (torch.float32)
  base_model.model.transformer.h.3.attn.c_attn.lora_A.default.weight: (4, 768) (torch.float32)
  base_model.model.transformer.h.3.attn.c_attn.lora_B.default.weight: (2304, 4) (torch.float32)
  base_model.model.transformer.h.4.attn.c_attn.lora_A.default.weight: (4, 768) (torch.float32)
  base_model.model.transformer.h.4.attn.c_attn.lora_B.default.weight: (2304, 4) (torch.float32)
  base_model.model.transformer.h.5.attn.c_attn.lora_A.default.weight: (4, 768) (torch.float32)
  base_model.model.transformer.h.5.attn.c_attn.lora_B.default.weight: (2304, 4) (torch.float32)
[transformers] `loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.
Quantized baseline loss: 5.4733
Step 1/30 | Loss: 5.5116
Step 5/30 | Loss: 6.2680
Step 10/30 | Loss: 6.2172
Step 15/30 | Loss: 4.8050
Step 20/30 | Loss: 6.5009
Step 25/30 | Loss: 5.8082
Step 30/30 | Loss: 6.3874

Peak allocated GPU memory during training: 281.02 MiB

Evaluation results:
Quantized model before training | loss=5.473258 | perplexity=238.24
Quantized model with trained LoRA | loss=5.044989 | perplexity=155.24

PROMPT: Predictive maintenance is

BEFORE: a key component of the software. It is a tool that can be used to predict the performance of a given application.

AFTER: a critical component of the maintenance of the system.
======================================================================

PROMPT: When bearing temperature increases,

BEFORE: the temperature increases, and the temperature decreases.

AFTER: the temperature of the body increases.
======================================================================

PROMPT: Vibration monitoring helps engineers

BEFORE: to understand the impact of the stress on the brain.

AFTER: understand the impact of a change in the temperature of a device.
======================================================================

Changed LoRA tensors: 12
Verified: frozen base parameters stayed identical.

Process finished with exit code 0
```

4 bit
---
```
/home/ravin/anaconda3/envs/aicondaenv/bin/python /home/ravin/aidev/aiml/assignments/10-19102026-LoRA/qlora-4bit.py
Device: cuda
GPU: NVIDIA GeForce RTX 5090 Laptop GPU

CPU-friendly uniform quantization demo
    Original     Code    Reconstructed   Absolute error
      -0.950        0           -0.950         0.000000
      -0.720        2           -0.702         0.018000
      -0.430        4           -0.454         0.024000
      -0.180        6           -0.206         0.026000
       0.060        8            0.042         0.018000
       0.290       10            0.290         0.000000
       0.570       12            0.538         0.032000
       0.910       15            0.910         0.000000
Number of available levels: 16
Mean absolute reconstruction error: 0.014750
Demo codes use uint8; packed 4-bit storage can fit two codes per byte.

Ideal weight-only storage for 1,000,000 parameters
        FP32: 3.815 MiB
        FP16: 1.907 MiB
Packed 4-bit: 0.477 MiB
Estimates exclude quantization metadata and other training memory.

Loading quantized model and setting up LoRA...
[transformers] `torch_dtype` is deprecated! Use `dtype` instead!
Loading weights: 100%|██████████| 76/76 [00:00<00:00, 349.62it/s]
4-bit linear layers: 24
Compute dtype: torch.bfloat16
Loaded model footprint: 95.49 MiB
trainable params: 73,728 || all params: 81,986,304 || trainable%: 0.0899
Trainable LoRA parameters:
  base_model.model.transformer.h.0.attn.c_attn.lora_A.default.weight: (4, 768) (torch.float32)
  base_model.model.transformer.h.0.attn.c_attn.lora_B.default.weight: (2304, 4) (torch.float32)
  base_model.model.transformer.h.1.attn.c_attn.lora_A.default.weight: (4, 768) (torch.float32)
  base_model.model.transformer.h.1.attn.c_attn.lora_B.default.weight: (2304, 4) (torch.float32)
  base_model.model.transformer.h.2.attn.c_attn.lora_A.default.weight: (4, 768) (torch.float32)
  base_model.model.transformer.h.2.attn.c_attn.lora_B.default.weight: (2304, 4) (torch.float32)
  base_model.model.transformer.h.3.attn.c_attn.lora_A.default.weight: (4, 768) (torch.float32)
  base_model.model.transformer.h.3.attn.c_attn.lora_B.default.weight: (2304, 4) (torch.float32)
  base_model.model.transformer.h.4.attn.c_attn.lora_A.default.weight: (4, 768) (torch.float32)
  base_model.model.transformer.h.4.attn.c_attn.lora_B.default.weight: (2304, 4) (torch.float32)
  base_model.model.transformer.h.5.attn.c_attn.lora_A.default.weight: (4, 768) (torch.float32)
  base_model.model.transformer.h.5.attn.c_attn.lora_B.default.weight: (2304, 4) (torch.float32)
[transformers] `loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.
Quantized baseline loss: 5.5552
Step 1/30 | Loss: 5.4570
Step 5/30 | Loss: 6.2534
Step 10/30 | Loss: 6.1498
Step 15/30 | Loss: 4.9490
Step 20/30 | Loss: 6.4895
Step 25/30 | Loss: 5.8042
Step 30/30 | Loss: 6.4758

Peak allocated GPU memory during training: 258.91 MiB

Evaluation results:
Quantized model before training | loss=5.555188 | perplexity=258.58
Quantized model with trained LoRA | loss=5.085584 | perplexity=161.67

PROMPT: Predictive maintenance is

BEFORE: a key component of the human brain. It is important to understand the role of the brain in the development of cognitive and emotional development.

AFTER: a critical component of the maintenance of the system.
======================================================================

PROMPT: When bearing temperature increases,

BEFORE: the body is more sensitive to temperature than the body.

AFTER: the temperature of the body increases.
======================================================================

PROMPT: Vibration monitoring helps engineers

BEFORE: to better understand the impact of the stress on the brain.

AFTER: to detect and diagnose a problem.
======================================================================

Changed LoRA tensors: 12
Verified: frozen base parameters stayed identical.

Process finished with exit code 0
```