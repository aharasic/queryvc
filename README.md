<<<<<<< HEAD
# queryvc
=======

# Query VC

**Query VC** is a Streamlit-based application that allows users to interact with a Crunchbase Startups Investments dataset. Users can ask questions in natural language, which are then converted into SQL queries to retrieve relevant data from the dataset. The results are processed and returned in a readable format.

## Features

- **Natural Language to SQL Conversion**: Convert user questions into SQL queries.
- **Crunchbase Data Analysis**: Interact with Crunchbase startup investment data.
- **Flexible Framework and Model Selection**: Choose from different AI frameworks and models, such as Amazon Bedrock, Ollama, or OpenAI.
- **Conversational Interface**: View your conversation history with the app for easy reference.

## Requirements

To run this application, you need the following installed:

- **Python** 3.x
- **Streamlit** (`pip install streamlit`)
- **dotenv** (`pip install python-dotenv`)
- **Other required modules** (e.g., `convert_to_sql`, `get_column_info`, `query_database`, `json_to_text`) should be available in your Python environment.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aharasic/queryvc.git
   cd queryvc
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables by creating a `.env` file in the root directory. This file may include sensitive credentials or configurations necessary for the application.

## Configuration

Ensure you have a file named `crunchbase.csv` under the `csv/` directory, as this is the dataset the app will query.

### .env File

You may need a `.env` file in the root directory to store API keys or other configuration details. This application loads environment variables with the `dotenv` package.

## Usage

1. Run the Streamlit app from the command line:

   ```bash
   streamlit run main.py
   ```

2. Open your web browser and navigate to the local server URL provided by Streamlit, typically [http://localhost:8501](http://localhost:8501).

3. Use the app's interface to:
   - Choose an AI framework and model from the sidebar.
   - Enter questions about Crunchbase startup investments.
   - View the SQL query generated and the results of the query.

## Application Flow

1. **Framework and Model Selection**: Choose from frameworks such as Amazon Bedrock. Available models vary by framework (e.g., Claude 3, Claude 3.5, GPT-4o).
   
2. **Input Question**: Enter your question in natural language. The app will retrieve table structure details, convert the question into an SQL query, and execute it.
   
3. **View Results**: The app returns a natural language response based on the SQL query results, leveraging LLMs to analyze the output.

## File Structure

- **main.py**: The main file for running the Streamlit app.
- **convert_to_sql.py**: Module for converting natural language questions into SQL queries.
- **get_column_info.py**: Module for retrieving column information from the dataset.
- **query_database.py**: Module for executing SQL queries on the dataset.
- **json_to_text.py**: Module for analyzing JSON results and converting them into natural language text.

## Additional Notes

- Ensure the dataset (`crunchbase.csv`) is up-to-date and located in the `csv/` folder.
- Make sure all required modules are installed and accessible within your Python environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy exploring Crunchbase data with Query VC!
>>>>>>> cd12058 (Initial commit)
