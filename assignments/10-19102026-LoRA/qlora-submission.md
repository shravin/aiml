
Why does 4-bit quantization provide 16 possible codes?
---
Four bits can represent (2^4 = 16) distinct binary patterns, so they provide 16 possible codes.

Why do reconstructed weights differ from the original weights?
---
Reconstructed weights differ because quantization maps each original weight to one of a limited number of representable values. This rounding introduces some information loss, so the reconstructed values are approximations rather than exact copies.

What is the difference between storage dtype and compute dtype?
---
Storage dtype is the format used to keep weights in memory or on disk, often a low-bit format to save space. Compute dtype is the format used for arithmetic during model operations, often a higher-precision format for speed or numerical stability. Quantized weights may be converted to the compute dtype when used.

Which parameters are trained in QLoRA?
---
QLoRA keeps the pretrained base model weights frozen and trains the small LoRA adapter parameters—typically low-rank matrices added to selected layers. Any extra modules explicitly marked trainable, such as a task-specific output head, may also be updated.

Why does total training memory exceed the size of the stored weights?
---
Because training memory includes more than the stored weights: activations saved for backpropagation, gradients, optimizer states, temporary computation buffers, and sometimes higher-precision copies of weights. These can add substantially to the memory needed during training.

Compare ranks 4 and 8 using a fresh model each time.
---
Comparison between 4 bit and 8 bit QLoRA


| Measure | 8-bit | 4-bit | Difference |
|---|---:|---:|---|
| Quantized model footprint | 115.74 MiB | 95.49 MiB | 4-bit is 20.25 MiB smaller |
| Peak training GPU memory | 281.02 MiB | 258.91 MiB | 4-bit is 22.11 MiB lower |
| Evaluation loss (before → after) | 5.4733 → 5.0450 | 5.5552 → 5.0856 | Both improved |
| Final perplexity | 155.24 | 161.67 | 8-bit is slightly lower |
| Trainable LoRA parameters | 73,728 | 73,728 | Same |

Findings: In these runs, 4-bit used less memory, while 8-bit finished with slightly better evaluation metrics. Both improved after LoRA training, and both verified that the frozen parameters stayed unchanged. The generated answers don’t show a clear qualitative winner.

Compare LoRA and QLoRA - Is lower memory guaranteed to produce better accuracy?
---
LoRA fine-tunes a model by freezing its original weights and training small low-rank adapter matrices. QLoRA does the same, but stores the frozen base weights in a quantized format, reducing memory use; adapters are still trained.

Lower memory use does not guarantee better accuracy. Quantization can introduce small errors, and accuracy depends on factors like the model, data, and training setup. Lower memory may let you fine-tune a larger model or use a larger batch, which can help—but results need to be evaluated.

Run the Python version of the notebook with:

```bash
python assignments/10-19102026-LoRA/qlora-8bit.py --device cpu
```

This runs the conceptual quantization exercise. To run QLoRA training on a supported NVIDIA GPU with the local DistilGPT-2 model:

```bash
python assignments/10-19102026-LoRA/qlora-8bit.py --device cuda
```

Use `--model-name` to specify a different local model directory. GPU training requires PyTorch, Transformers, PEFT, and bitsandbytes.
