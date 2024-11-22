import os
import boto3
import json
from dotenv import load_dotenv  # Importa la función para cargar las variables de entorno

load_dotenv()
# Initialize the Bedrock client
bedrock_client = boto3.client(
    'bedrock-runtime',
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

inference_profile_arn = "arn:aws:bedrock:us-east-2:205930639716:inference-profile/us.anthropic.claude-3-5-sonnet-20240620-v1:0"

#models
#model="anthropic.claude-3-sonnet-20240229-v1:0"
#model="anthropic.claude-3-5-sonnet-20240620-v1:0"
#model="anthropic.claude-3-haiku-20240307-v1:0"

def query_claude(prompt, model):
    print("\nExecuting Call_Claude Model: ", model)
    model="us.anthropic.claude-3-5-sonnet-20240620-v1:0"
    
    # Create the messages payload as expected by the Messages API
    messages = [
        #{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    
    payload = {
        "messages": messages,
        "max_tokens": 1000,  # Correct parameter name
        "anthropic_version": "bedrock-2023-05-31"  # Adjust as per expected format
    }
    
    response = bedrock_client.invoke_model(
        modelId=model,
        contentType="application/json",
        accept="application/json",
        body=json.dumps(payload).encode('utf-8')
    )

    response_body = json.loads(response.get("body").read().decode('utf-8'))
    output = response_body['content'][0]['text']
    print(output)

    return output

def query_bedrock(prompt, model):
    if model == 'claude_3':
        output = query_claude(prompt, 'anthropic.claude-3-sonnet-20240229-v1:0')
    elif model == 'claude_35':
        output = query_claude(prompt, 'anthropic.claude-3-5-sonnet-20240620-v1:0')
    else:
        output = query_claude(prompt, 'anthropic.claude-3-sonnet-20240229-v1:0')
    
    return output