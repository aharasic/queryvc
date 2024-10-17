import ollama

# Define the model ID for LLaMA-3 (replace with the exact model name if different)
def query_llama(prompt, model):
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    
    # Access the 'content' field within 'message'
    output1 = response['message']['content']
    
    return output1

def query_ollama(prompt, model):
    print("Running query_ollama function\n")
    output2 = query_llama(prompt, model)
    return output2