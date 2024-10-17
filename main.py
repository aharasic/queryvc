import streamlit as st
from dotenv import load_dotenv
import os
from convert_to_sql import convert_natural_to_sql
from get_column_info import get_column_info
from query_database import execute_sql_query
from json_to_text import analyze_json_with_llm

load_dotenv()

# Configuración de Streamlit
def main():
    st.set_page_config("Query VC", initial_sidebar_state="collapsed")
    st.title("Query VC")
            
    csv_file = "csv/crunchbase.csv"

    with st.sidebar:
        
        f_options = [
            {"label": "Amazon Bedrock", "value": "bedrock"}
            #{"label": "Ollama", "value": "ollama"},
            #{"label": "OpenAI", "value": "openai"}
        ]

        select_framework = st.selectbox("Select a Framework:", [option["label"] for option in f_options], index=0)
        framework = next((option["value"] for option in f_options if option["label"] == select_framework), None)
        #st.write("Framework ID: ", framework)

        if framework == 'ollama':
            local_options = [
                {"label": "Llama 3", "value": "llama3"},
                {"label": "Llama 3.2", "value": "llama3.2"}
            ]

            selected_model = st.radio("Select a Model:", [option["label"] for option in local_options], index=1)
            model = next((option["value"] for option in local_options if option["label"] == selected_model), None)
        
        elif framework == 'bedrock': 
            bedrock_options = [
                {"label": "Claude 3", "value": "claude_3"},
                {"label": "Claude 3.5", "value": "claude_35"}
            ]

            selected_model = st.radio("Select a Model:", [option["label"] for option in bedrock_options], index=1)
            model = next((option["value"] for option in bedrock_options if option["label"] == selected_model), None)

        elif framework == 'openai':
            openai_options = [
                {"label": "GPT-4o", "value": "gpt_4o"}
            ]

            selected_model = st.radio("Select a Model:", [option["label"] for option in openai_options], index=0)
            model = next((option["value"] for option in openai_options if option["label"] == selected_model), None)

        #st.write("Model ID: ", model)

    prompt = st.text_input("Question: ", placeholder="Enter your question here...")
    execute_button = st.button("Execute", type="primary")

    if prompt or execute_button:
        with st.spinner('Retrieving Fields information...'):
            #Get Column Info
            columns, data_types, columns_and_types = get_column_info()
        with st.spinner('Converting Question to SQL format...'):
            # Convertir pregunta en SQL
            sql_query = convert_natural_to_sql(prompt, columns, columns_and_types, csv_file, framework, model)
        with st.spinner('Running the SQL Query...'):
            print("Ejecutar la consulta SQL")
            json_result = execute_sql_query(sql_query, columns, data_types, csv_file)
        with st.spinner('Creating Report...'):
            print("Convertir el resultado JSON en texto natural")
            response = analyze_json_with_llm(prompt, json_result, framework, model)

        st.markdown(f"**Answer:** {response}", unsafe_allow_html=True)

if __name__ == "__main__":
    main()