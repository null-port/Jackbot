# 🤖 JackBot — The World's Funniest AI Model

JackBot is a fine-tuned language model trained to play **Quiplash**, the comedy-based party game by Jackbox Games. It was designed with one mission: **win a game against my real world friends**.

👉 [Watch the video here](https://youtu.be/ksJESDxkaCg)  
(*Warning: Contains crass humor — not safe for all audiences*)

---

## Disclaimer

JackBot was trained on jokes and Quiplash responses that often lean toward the **inappropriate and absurd**. Use it responsibly and don't let it loose at your next office party.

---

## What is JackBot?

- A **large language model trained on 500 of my own Quiplash responses**.
- Fine-tuned the trained on the [Mistral-7B-Instruct Model](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) using **[Unsloth](https://github.com/unslothai/unsloth)** for quick and efficient training.
- Designed to generate funny (and wildly inappropriate) answers to Quiplash prompts.

---


## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install huggingface_hub
pip install llama_cpp
```

### 2. Run Inference

#### Option A: Run via HuggingFace  

```bash
python run_inference_huggingface.py
```

#### Option B: Run Locally  

If you've downloaded the model files, modify the path on line 3 in run_inference_locally.py and use
```bash
python run_inference_locally.py
```

---

## 📦 Resources

- 🤖 **Download the model itself on HuggingFace**: [nullport/JackBot](https://huggingface.co/nullport/JackBot)  
- 📊 **Training Dataset**: [nullport/QuiplashAnswers](https://huggingface.co/datasets/nullport/QuiplashAnswers)
