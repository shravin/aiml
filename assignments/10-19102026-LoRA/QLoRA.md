
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


Compare LoRA and QLoRA - Is lower memory guaranteed to produce better accuracy?
---
LoRA fine-tunes a model by freezing its original weights and training small low-rank adapter matrices. QLoRA does the same, but stores the frozen base weights in a quantized format, reducing memory use; adapters are still trained.

Lower memory use does not guarantee better accuracy. Quantization can introduce small errors, and accuracy depends on factors like the model, data, and training setup. Lower memory may let you fine-tune a larger model or use a larger batch, which can help—but results need to be evaluated.