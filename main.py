import streamlit as st
#import css.stylers
from convert_to_sql import convert_natural_to_sql
from get_column_info import get_column_info
from query_database import execute_sql_query
from json_to_text import analyze_json_with_llm
import logging

logging.basicConfig(level=logging.ERROR)

# Configuración de Streamlit
def main():
    st.set_page_config(page_title="Mika Analyst")#,
                    #initial_sidebar_state="collapsed")
    st.title("Mika Analyst")
            
    csv_file = "csv/crunchbase.csv"

    with st.sidebar:
        
        f_options = [
            {"label": "Amazon Bedrock", "value": "bedrock"},
            {"label": "Ollama", "value": "ollama"},
            {"label": "OpenAI", "value": "openai"}
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
    
    with st.expander("What can I ask?"):
        st.write('''
            - Which countries raised the most money in 2024? Provide the top 10.
            - Which startups raised the highest amount of money in 2023? List the top 10 along with detailed information about each.
            - What is the growth in funds raised in Latin America during Q1 2024 compared to Q1 2023?
            - List the newly funded Startups in Chile? (i.e. received funding in the last 3 months)
        ''')
    
    st.info("This App is meant as a Proof-of-Concept. The dataset is not fully cleaned so don't use it to make business decisions.")
    prompt = st.text_input("", placeholder="Ask me anything on VCs and Startups...")
    execute_button = st.button("Go", type="primary")

    if prompt or execute_button:
        try:
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
                response = response.replace("$", r"\$")
                st.markdown(f"**Answer:** {response}", unsafe_allow_html=True)
                with st.expander("Step-by-step:"):
                    st.markdown("1. The question is initially converted from natural language to SQL")
                    st.markdown(f"**Question:** {prompt}")
                    st.markdown(f"SQL Query:")
                    st.code(f"{sql_query}")
                    st.markdown("2. The query is sent to the database, which returns a response in JSON format.")
                    st.markdown("JSON:")
                    st.json(json_result)
                    st.markdown("3. Finally, the JSON is passed to the LLM to generate a response.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            st.error("There has been an error. Try again or rephrase the question.")
        
    # Add a footer using HTML and CSS
    st.markdown("""
    <div class="footer-note">
        <p>Created by Alex Harasic @harasic</p>
    </div>
    """, unsafe_allow_html=True)

    # Import custom CSS
    #css.stylers.css('footer.css')
    
if __name__ == "__main__":
    main()