from call_openai import query_openai
from call_bedrock import query_bedrock
from call_ollama import query_ollama

def call_llm(prompt, framework, model):
    print("\nExecuting Call_LLM Function\n")
    print("With framework: ", framework)

    # Define a dictionary to map framework to the corresponding function
    framework_switch = {
        "openai": query_openai,
        "bedrock": query_bedrock,
        "ollama": query_ollama
    }
    
    # Get the function based on framework, or raise an error if not found
    try:
        framework_function = framework_switch[framework]
        output = framework_function(prompt, model)
    except KeyError:
        raise ValueError(f"Unsupported model ID: {framework}")
    
    return output
