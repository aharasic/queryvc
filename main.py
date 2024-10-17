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

    if "messages" not in st.session_state.keys():  # Initialize the chat messages history
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Ask me a question about Crunchbase Startups Investments!",
            }]

    # Add a sidebar
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

            # Now you can access the selected model
            model = next((option["value"] for option in local_options if option["label"] == selected_model), None)
        
        elif framework == 'bedrock': 
            bedrock_options = [
                {"label": "Claude 3", "value": "claude_3"},
                {"label": "Claude 3.5", "value": "claude_35"}
            ]

            selected_model = st.radio("Select a Model:", [option["label"] for option in bedrock_options], index=1)

            # Now you can access the selected model
            model = next((option["value"] for option in bedrock_options if option["label"] == selected_model), None)

        elif framework == 'openai':
            openai_options = [
                {"label": "GPT-4o", "value": "gpt_4o"}
            ]

            selected_model = st.radio("Select a Model:", [option["label"] for option in openai_options], index=0)

            # Now you can access the selected model
            model = next((option["value"] for option in openai_options if option["label"] == selected_model), None)

        #st.write("Model ID: ", model)

    # The rest of your app goes here
    #st.write("This is where you would add your main content.")

    if "conversation" not in st.session_state:
        st.session_state["conversation"] = []
    
    prompt = st.text_input("Question: ", placeholder="Enter your question here...")
    execute_button = st.button("Execute", type="primary")

    if prompt or execute_button:
        st.session_state["conversation"].append({"role": "user", "content": prompt})
        
        # Container to hold the streaming response
        #response_container = st.empty()
        response = ""
        
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

        # Append bot response to the conversation
        st.session_state["conversation"].append({"role": "assistant", "content": response})
    
    # Display the conversation history
    for message in st.session_state["conversation"]:
        if message["role"] == "user":
            st.markdown(f"**Question:** {message['content']}", unsafe_allow_html=False)
        else:
            st.markdown(f"**Answer:** {message['content']}", unsafe_allow_html=False)

if __name__ == "__main__":
    main()