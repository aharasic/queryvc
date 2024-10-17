import boto3

# Initialize the SageMaker client
sagemaker_client = boto3.client('sagemaker', region_name='us-east-1')  # Replace with your region

# Specify the endpoint name
endpoint_name = 'jumpstart-dft-meta-textgeneration-l-20241017-183205'  # Replace with the actual name of your endpoint

# Delete the endpoint
sagemaker_client.delete_endpoint(EndpointName=endpoint_name)
print(f"Endpoint '{endpoint_name}' deleted successfully.")
