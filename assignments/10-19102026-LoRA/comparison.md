/home/ravin/anaconda3/envs/aicondaenv/bin/python /home/ravin/aidev/aiml/assignments/10-19102026-LoRA/lora-ai.py 
Device: cuda
GPU: NVIDIA GeForce RTX 5090 Laptop GPU
LoRA rank: 4
LoRA alpha: 8
Scaling factor: 2.0
Training examples: 12
Evaluation examples: 4
Loading weights: 100%|██████████| 338/338 [00:00<00:00, 16511.47it/s]
Model loaded.

Attention projections selected for LoRA:
model.layers.0.self_attn.q_proj (1536, 1536)
model.layers.0.self_attn.v_proj (256, 1536)
model.layers.1.self_attn.q_proj (1536, 1536)
model.layers.1.self_attn.v_proj (256, 1536)
model.layers.2.self_attn.q_proj (1536, 1536)
model.layers.2.self_attn.v_proj (256, 1536)
model.layers.3.self_attn.q_proj (1536, 1536)
model.layers.3.self_attn.v_proj (256, 1536)
model.layers.4.self_attn.q_proj (1536, 1536)
model.layers.4.self_attn.v_proj (256, 1536)
model.layers.5.self_attn.q_proj (1536, 1536)
model.layers.5.self_attn.v_proj (256, 1536)
model.layers.6.self_attn.q_proj (1536, 1536)
model.layers.6.self_attn.v_proj (256, 1536)
model.layers.7.self_attn.q_proj (1536, 1536)
model.layers.7.self_attn.v_proj (256, 1536)
model.layers.8.self_attn.q_proj (1536, 1536)
model.layers.8.self_attn.v_proj (256, 1536)
model.layers.9.self_attn.q_proj (1536, 1536)
model.layers.9.self_attn.v_proj (256, 1536)
model.layers.10.self_attn.q_proj (1536, 1536)
model.layers.10.self_attn.v_proj (256, 1536)
model.layers.11.self_attn.q_proj (1536, 1536)
model.layers.11.self_attn.v_proj (256, 1536)
model.layers.12.self_attn.q_proj (1536, 1536)
model.layers.12.self_attn.v_proj (256, 1536)
model.layers.13.self_attn.q_proj (1536, 1536)
model.layers.13.self_attn.v_proj (256, 1536)
model.layers.14.self_attn.q_proj (1536, 1536)
model.layers.14.self_attn.v_proj (256, 1536)
model.layers.15.self_attn.q_proj (1536, 1536)
model.layers.15.self_attn.v_proj (256, 1536)
model.layers.16.self_attn.q_proj (1536, 1536)
model.layers.16.self_attn.v_proj (256, 1536)
model.layers.17.self_attn.q_proj (1536, 1536)
model.layers.17.self_attn.v_proj (256, 1536)
model.layers.18.self_attn.q_proj (1536, 1536)
model.layers.18.self_attn.v_proj (256, 1536)
model.layers.19.self_attn.q_proj (1536, 1536)
model.layers.19.self_attn.v_proj (256, 1536)
model.layers.20.self_attn.q_proj (1536, 1536)
model.layers.20.self_attn.v_proj (256, 1536)
model.layers.21.self_attn.q_proj (1536, 1536)
model.layers.21.self_attn.v_proj (256, 1536)
model.layers.22.self_attn.q_proj (1536, 1536)
model.layers.22.self_attn.v_proj (256, 1536)
model.layers.23.self_attn.q_proj (1536, 1536)
model.layers.23.self_attn.v_proj (256, 1536)
model.layers.24.self_attn.q_proj (1536, 1536)
model.layers.24.self_attn.v_proj (256, 1536)
model.layers.25.self_attn.q_proj (1536, 1536)
model.layers.25.self_attn.v_proj (256, 1536)
model.layers.26.self_attn.q_proj (1536, 1536)
model.layers.26.self_attn.v_proj (256, 1536)
model.layers.27.self_attn.q_proj (1536, 1536)
model.layers.27.self_attn.v_proj (256, 1536)
Original evaluation loss: 4.1166
Original perplexity: 61.35

PROMPT: Predictive maintenance is
CONTINUATION: a proactive approach to equipment maintenance that aims to prevent equipment failure before it occurs. It involves using data analytics and machine learning algorithms to predict when equipment will fail based on its performance and usage patterns. Predictive maintenance can help organizations

PROMPT: When bearing temperature increases,
CONTINUATION: the viscosity of the oil ____.
A. Increases
B. Decreases
C. Remains unchanged
D. Is uncertain
Answer:
B

The main reason for the increase in the temperature of the oil in the

PROMPT: Vibration monitoring helps engineers
CONTINUATION: to identify and prevent equipment failures. It is a critical part of the maintenance process, and it can help to reduce downtime and increase productivity. Vibration monitoring is a process of measuring the vibration of a machine or system. It
trainable params: 544,768 || all params: 1,544,259,072 || trainable%: 0.0353
Selected projection: base_model.model.model.layers.0.self_attn.q_proj
LoRA A shape: (4, 1536)
LoRA B shape: (1536, 4)
Parameters in A: 6144
Parameters in B: 6144
Parameters in original projection: 2359296
LoRA scaling: 2.0
Initial B magnitude: 0.0
Original loss:         4.116600
Initialized LoRA loss: 4.116600
Verified: initialized LoRA preserves the baseline.
Step 1/30 | Loss: 5.0274
Step 5/30 | Loss: 3.4424
Step 10/30 | Loss: 2.7583
Step 15/30 | Loss: 4.2777
Step 20/30 | Loss: 3.6408
Step 25/30 | Loss: 3.2622
Step 30/30 | Loss: 1.6192

LoRA training complete.

Evaluation results:
Before LoRA training | loss=4.116600 | perplexity=61.35
After LoRA training  | loss=2.806840 | perplexity=16.56
Evaluation loss reduction: 1.3098

PROMPT: Predictive maintenance is

BEFORE: a proactive approach to equipment maintenance that aims to prevent equipment failure before it occurs. It involves using data analytics and machine learning algorithms to predict when equipment will fail based on its performance and usage patterns. Predictive maintenance can help organizations

AFTER: a proactive approach to equipment maintenance that uses data from sensors and other monitoring systems to predict when equipment will fail.
======================================================================

PROMPT: When bearing temperature increases,

BEFORE: the viscosity of the oil ____.
A. Increases
B. Decreases
C. Remains unchanged
D. Is uncertain
Answer:
B

The main reason for the increase in the temperature of the oil in the

AFTER: the bearing clearance should be reduced.
A. Correct
B. Incorrect
Answer:
A

The main function of a transformer breather is to remove moisture and impurities from the oil.
A. Correct
B. Incorrect
======================================================================

PROMPT: Vibration monitoring helps engineers

BEFORE: to identify and prevent equipment failures. It is a critical part of the maintenance process, and it can help to reduce downtime and increase productivity. Vibration monitoring is a process of measuring the vibration of a machine or system. It

AFTER: detect potential problems before they become major issues.
======================================================================

LoRA parameter changes:
base_model.model.model.layers.0.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00298021
base_model.model.model.layers.0.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00290932
base_model.model.model.layers.0.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00360849
base_model.model.model.layers.0.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00334305
base_model.model.model.layers.1.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00360324
base_model.model.model.layers.1.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00343791
base_model.model.model.layers.1.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00335914
base_model.model.model.layers.1.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00389453
base_model.model.model.layers.2.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00285597
base_model.model.model.layers.2.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00279739
base_model.model.model.layers.2.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00411533
base_model.model.model.layers.2.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00399330
base_model.model.model.layers.3.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00311354
base_model.model.model.layers.3.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00313851
base_model.model.model.layers.3.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00394138
base_model.model.model.layers.3.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00366129
base_model.model.model.layers.4.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00302162
base_model.model.model.layers.4.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00293440
base_model.model.model.layers.4.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00496043
base_model.model.model.layers.4.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00421078
base_model.model.model.layers.5.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00318438
base_model.model.model.layers.5.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00318344
base_model.model.model.layers.5.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00363216
base_model.model.model.layers.5.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00391767
base_model.model.model.layers.6.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00414765
base_model.model.model.layers.6.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00360901
base_model.model.model.layers.6.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00493718
base_model.model.model.layers.6.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00377385
base_model.model.model.layers.7.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00440721
base_model.model.model.layers.7.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00392845
base_model.model.model.layers.7.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00574731
base_model.model.model.layers.7.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00449568
base_model.model.model.layers.8.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00334025
base_model.model.model.layers.8.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00333053
base_model.model.model.layers.8.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00500575
base_model.model.model.layers.8.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00401743
base_model.model.model.layers.9.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00379970
base_model.model.model.layers.9.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00390328
base_model.model.model.layers.9.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00550113
base_model.model.model.layers.9.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00408462
base_model.model.model.layers.10.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00285630
base_model.model.model.layers.10.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00314381
base_model.model.model.layers.10.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00566994
base_model.model.model.layers.10.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00407744
base_model.model.model.layers.11.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00358082
base_model.model.model.layers.11.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00361391
base_model.model.model.layers.11.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00615432
base_model.model.model.layers.11.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00464546
base_model.model.model.layers.12.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00341837
base_model.model.model.layers.12.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00341267
base_model.model.model.layers.12.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00699414
base_model.model.model.layers.12.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00463133
base_model.model.model.layers.13.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00356830
base_model.model.model.layers.13.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00340845
base_model.model.model.layers.13.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00617261
base_model.model.model.layers.13.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00447643
base_model.model.model.layers.14.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00376922
base_model.model.model.layers.14.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00380784
base_model.model.model.layers.14.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00795708
base_model.model.model.layers.14.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00501157
base_model.model.model.layers.15.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00463532
base_model.model.model.layers.15.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00428294
base_model.model.model.layers.15.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00619746
base_model.model.model.layers.15.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00496612
base_model.model.model.layers.16.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00316664
base_model.model.model.layers.16.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00307224
base_model.model.model.layers.16.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00642653
base_model.model.model.layers.16.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00460686
base_model.model.model.layers.17.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00616540
base_model.model.model.layers.17.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00552920
base_model.model.model.layers.17.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00705736
base_model.model.model.layers.17.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00610394
base_model.model.model.layers.18.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00385049
base_model.model.model.layers.18.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00345577
base_model.model.model.layers.18.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00652718
base_model.model.model.layers.18.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00543676
base_model.model.model.layers.19.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00548276
base_model.model.model.layers.19.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00492789
base_model.model.model.layers.19.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00747043
base_model.model.model.layers.19.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00642638
base_model.model.model.layers.20.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00417507
base_model.model.model.layers.20.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00428728
base_model.model.model.layers.20.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00538873
base_model.model.model.layers.20.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00426728
base_model.model.model.layers.21.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00391205
base_model.model.model.layers.21.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00405480
base_model.model.model.layers.21.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00665610
base_model.model.model.layers.21.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00461373
base_model.model.model.layers.22.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00410867
base_model.model.model.layers.22.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00417925
base_model.model.model.layers.22.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00551004
base_model.model.model.layers.22.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00421157
base_model.model.model.layers.23.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00342902
base_model.model.model.layers.23.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00349660
base_model.model.model.layers.23.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00853187
base_model.model.model.layers.23.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00601475
base_model.model.model.layers.24.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00439055
base_model.model.model.layers.24.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00385306
base_model.model.model.layers.24.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00743647
base_model.model.model.layers.24.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00524974
base_model.model.model.layers.25.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00660024
base_model.model.model.layers.25.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00485902
base_model.model.model.layers.25.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00768862
base_model.model.model.layers.25.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00701979
base_model.model.model.layers.26.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00507970
base_model.model.model.layers.26.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00404663
base_model.model.model.layers.26.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00743274
base_model.model.model.layers.26.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00458970
base_model.model.model.layers.27.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00382754
base_model.model.model.layers.27.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00356318
base_model.model.model.layers.27.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00517952
base_model.model.model.layers.27.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00425410
Changed frozen tensors: 0
Verified: LoRA parameters changed; original parameters stayed identical.

Process finished with exit code 0

----

/home/ravin/anaconda3/envs/aicondaenv/bin/python /home/ravin/aidev/aiml/assignments/10-19102026-LoRA/lora-ai.py 
Device: cuda
GPU: NVIDIA GeForce RTX 5090 Laptop GPU
LoRA rank: 8
LoRA alpha: 8
Scaling factor: 1.0
Training examples: 12
Evaluation examples: 4
Loading weights: 100%|██████████| 338/338 [00:00<00:00, 15434.00it/s]
Model loaded.

Attention projections selected for LoRA:
model.layers.0.self_attn.q_proj (1536, 1536)
model.layers.0.self_attn.v_proj (256, 1536)
model.layers.1.self_attn.q_proj (1536, 1536)
model.layers.1.self_attn.v_proj (256, 1536)
model.layers.2.self_attn.q_proj (1536, 1536)
model.layers.2.self_attn.v_proj (256, 1536)
model.layers.3.self_attn.q_proj (1536, 1536)
model.layers.3.self_attn.v_proj (256, 1536)
model.layers.4.self_attn.q_proj (1536, 1536)
model.layers.4.self_attn.v_proj (256, 1536)
model.layers.5.self_attn.q_proj (1536, 1536)
model.layers.5.self_attn.v_proj (256, 1536)
model.layers.6.self_attn.q_proj (1536, 1536)
model.layers.6.self_attn.v_proj (256, 1536)
model.layers.7.self_attn.q_proj (1536, 1536)
model.layers.7.self_attn.v_proj (256, 1536)
model.layers.8.self_attn.q_proj (1536, 1536)
model.layers.8.self_attn.v_proj (256, 1536)
model.layers.9.self_attn.q_proj (1536, 1536)
model.layers.9.self_attn.v_proj (256, 1536)
model.layers.10.self_attn.q_proj (1536, 1536)
model.layers.10.self_attn.v_proj (256, 1536)
model.layers.11.self_attn.q_proj (1536, 1536)
model.layers.11.self_attn.v_proj (256, 1536)
model.layers.12.self_attn.q_proj (1536, 1536)
model.layers.12.self_attn.v_proj (256, 1536)
model.layers.13.self_attn.q_proj (1536, 1536)
model.layers.13.self_attn.v_proj (256, 1536)
model.layers.14.self_attn.q_proj (1536, 1536)
model.layers.14.self_attn.v_proj (256, 1536)
model.layers.15.self_attn.q_proj (1536, 1536)
model.layers.15.self_attn.v_proj (256, 1536)
model.layers.16.self_attn.q_proj (1536, 1536)
model.layers.16.self_attn.v_proj (256, 1536)
model.layers.17.self_attn.q_proj (1536, 1536)
model.layers.17.self_attn.v_proj (256, 1536)
model.layers.18.self_attn.q_proj (1536, 1536)
model.layers.18.self_attn.v_proj (256, 1536)
model.layers.19.self_attn.q_proj (1536, 1536)
model.layers.19.self_attn.v_proj (256, 1536)
model.layers.20.self_attn.q_proj (1536, 1536)
model.layers.20.self_attn.v_proj (256, 1536)
model.layers.21.self_attn.q_proj (1536, 1536)
model.layers.21.self_attn.v_proj (256, 1536)
model.layers.22.self_attn.q_proj (1536, 1536)
model.layers.22.self_attn.v_proj (256, 1536)
model.layers.23.self_attn.q_proj (1536, 1536)
model.layers.23.self_attn.v_proj (256, 1536)
model.layers.24.self_attn.q_proj (1536, 1536)
model.layers.24.self_attn.v_proj (256, 1536)
model.layers.25.self_attn.q_proj (1536, 1536)
model.layers.25.self_attn.v_proj (256, 1536)
model.layers.26.self_attn.q_proj (1536, 1536)
model.layers.26.self_attn.v_proj (256, 1536)
model.layers.27.self_attn.q_proj (1536, 1536)
model.layers.27.self_attn.v_proj (256, 1536)
Original evaluation loss: 4.1166
Original perplexity: 61.35

PROMPT: Predictive maintenance is
CONTINUATION: a proactive approach to equipment maintenance that aims to prevent equipment failure before it occurs. It involves using data analytics and machine learning algorithms to predict when equipment will fail based on its performance and usage patterns. Predictive maintenance can help organizations

PROMPT: When bearing temperature increases,
CONTINUATION: the viscosity of the oil ____.
A. Increases
B. Decreases
C. Remains unchanged
D. Is uncertain
Answer:
B

The main reason for the increase in the temperature of the oil in the

PROMPT: Vibration monitoring helps engineers
CONTINUATION: to identify and prevent equipment failures. It is a critical part of the maintenance process, and it can help to reduce downtime and increase productivity. Vibration monitoring is a process of measuring the vibration of a machine or system. It
trainable params: 1,089,536 || all params: 1,544,803,840 || trainable%: 0.0705
Selected projection: base_model.model.model.layers.0.self_attn.q_proj
LoRA A shape: (8, 1536)
LoRA B shape: (1536, 8)
Parameters in A: 12288
Parameters in B: 12288
Parameters in original projection: 2359296
LoRA scaling: 1.0
Initial B magnitude: 0.0
Original loss:         4.116600
Initialized LoRA loss: 4.116600
Verified: initialized LoRA preserves the baseline.
Step 1/30 | Loss: 2.9760
Step 5/30 | Loss: 2.5781
Step 10/30 | Loss: 2.7836
Step 15/30 | Loss: 3.3180
Step 20/30 | Loss: 2.3940
Step 25/30 | Loss: 2.6921
Step 30/30 | Loss: 2.9503

LoRA training complete.

Evaluation results:
Before LoRA training | loss=4.116600 | perplexity=61.35
After LoRA training  | loss=2.802286 | perplexity=16.48
Evaluation loss reduction: 1.3143

PROMPT: Predictive maintenance is

BEFORE: a proactive approach to equipment maintenance that aims to prevent equipment failure before it occurs. It involves using data analytics and machine learning algorithms to predict when equipment will fail based on its performance and usage patterns. Predictive maintenance can help organizations

AFTER: a proactive approach to equipment maintenance that uses data from sensors and other monitoring devices to predict when equipment will fail.
======================================================================

PROMPT: When bearing temperature increases,

BEFORE: the viscosity of the oil ____.
A. Increases
B. Decreases
C. Remains unchanged
D. Is uncertain
Answer:
B

The main reason for the increase in the temperature of the oil in the

AFTER: the bearing clearance should be reduced.
A. Correct
B. Incorrect
Answer:
A

The main function of a transformer breather is to remove impurities and moisture from the air being drawn in.
======================================================================

PROMPT: Vibration monitoring helps engineers

BEFORE: to identify and prevent equipment failures. It is a critical part of the maintenance process, and it can help to reduce downtime and increase productivity. Vibration monitoring is a process of measuring the vibration of a machine or system. It

AFTER: detect potential problems before they become major issues.
======================================================================

LoRA parameter changes:
base_model.model.model.layers.0.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00317122
base_model.model.model.layers.0.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00302077
base_model.model.model.layers.0.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00399363
base_model.model.model.layers.0.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00384075
base_model.model.model.layers.1.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00336367
base_model.model.model.layers.1.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00326393
base_model.model.model.layers.1.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00326077
base_model.model.model.layers.1.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00351976
base_model.model.model.layers.2.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00274223
base_model.model.model.layers.2.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00273729
base_model.model.model.layers.2.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00370359
base_model.model.model.layers.2.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00378196
base_model.model.model.layers.3.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00319752
base_model.model.model.layers.3.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00301423
base_model.model.model.layers.3.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00394132
base_model.model.model.layers.3.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00368741
base_model.model.model.layers.4.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00301281
base_model.model.model.layers.4.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00299884
base_model.model.model.layers.4.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00481092
base_model.model.model.layers.4.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00408887
base_model.model.model.layers.5.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00343539
base_model.model.model.layers.5.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00325120
base_model.model.model.layers.5.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00346151
base_model.model.model.layers.5.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00413909
base_model.model.model.layers.6.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00392306
base_model.model.model.layers.6.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00357558
base_model.model.model.layers.6.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00476366
base_model.model.model.layers.6.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00377848
base_model.model.model.layers.7.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00398866
base_model.model.model.layers.7.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00398771
base_model.model.model.layers.7.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00551778
base_model.model.model.layers.7.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00434729
base_model.model.model.layers.8.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00355752
base_model.model.model.layers.8.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00355622
base_model.model.model.layers.8.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00487809
base_model.model.model.layers.8.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00413439
base_model.model.model.layers.9.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00411681
base_model.model.model.layers.9.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00397752
base_model.model.model.layers.9.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00521307
base_model.model.model.layers.9.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00403602
base_model.model.model.layers.10.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00337525
base_model.model.model.layers.10.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00357423
base_model.model.model.layers.10.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00524855
base_model.model.model.layers.10.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00431716
base_model.model.model.layers.11.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00351111
base_model.model.model.layers.11.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00348610
base_model.model.model.layers.11.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00567078
base_model.model.model.layers.11.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00445125
base_model.model.model.layers.12.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00378760
base_model.model.model.layers.12.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00361299
base_model.model.model.layers.12.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00653792
base_model.model.model.layers.12.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00451786
base_model.model.model.layers.13.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00354625
base_model.model.model.layers.13.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00340916
base_model.model.model.layers.13.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00642767
base_model.model.model.layers.13.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00468342
base_model.model.model.layers.14.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00404572
base_model.model.model.layers.14.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00373113
base_model.model.model.layers.14.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00777501
base_model.model.model.layers.14.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00489389
base_model.model.model.layers.15.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00396325
base_model.model.model.layers.15.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00407841
base_model.model.model.layers.15.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00598666
base_model.model.model.layers.15.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00502965
base_model.model.model.layers.16.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00415714
base_model.model.model.layers.16.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00388421
base_model.model.model.layers.16.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00665027
base_model.model.model.layers.16.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00476908
base_model.model.model.layers.17.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00615457
base_model.model.model.layers.17.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00548239
base_model.model.model.layers.17.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00713742
base_model.model.model.layers.17.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00589024
base_model.model.model.layers.18.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00437932
base_model.model.model.layers.18.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00401278
base_model.model.model.layers.18.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00640479
base_model.model.model.layers.18.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00552298
base_model.model.model.layers.19.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00525922
base_model.model.model.layers.19.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00476091
base_model.model.model.layers.19.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00746445
base_model.model.model.layers.19.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00654864
base_model.model.model.layers.20.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00345797
base_model.model.model.layers.20.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00356526
base_model.model.model.layers.20.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00591778
base_model.model.model.layers.20.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00437425
base_model.model.model.layers.21.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00390671
base_model.model.model.layers.21.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00393730
base_model.model.model.layers.21.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00692269
base_model.model.model.layers.21.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00469737
base_model.model.model.layers.22.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00433731
base_model.model.model.layers.22.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00422842
base_model.model.model.layers.22.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00646600
base_model.model.model.layers.22.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00460074
base_model.model.model.layers.23.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00412358
base_model.model.model.layers.23.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00371128
base_model.model.model.layers.23.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00831436
base_model.model.model.layers.23.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00597261
base_model.model.model.layers.24.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00426014
base_model.model.model.layers.24.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00407555
base_model.model.model.layers.24.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00764896
base_model.model.model.layers.24.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00569475
base_model.model.model.layers.25.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00674808
base_model.model.model.layers.25.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00508803
base_model.model.model.layers.25.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00794767
base_model.model.model.layers.25.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00726292
base_model.model.model.layers.26.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00482999
base_model.model.model.layers.26.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00411797
base_model.model.model.layers.26.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00710911
base_model.model.model.layers.26.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00466460
base_model.model.model.layers.27.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00457579
base_model.model.model.layers.27.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00376112
base_model.model.model.layers.27.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00577683
base_model.model.model.layers.27.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00442066
Changed frozen tensors: 0
Verified: LoRA parameters changed; original parameters stayed identical.

Process finished with exit code 0

---
LORA_ALPHA = 16

/home/ravin/anaconda3/envs/aicondaenv/bin/python /home/ravin/aidev/aiml/assignments/10-19102026-LoRA/lora-ai.py 
Device: cuda
GPU: NVIDIA GeForce RTX 5090 Laptop GPU
LoRA rank: 8
LoRA alpha: 16
Scaling factor: 2.0
Training examples: 12
Evaluation examples: 4
Loading weights: 100%|██████████| 338/338 [00:00<00:00, 16086.36it/s]
Model loaded.

Attention projections selected for LoRA:
model.layers.0.self_attn.q_proj (1536, 1536)
model.layers.0.self_attn.v_proj (256, 1536)
model.layers.1.self_attn.q_proj (1536, 1536)
model.layers.1.self_attn.v_proj (256, 1536)
model.layers.2.self_attn.q_proj (1536, 1536)
model.layers.2.self_attn.v_proj (256, 1536)
model.layers.3.self_attn.q_proj (1536, 1536)
model.layers.3.self_attn.v_proj (256, 1536)
model.layers.4.self_attn.q_proj (1536, 1536)
model.layers.4.self_attn.v_proj (256, 1536)
model.layers.5.self_attn.q_proj (1536, 1536)
model.layers.5.self_attn.v_proj (256, 1536)
model.layers.6.self_attn.q_proj (1536, 1536)
model.layers.6.self_attn.v_proj (256, 1536)
model.layers.7.self_attn.q_proj (1536, 1536)
model.layers.7.self_attn.v_proj (256, 1536)
model.layers.8.self_attn.q_proj (1536, 1536)
model.layers.8.self_attn.v_proj (256, 1536)
model.layers.9.self_attn.q_proj (1536, 1536)
model.layers.9.self_attn.v_proj (256, 1536)
model.layers.10.self_attn.q_proj (1536, 1536)
model.layers.10.self_attn.v_proj (256, 1536)
model.layers.11.self_attn.q_proj (1536, 1536)
model.layers.11.self_attn.v_proj (256, 1536)
model.layers.12.self_attn.q_proj (1536, 1536)
model.layers.12.self_attn.v_proj (256, 1536)
model.layers.13.self_attn.q_proj (1536, 1536)
model.layers.13.self_attn.v_proj (256, 1536)
model.layers.14.self_attn.q_proj (1536, 1536)
model.layers.14.self_attn.v_proj (256, 1536)
model.layers.15.self_attn.q_proj (1536, 1536)
model.layers.15.self_attn.v_proj (256, 1536)
model.layers.16.self_attn.q_proj (1536, 1536)
model.layers.16.self_attn.v_proj (256, 1536)
model.layers.17.self_attn.q_proj (1536, 1536)
model.layers.17.self_attn.v_proj (256, 1536)
model.layers.18.self_attn.q_proj (1536, 1536)
model.layers.18.self_attn.v_proj (256, 1536)
model.layers.19.self_attn.q_proj (1536, 1536)
model.layers.19.self_attn.v_proj (256, 1536)
model.layers.20.self_attn.q_proj (1536, 1536)
model.layers.20.self_attn.v_proj (256, 1536)
model.layers.21.self_attn.q_proj (1536, 1536)
model.layers.21.self_attn.v_proj (256, 1536)
model.layers.22.self_attn.q_proj (1536, 1536)
model.layers.22.self_attn.v_proj (256, 1536)
model.layers.23.self_attn.q_proj (1536, 1536)
model.layers.23.self_attn.v_proj (256, 1536)
model.layers.24.self_attn.q_proj (1536, 1536)
model.layers.24.self_attn.v_proj (256, 1536)
model.layers.25.self_attn.q_proj (1536, 1536)
model.layers.25.self_attn.v_proj (256, 1536)
model.layers.26.self_attn.q_proj (1536, 1536)
model.layers.26.self_attn.v_proj (256, 1536)
model.layers.27.self_attn.q_proj (1536, 1536)
model.layers.27.self_attn.v_proj (256, 1536)
Original evaluation loss: 4.1166
Original perplexity: 61.35

PROMPT: Predictive maintenance is
CONTINUATION: a proactive approach to equipment maintenance that aims to prevent equipment failure before it occurs. It involves using data analytics and machine learning algorithms to predict when equipment will fail based on its performance and usage patterns. Predictive maintenance can help organizations

PROMPT: When bearing temperature increases,
CONTINUATION: the viscosity of the oil ____.
A. Increases
B. Decreases
C. Remains unchanged
D. Is uncertain
Answer:
B

The main reason for the increase in the temperature of the oil in the

PROMPT: Vibration monitoring helps engineers
CONTINUATION: to identify and prevent equipment failures. It is a critical part of the maintenance process, and it can help to reduce downtime and increase productivity. Vibration monitoring is a process of measuring the vibration of a machine or system. It
trainable params: 1,089,536 || all params: 1,544,803,840 || trainable%: 0.0705
print_trainable_parameters: None
trainable params: 1,089,536 || all params: 1,544,803,840 || trainable%: 0.0705
Selected projection: base_model.model.model.layers.0.self_attn.q_proj
LoRA A shape: (8, 1536)
LoRA B shape: (1536, 8)
Parameters in A: 12288
Parameters in B: 12288
Parameters in original projection: 2359296
LoRA scaling: 2.0
Initial B magnitude: 0.0
Original loss:         4.116600
Initialized LoRA loss: 4.116600
Verified: initialized LoRA preserves the baseline.
Step 1/30 | Loss: 2.9760
Step 5/30 | Loss: 2.5280
Step 10/30 | Loss: 2.6227
Step 15/30 | Loss: 3.0067
Step 20/30 | Loss: 1.9738
Step 25/30 | Loss: 2.2981
Step 30/30 | Loss: 2.4113

LoRA training complete.

Evaluation results:
Before LoRA training | loss=4.116600 | perplexity=61.35
After LoRA training  | loss=2.703294 | perplexity=14.93
Evaluation loss reduction: 1.4133

PROMPT: Predictive maintenance is

BEFORE: a proactive approach to equipment maintenance that aims to prevent equipment failure before it occurs. It involves using data analytics and machine learning algorithms to predict when equipment will fail based on its performance and usage patterns. Predictive maintenance can help organizations

AFTER: a proactive maintenance strategy that uses equipment condition data to schedule maintenance.
======================================================================

PROMPT: When bearing temperature increases,

BEFORE: the viscosity of the oil ____.
A. Increases
B. Decreases
C. Remains unchanged
D. Is uncertain
Answer:
B

The main reason for the increase in the temperature of the oil in the

AFTER: the oil film thickness decreases, increasing friction.
======================================================================

PROMPT: Vibration monitoring helps engineers

BEFORE: to identify and prevent equipment failures. It is a critical part of the maintenance process, and it can help to reduce downtime and increase productivity. Vibration monitoring is a process of measuring the vibration of a machine or system. It

AFTER: detect changes in equipment health.
======================================================================

LoRA parameter changes:
base_model.model.model.layers.0.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00281561
base_model.model.model.layers.0.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00278917
base_model.model.model.layers.0.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00370217
base_model.model.model.layers.0.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00343703
base_model.model.model.layers.1.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00290258
base_model.model.model.layers.1.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00290704
base_model.model.model.layers.1.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00320999
base_model.model.model.layers.1.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00320214
base_model.model.model.layers.2.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00261096
base_model.model.model.layers.2.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00256778
base_model.model.model.layers.2.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00328015
base_model.model.model.layers.2.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00334652
base_model.model.model.layers.3.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00278243
base_model.model.model.layers.3.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00276712
base_model.model.model.layers.3.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00342024
base_model.model.model.layers.3.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00321817
base_model.model.model.layers.4.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00280941
base_model.model.model.layers.4.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00277620
base_model.model.model.layers.4.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00400505
base_model.model.model.layers.4.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00364324
base_model.model.model.layers.5.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00312486
base_model.model.model.layers.5.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00312249
base_model.model.model.layers.5.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00319869
base_model.model.model.layers.5.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00367418
base_model.model.model.layers.6.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00338220
base_model.model.model.layers.6.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00319402
base_model.model.model.layers.6.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00407242
base_model.model.model.layers.6.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00346548
base_model.model.model.layers.7.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00345169
base_model.model.model.layers.7.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00354305
base_model.model.model.layers.7.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00462862
base_model.model.model.layers.7.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00385014
base_model.model.model.layers.8.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00322413
base_model.model.model.layers.8.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00326635
base_model.model.model.layers.8.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00449435
base_model.model.model.layers.8.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00377220
base_model.model.model.layers.9.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00351697
base_model.model.model.layers.9.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00366122
base_model.model.model.layers.9.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00476852
base_model.model.model.layers.9.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00363188
base_model.model.model.layers.10.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00315935
base_model.model.model.layers.10.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00336770
base_model.model.model.layers.10.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00483350
base_model.model.model.layers.10.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00390501
base_model.model.model.layers.11.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00319774
base_model.model.model.layers.11.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00321004
base_model.model.model.layers.11.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00504162
base_model.model.model.layers.11.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00403214
base_model.model.model.layers.12.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00342697
base_model.model.model.layers.12.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00335667
base_model.model.model.layers.12.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00553324
base_model.model.model.layers.12.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00400096
base_model.model.model.layers.13.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00301591
base_model.model.model.layers.13.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00313343
base_model.model.model.layers.13.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00572579
base_model.model.model.layers.13.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00410136
base_model.model.model.layers.14.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00349374
base_model.model.model.layers.14.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00332712
base_model.model.model.layers.14.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00694894
base_model.model.model.layers.14.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00432598
base_model.model.model.layers.15.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00325619
base_model.model.model.layers.15.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00339729
base_model.model.model.layers.15.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00529803
base_model.model.model.layers.15.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00440878
base_model.model.model.layers.16.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00360583
base_model.model.model.layers.16.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00353585
base_model.model.model.layers.16.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00618216
base_model.model.model.layers.16.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00424807
base_model.model.model.layers.17.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00537247
base_model.model.model.layers.17.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00476086
base_model.model.model.layers.17.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00668777
base_model.model.model.layers.17.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00514688
base_model.model.model.layers.18.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00390010
base_model.model.model.layers.18.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00366761
base_model.model.model.layers.18.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00565109
base_model.model.model.layers.18.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00482681
base_model.model.model.layers.19.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00435652
base_model.model.model.layers.19.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00425227
base_model.model.model.layers.19.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00666830
base_model.model.model.layers.19.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00563287
base_model.model.model.layers.20.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00313067
base_model.model.model.layers.20.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00330761
base_model.model.model.layers.20.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00536992
base_model.model.model.layers.20.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00400661
base_model.model.model.layers.21.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00348402
base_model.model.model.layers.21.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00354799
base_model.model.model.layers.21.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00637032
base_model.model.model.layers.21.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00418566
base_model.model.model.layers.22.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00389913
base_model.model.model.layers.22.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00390395
base_model.model.model.layers.22.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00588458
base_model.model.model.layers.22.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00419528
base_model.model.model.layers.23.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00353645
base_model.model.model.layers.23.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00339705
base_model.model.model.layers.23.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00738056
base_model.model.model.layers.23.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00517448
base_model.model.model.layers.24.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00394260
base_model.model.model.layers.24.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00379816
base_model.model.model.layers.24.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00699856
base_model.model.model.layers.24.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00492331
base_model.model.model.layers.25.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00564956
base_model.model.model.layers.25.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00447463
base_model.model.model.layers.25.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00703822
base_model.model.model.layers.25.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00618025
base_model.model.model.layers.26.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00436621
base_model.model.model.layers.26.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00368365
base_model.model.model.layers.26.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00679216
base_model.model.model.layers.26.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00429618
base_model.model.model.layers.27.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00436414
base_model.model.model.layers.27.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00352745
base_model.model.model.layers.27.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00505168
base_model.model.model.layers.27.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00398927
Changed frozen tensors: 0
Verified: LoRA parameters changed; original parameters stayed identical.

Process finished with exit code 0

---
TRAINING_STEPS = 60

/home/ravin/anaconda3/envs/aicondaenv/bin/python /home/ravin/aidev/aiml/assignments/10-19102026-LoRA/lora-ai.py 
Device: cuda
GPU: NVIDIA GeForce RTX 5090 Laptop GPU
LoRA rank: 8
LoRA alpha: 16
Scaling factor: 2.0
Training examples: 12
Evaluation examples: 4
Loading weights: 100%|██████████| 338/338 [00:00<00:00, 15570.46it/s]
Model loaded.

Attention projections selected for LoRA:
model.layers.0.self_attn.q_proj (1536, 1536)
model.layers.0.self_attn.v_proj (256, 1536)
model.layers.1.self_attn.q_proj (1536, 1536)
model.layers.1.self_attn.v_proj (256, 1536)
model.layers.2.self_attn.q_proj (1536, 1536)
model.layers.2.self_attn.v_proj (256, 1536)
model.layers.3.self_attn.q_proj (1536, 1536)
model.layers.3.self_attn.v_proj (256, 1536)
model.layers.4.self_attn.q_proj (1536, 1536)
model.layers.4.self_attn.v_proj (256, 1536)
model.layers.5.self_attn.q_proj (1536, 1536)
model.layers.5.self_attn.v_proj (256, 1536)
model.layers.6.self_attn.q_proj (1536, 1536)
model.layers.6.self_attn.v_proj (256, 1536)
model.layers.7.self_attn.q_proj (1536, 1536)
model.layers.7.self_attn.v_proj (256, 1536)
model.layers.8.self_attn.q_proj (1536, 1536)
model.layers.8.self_attn.v_proj (256, 1536)
model.layers.9.self_attn.q_proj (1536, 1536)
model.layers.9.self_attn.v_proj (256, 1536)
model.layers.10.self_attn.q_proj (1536, 1536)
model.layers.10.self_attn.v_proj (256, 1536)
model.layers.11.self_attn.q_proj (1536, 1536)
model.layers.11.self_attn.v_proj (256, 1536)
model.layers.12.self_attn.q_proj (1536, 1536)
model.layers.12.self_attn.v_proj (256, 1536)
model.layers.13.self_attn.q_proj (1536, 1536)
model.layers.13.self_attn.v_proj (256, 1536)
model.layers.14.self_attn.q_proj (1536, 1536)
model.layers.14.self_attn.v_proj (256, 1536)
model.layers.15.self_attn.q_proj (1536, 1536)
model.layers.15.self_attn.v_proj (256, 1536)
model.layers.16.self_attn.q_proj (1536, 1536)
model.layers.16.self_attn.v_proj (256, 1536)
model.layers.17.self_attn.q_proj (1536, 1536)
model.layers.17.self_attn.v_proj (256, 1536)
model.layers.18.self_attn.q_proj (1536, 1536)
model.layers.18.self_attn.v_proj (256, 1536)
model.layers.19.self_attn.q_proj (1536, 1536)
model.layers.19.self_attn.v_proj (256, 1536)
model.layers.20.self_attn.q_proj (1536, 1536)
model.layers.20.self_attn.v_proj (256, 1536)
model.layers.21.self_attn.q_proj (1536, 1536)
model.layers.21.self_attn.v_proj (256, 1536)
model.layers.22.self_attn.q_proj (1536, 1536)
model.layers.22.self_attn.v_proj (256, 1536)
model.layers.23.self_attn.q_proj (1536, 1536)
model.layers.23.self_attn.v_proj (256, 1536)
model.layers.24.self_attn.q_proj (1536, 1536)
model.layers.24.self_attn.v_proj (256, 1536)
model.layers.25.self_attn.q_proj (1536, 1536)
model.layers.25.self_attn.v_proj (256, 1536)
model.layers.26.self_attn.q_proj (1536, 1536)
model.layers.26.self_attn.v_proj (256, 1536)
model.layers.27.self_attn.q_proj (1536, 1536)
model.layers.27.self_attn.v_proj (256, 1536)
Original evaluation loss: 4.1166
Original perplexity: 61.35

PROMPT: Predictive maintenance is
CONTINUATION: a proactive approach to equipment maintenance that aims to prevent equipment failure before it occurs. It involves using data analytics and machine learning algorithms to predict when equipment will fail based on its performance and usage patterns. Predictive maintenance can help organizations

PROMPT: When bearing temperature increases,
CONTINUATION: the viscosity of the oil ____.
A. Increases
B. Decreases
C. Remains unchanged
D. Is uncertain
Answer:
B

The main reason for the increase in the temperature of the oil in the

PROMPT: Vibration monitoring helps engineers
CONTINUATION: to identify and prevent equipment failures. It is a critical part of the maintenance process, and it can help to reduce downtime and increase productivity. Vibration monitoring is a process of measuring the vibration of a machine or system. It
trainable params: 1,089,536 || all params: 1,544,803,840 || trainable%: 0.0705
print_trainable_parameters: None
trainable params: 1,089,536 || all params: 1,544,803,840 || trainable%: 0.0705
Selected projection: base_model.model.model.layers.0.self_attn.q_proj
LoRA A shape: (8, 1536)
LoRA B shape: (1536, 8)
Parameters in A: 12288
Parameters in B: 12288
Parameters in original projection: 2359296
LoRA scaling: 2.0
Initial B magnitude: 0.0
Original loss:         4.116600
Initialized LoRA loss: 4.116600
Verified: initialized LoRA preserves the baseline.
Step 1/60 | Loss: 2.9760
Step 5/60 | Loss: 2.5280
Step 10/60 | Loss: 2.6227
Step 15/60 | Loss: 3.0067
Step 20/60 | Loss: 1.9738
Step 25/60 | Loss: 2.2981
Step 30/60 | Loss: 2.4113
Step 35/60 | Loss: 2.7571
Step 40/60 | Loss: 2.0349
Step 45/60 | Loss: 1.0846
Step 50/60 | Loss: 0.6098
Step 55/60 | Loss: 0.5435
Step 60/60 | Loss: 0.4548

LoRA training complete.

Evaluation results:
Before LoRA training | loss=4.116600 | perplexity=61.35
After LoRA training  | loss=3.793437 | perplexity=44.41
Evaluation loss reduction: 0.3232

PROMPT: Predictive maintenance is

BEFORE: a proactive approach to equipment maintenance that aims to prevent equipment failure before it occurs. It involves using data analytics and machine learning algorithms to predict when equipment will fail based on its performance and usage patterns. Predictive maintenance can help organizations

AFTER: a planned maintenance strategy that uses equipment condition data to plan maintenance before a failure occurs.
======================================================================

PROMPT: When bearing temperature increases,

BEFORE: the viscosity of the oil ____.
A. Increases
B. Decreases
C. Remains unchanged
D. Is uncertain
Answer:
B

The main reason for the increase in the temperature of the oil in the

AFTER: additional lubrication can help keep the bearing in a more normal operating range.
======================================================================

PROMPT: Vibration monitoring helps engineers

BEFORE: to identify and prevent equipment failures. It is a critical part of the maintenance process, and it can help to reduce downtime and increase productivity. Vibration monitoring is a process of measuring the vibration of a machine or system. It

AFTER: identify changes in the condition of rotating equipment.
======================================================================

LoRA parameter changes:
base_model.model.model.layers.0.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00357871
base_model.model.model.layers.0.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00355792
base_model.model.model.layers.0.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00541016
base_model.model.model.layers.0.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00457740
base_model.model.model.layers.1.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00377741
base_model.model.model.layers.1.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00359589
base_model.model.model.layers.1.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00470209
base_model.model.model.layers.1.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00436235
base_model.model.model.layers.2.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00365193
base_model.model.model.layers.2.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00325169
base_model.model.model.layers.2.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00372909
base_model.model.model.layers.2.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00393832
base_model.model.model.layers.3.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00380351
base_model.model.model.layers.3.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00340127
base_model.model.model.layers.3.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00399232
base_model.model.model.layers.3.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00384116
base_model.model.model.layers.4.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00419159
base_model.model.model.layers.4.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00358595
base_model.model.model.layers.4.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00498561
base_model.model.model.layers.4.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00463086
base_model.model.model.layers.5.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00420720
base_model.model.model.layers.5.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00405666
base_model.model.model.layers.5.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00389883
base_model.model.model.layers.5.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00451954
base_model.model.model.layers.6.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00474322
base_model.model.model.layers.6.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00452726
base_model.model.model.layers.6.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00593530
base_model.model.model.layers.6.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00478777
base_model.model.model.layers.7.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00491091
base_model.model.model.layers.7.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00481630
base_model.model.model.layers.7.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00606368
base_model.model.model.layers.7.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00495511
base_model.model.model.layers.8.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00508940
base_model.model.model.layers.8.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00458233
base_model.model.model.layers.8.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00669624
base_model.model.model.layers.8.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00516106
base_model.model.model.layers.9.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00500169
base_model.model.model.layers.9.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00489984
base_model.model.model.layers.9.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00712871
base_model.model.model.layers.9.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00500354
base_model.model.model.layers.10.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00467556
base_model.model.model.layers.10.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00466415
base_model.model.model.layers.10.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00695850
base_model.model.model.layers.10.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00532572
base_model.model.model.layers.11.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00443081
base_model.model.model.layers.11.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00415381
base_model.model.model.layers.11.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00793220
base_model.model.model.layers.11.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00567251
base_model.model.model.layers.12.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00582653
base_model.model.model.layers.12.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00526082
base_model.model.model.layers.12.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00767549
base_model.model.model.layers.12.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00529875
base_model.model.model.layers.13.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00522951
base_model.model.model.layers.13.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00476712
base_model.model.model.layers.13.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00754930
base_model.model.model.layers.13.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00536771
base_model.model.model.layers.14.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00497088
base_model.model.model.layers.14.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00430103
base_model.model.model.layers.14.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.01049956
base_model.model.model.layers.14.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00589719
base_model.model.model.layers.15.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00462666
base_model.model.model.layers.15.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00453132
base_model.model.model.layers.15.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00728070
base_model.model.model.layers.15.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00575540
base_model.model.model.layers.16.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00487553
base_model.model.model.layers.16.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00457701
base_model.model.model.layers.16.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00889967
base_model.model.model.layers.16.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00576905
base_model.model.model.layers.17.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00680834
base_model.model.model.layers.17.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00595593
base_model.model.model.layers.17.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00923200
base_model.model.model.layers.17.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00663953
base_model.model.model.layers.18.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00553714
base_model.model.model.layers.18.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00496893
base_model.model.model.layers.18.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00817313
base_model.model.model.layers.18.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00641360
base_model.model.model.layers.19.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00532314
base_model.model.model.layers.19.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00540943
base_model.model.model.layers.19.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00865631
base_model.model.model.layers.19.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00705086
base_model.model.model.layers.20.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00515990
base_model.model.model.layers.20.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00509148
base_model.model.model.layers.20.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00887637
base_model.model.model.layers.20.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00602041
base_model.model.model.layers.21.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00527212
base_model.model.model.layers.21.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00518497
base_model.model.model.layers.21.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00818627
base_model.model.model.layers.21.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00560848
base_model.model.model.layers.22.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00594371
base_model.model.model.layers.22.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00557048
base_model.model.model.layers.22.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00959636
base_model.model.model.layers.22.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00628619
base_model.model.model.layers.23.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00560991
base_model.model.model.layers.23.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00517235
base_model.model.model.layers.23.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.01072103
base_model.model.model.layers.23.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00691871
base_model.model.model.layers.24.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00627732
base_model.model.model.layers.24.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00544866
base_model.model.model.layers.24.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.01057538
base_model.model.model.layers.24.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00679808
base_model.model.model.layers.25.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00818769
base_model.model.model.layers.25.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00664813
base_model.model.model.layers.25.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00917817
base_model.model.model.layers.25.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00791868
base_model.model.model.layers.26.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00625176
base_model.model.model.layers.26.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00505619
base_model.model.model.layers.26.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.01171130
base_model.model.model.layers.26.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00655372
base_model.model.model.layers.27.self_attn.q_proj.lora_A.default.weight: changed=True, mean absolute change=0.00731579
base_model.model.model.layers.27.self_attn.q_proj.lora_B.default.weight: changed=True, mean absolute change=0.00528180
base_model.model.model.layers.27.self_attn.v_proj.lora_A.default.weight: changed=True, mean absolute change=0.00900945
base_model.model.model.layers.27.self_attn.v_proj.lora_B.default.weight: changed=True, mean absolute change=0.00625691
Changed frozen tensors: 0
Verified: LoRA parameters changed; original parameters stayed identical.

Process finished with exit code 0
