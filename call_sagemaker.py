import boto3
import json

# Define the model ID for LLaMA-3 (replace with the exact model name if different)
def query_codellama(prompt):
    region = 'us-east-1'
    sagemaker_runtime_client = boto3.client('sagemaker-runtime', region_name=region)  # Replace with your region
    endpoint_name = 'jumpstart-dft-meta-textgeneration-l-20241017-183205'
    response = sagemaker_runtime_client.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType="text/plain",
    Accept="text/plain",
    Body=prompt)

    # Read and print the response directly as plain text
    response_body = response['Body'].read().decode('utf-8')

    # If the output is JSON-formatted, parse it and extract the plain text
    response_data = json.loads(response_body)

    # Assume the text output is in a field called 'generated_text'
    # You may need to replace 'generated_text' with the actual key used in the response JSON
    plain_text_output = response_data.get('generated_text', response_data)
    plain_sql = plain_text_output.replace("```sql", "").replace("```", "").strip()

    print("PlainSQL: \n", plain_sql)
        
    return plain_sql
    
def query_sagemaker(prompt):
    output = query_codellama(prompt)
    return output
  
