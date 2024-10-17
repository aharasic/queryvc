import pandas as pd
#from call_openai import query_openai
from call_ollama import query_ollama
iteration = 0

def convert_natural_to_sql(natural_query, columns, columns_and_types, csv_file, framework, model):
    print("Executing Function: convert_natural_to_sql from convert_to_sql.py")
    
    df = pd.read_csv(csv_file, skiprows=2, sep=";")
    examples = df.iloc[0:3].values.tolist()
    print("\nExamples:\n")
    print(examples)

    print("\nconvert_natural_to_sql\n")
    prompt = f"""

    You are an expert programmer that writes SQL queries. I need to query a SQL DB to find specific data.
    
    I need to answer this question: {natural_query}
    
    Table:
    - Columns types to use in the select field part of the query: {columns_and_types}
    - Columns names to use in the WHERE part of the query: {columns}
    
    Examples:
    {examples}
    
    Create and SQL Query to respond this question: {natural_query}
    
    Instructions:
    
    Step 1: Understand the data structure: {columns_and_types}
    Step 2: Think what fields you need to query to answer the question
    Step 3: THink of what conditions should be met in the WHERE To answer the question
    Step 4: Create an SQL query
    Step 5: Review one more time the SQL query to check for errors.
    
    Consider the following:
    
    **Please convert this into a valid SQL statement, taking into account the column names, data types, and the example data provided.
    The Table Name is temp_table with no quotes **

    **When you need to use the operator LIKE, always use ILIKE**
    
    **Only respond with the SQL command without any markdown ticks**
    
    **The LastFundingDate is a DATE field, so make sure to query with DATE types of conditions, never use LIKE

    **If asked for data about a specific country, then query for StartupCountry using 2-letter country code**
    
    ** Do not give explanations to the query, only respond with just the query **
    
    """
    
    sql_query = query_ollama(prompt, 'codellama')
    
    print(f"Run {iteration+1}")
    print("SQL Query2: ", sql_query)
    print("---Ended----")

    return sql_query
