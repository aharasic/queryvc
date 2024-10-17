#from call_openai import query_openai
from call_ollama import query_ollama

def route_query_with_llm(query, model):
    llm_prompt = f"Classify the following question. If it is something to be search in past documents, then classify it as 'text'. If this is something that should be queried in Statistical Databases then return 'numeric': {query}. You should only reply with text or numeric and no other word."
    classification = llm.ask(llm_prompt)  # Assume llm.ask() sends the prompt and returns a response

    # Route based on LLM's classification
    if "text" in classification.lower():
        return RAG_search(query)
    elif "numeric" in classification.lower():
        return SQL_analyze(query)
    else:
        return "Unable to determine query type. Please clarify your request."

class LLM:
    def ask(self, prompt):
        #output = query_openai(prompt, model)
        output = query_ollama(prompt, model)
        return "text" if "text" in output else "numeric"

# Dummy functions for demonstration
def RAG_search(query):
    return f"Performing RAG search for: {query}"

def SQL_analyze(query):
    return f"Performing SQL analysis for: {query}"

# Example usage
#query = "What are the startups that raised the most amount of money in 2024"
query = "what was the startups with the highest investment in 2024"

#model = "gpt-4"
model = "llama3.2"

llm = LLM()  # Instantiate your LLM class
result = route_query_with_llm(query, model)
print(result)
