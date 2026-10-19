Q1: Change LORA_RANK from 4 to 8.
---
Predict the trainable parameter count.

### Ans: 
When we changed the count we saw that the `trainable_params` changed drastically. Here is the output before and after. Reason is simple: LoRA is applied to the q_proj and v_proj layers. For each layer, its added matrices have `rank × input size and output size × rank parameters, so the count is rank × (input size + output size)`

Before:  
`trainable params: 544,768 || all params: 1,544,259,072 || trainable%: 0.0353`

After:  
`trainable params: 1,089,536 || all params: 1,544,803,840 || trainable%: 0.0705`

Q2: Change LORA_ALPHA from 8 to 16.
---
What happens to the scaling factor?

### Ans: 
Both runs improved on the evaluation texts: loss fell from 4.1166 to about 2.8, and perplexity fell from 61.35 to about 15–16.

The second run is slightly better on this evaluation set:

Loss is lower by about 0.099 (2.7033 vs. 2.8023).
Perplexity is about 9% lower (14.93 vs. 16.48).
Its loss reduction is correspondingly larger (1.4133 vs. 1.3143).
If the only setting you changed between runs was LORA_ALPHA, the result suggests the alpha used in the second run worked better for these particular evaluation texts. It doesn’t establish that it will be better generally—the evaluation set is small, so compare the generated completions too, and treat this as an experiment rather than a definitive conclusion.

Before:  
```
Evaluation results:
Before LoRA training | loss=4.116600 | perplexity=61.35
After LoRA training  | loss=2.802286 | perplexity=16.48
Evaluation loss reduction: 1.3143
```

After:  
```
Evaluation results:
Before LoRA training | loss=4.116600 | perplexity=61.35
After LoRA training  | loss=2.703294 | perplexity=14.93
Evaluation loss reduction: 1.4133
```

Q3: Compare 30 and 60 training steps with LORA_RANK=8, LORA_ALPHA=16
---

### Ans: 
The 30-step run performed better on the evaluation set:

30 steps: evaluation loss 2.7033, perplexity 14.93, loss reduction 1.4133
60 steps: evaluation loss 3.7934, perplexity 44.41, loss reduction 0.3232
Lower evaluation loss and perplexity are better, so the 60-step result is substantially worse on these held-out examples—even though it trained longer. More steps don’t guarantee better results: continued training can start to overfit the training texts or move the model away from a solution that worked better on the evaluation set.
Before:  
```
Evaluation results:
Before LoRA training | loss=4.116600 | perplexity=61.35
After LoRA training  | loss=2.703294 | perplexity=14.93
Evaluation loss reduction: 1.4133
```

After:  
```
Evaluation results:
Before LoRA training | loss=4.116600 | perplexity=61.35
After LoRA training  | loss=3.793437 | perplexity=44.41
Evaluation loss reduction: 0.3232
```

Q4: Why does setting B to zero preserve the original model initially?
---
### Ans:
LoRA modifies a weight matrix (W) by adding a low-rank update:


At initialization, (B) is all zeros, so (BA=0). The update is therefore zero, and (W_{\text{new}}=W): the model initially behaves exactly like the original, regardless of the alpha value. During training, (B) and (A) are learned, allowing the LoRA update to become nonzero.

Q5: How does LoRA differ from a nonlinear bottleneck adapter?
---
### Ans:
LoRA adds a low-rank update to an existing weight matrix: (W_{\text{new}} = W + BA) (usually scaled by (\text{alpha}/\text{rank})). It keeps the original weights frozen and trains the small matrices (A) and (B). The update is linear and can often be merged into the original weights for inference.

A nonlinear bottleneck adapter adds a small neural network between model layers. It typically projects activations down to a smaller dimension, applies a nonlinear activation, then projects them back up. It trains those added layers and remains an extra computation in the model.

In short: LoRA learns a compact, linear change to existing weights; a bottleneck adapter learns a separate nonlinear transformation of activations.

Q6: Why can LoRA be merged into a weight matrix?
---
### Ans:
LoRA adds a linear low-rank update to a weight matrix. For input (x), the adapted layer computes:

[
Wx + \frac{\alpha}{r}BAx
]

By associativity and linearity, this is equivalent to applying one modified matrix:

[
\left(W + \frac{\alpha}{r}BA\right)x
]

So after training, the update can be added directly to (W), removing the need to compute the separate LoRA branches during inference. This works because LoRA’s update is linear; a nonlinear adapter generally cannot be folded into a single weight matrix.