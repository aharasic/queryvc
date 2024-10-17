from call_llm import call_llm

def analyze_json_with_llm(natural_query, json_data, framework, model):
    print("Executing Function: analyze_json_with_llm from json_to_text.py")
    prompt = f"""
    I asked a question to the LLM that look like this:
    {natural_query}
    
    The system responded with these results:
    {json_data}

    Assume you are a business analyst, follow this instructions for analyze the response and give an interesting text:
    <instructions>
    - Say what the results mean when compared to the question asked
    - Dont talk about the query and don't talk about the structure of the query or the json
    - Only talk about how the data in the results respond related to the query
    - In the answer, augment the answer with the data responded in the json_data
    - Respond all in english
    - If you have country codes, convert them to the full country name without countrycodes: Example Chile
    - Bring the results formatted in Markdown
    </instructions>
    """

    query_results = call_llm(prompt, framework, model)
    
    return query_results