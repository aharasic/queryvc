import boto3
from dotenv import load_dotenv
import json

load_dotenv()

region = 'us-east-1'

# Initialize the SageMaker runtime client
sagemaker_runtime_client = boto3.client('sagemaker-runtime', region_name=region)  # Replace with your region

# Define the endpoint name
endpoint_name = 'jumpstart-dft-meta-textgeneration-l-20241017-183205'

# Define your prompt
prompt_text = """
Convert the following question to an SQL query based on the table structure. The output should not have any markdown format like ```sql:

Table: users
Columns:
  - user_id (INTEGER)
  - signup_date (DATE)
  - email (VARCHAR)
  - status (VARCHAR)
  - age (INTEGER)

Question: How many users signed up in the last month?

SQL Query:
"""

# Send the request to the SageMaker endpoint with plain text headers
response = sagemaker_runtime_client.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType="text/plain",
    Accept="text/plain",
    Body=prompt_text
)

# Read and print the response directly as plain text
response_body = response['Body'].read().decode('utf-8')

# If the output is JSON-formatted, parse it and extract the plain text
response_data = json.loads(response_body)

# Assume the text output is in a field called 'generated_text'
# You may need to replace 'generated_text' with the actual key used in the response JSON
plain_text_output = response_data.get('generated_text', response_data)
plain_sql = plain_text_output.replace("```sql", "").replace("```", "").strip()

print(plain_sql)