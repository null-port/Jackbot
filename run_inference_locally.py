from llama_cpp import Llama

model_path = "" # Path to desired model

model_kwargs = {
    "n_ctx": 8192, # Context length to use
    "n_threads": 4, # Number of CPU threads to use
    "n_gpu_layers": 32, # Number of model layers to offload to GPU. Set to 0 if only using CPU
    "verbose": False
}
llm = Llama(model_path=model_path, **model_kwargs)

generation_kwargs = {
    "max_tokens": 150, # Max number of new tokens to generate
    "stop": ["<|endoftext|>", "</s>"], # Text sequences to stop generation on
    "echo": False, # Echo the prompt in the output
    "temperature": 1.2,
    "top_k": 100 # Set this value > 1 for sampling decoding
}

def generate_response(instruction, user_input):
    prompt = (
        f"Instruction: {instruction}\n"
        f"Input: {user_input}\n"
        f"Output:"
    )
    res = llm(prompt, **generation_kwargs)
    return res['choices'][0]['text'].strip()


def main():
    instruction = "You are Jack_Bot, an incredibly funny chatbot designed to always win at the online game 'Quiplash'. The user will present you with a prompt and your goal is to answer it in the most hilarious way possible. Your answer will be pitted against another user's answer, and the audience will determine whose response to the prompt is funnier, so making people laugh is an important part of your job. No topic is off-limits, meaning you should feel free to be as crass and toe the line of what is acceptable to say. Swearing is fine (and even encouraged). Misspelling words also adds to the comedy, so use that when appropriate. Think in the style of 'Cards Against Humanity'. Feel free to use topical references or jokes involving internet culture, well-understood humor, politics, and religion. Remember, your goal is make people laugh!",
    user_input = ""
    # Generates 20 potential JackBot answers
    for i in range(20):
        output = generate_response(instruction, user_input)
        print(f"Run {i+1}: {output}")

if __name__ == "__main__":
    main()