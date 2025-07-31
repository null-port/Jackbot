## Imports
from huggingface_hub import hf_hub_download
from llama_cpp import Llama

## Define model name and file name
model_name = "nullport/JackBot"
model_file = "unsloth.Q4_K_M.gguf"

## Download the model
model_path = hf_hub_download(model_name, filename=model_file)

model_kwargs = {
  "n_ctx":4096,    # Context length to use
  "n_threads":4,   # Number of CPU threads to use
  "n_gpu_layers":32, # Number of model layers to offload to GPU. Set to 0 if only using CPU
  "verbose":False
}

## Instantiate model from downloaded file
llm = Llama(model_path=model_path, **model_kwargs)

## Generation kwargs
generation_kwargs = {
    "max_tokens":200, # Max number of new tokens to generate
    "stop":["<|endoftext|>", "</s>"], # Text sequences to stop generation on
    "echo":False, # Echo the prompt in the output
    "temperature": 0.9,
    "top_k": 100 # Set this value > 1 for sampling decoding
}

# JackBox question to Ask
question = ""

## Run inference

prompt = f"Instruction: You are Jack_Bot, an incredibly funny chatbot designed to always win at the online game 'Quiplash'. The user will present you with a prompt and your goal is to answer it in the most hilarious way possible. Your answer will be pitted against another user's answer, and the audience will determine whose response to the prompt is funnier, so making people laugh is an important part of your job. No topic is off-limits, meaning you should feel free to be as crass and toe the line of what is acceptable to say. Swearing is fine (and even encouraged). Misspelling words also adds to the comedy, so use that when appropriate. Think in the style of 'Cards Against Humanity'. Feel free to use topical references or jokes involving internet culture, well-understood humor, politics, and religion. Remember, your goal is make people laugh!\nInput: {question}\nOutput:"

print(f"\n\nQuiplash Prompt: {question}\n\nJackBot's Response: ", end="")

res = llm(prompt, **generation_kwargs) # Res is a dictionary

## Unpack and the generated text from the LLM response dictionary and print it

print(f"{res['choices'][0]['text']}\n\n")
