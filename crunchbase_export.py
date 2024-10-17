import requests
import pandas as pd
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("CRUNCHBASE_API_KEY")
BASE_URL = 'https://api.crunchbase.com/api/v4/searches/organizations'
headers = {'User-Agent': 'Mozilla/5.0'}

# Define the search filters for your query
search_body = {
    "field_ids": [
        "name", "categories", "location_identifiers", "short_description", "last_funding_at", 
        "num_funding_rounds", "last_funding_type", "ipo_status", "investor_names"
    ],
    "query": [
        {
            "type": "predicate",
            "field_id": "location_identifiers",
            "operator_id": "includes",
            "values": ["Chile", "Argentina"]  # Replace country code with country names
        },
        {
            "type": "predicate",
            "field_id": "last_funding_at",
            "operator_id": "gte",
            "values": ["2022-01-01"]  # Funding date 2022 and later
        }
    ],
    "limit": 100  # Adjust limit based on how many results you want
}

# Make API request
headers = {'Content-Type': 'application/json'}
response = requests.post(f'{BASE_URL}?user_key={API_KEY}', json=search_body, headers=headers)

# Check for successful response
if response.status_code == 200:
    data = response.json()
    organizations = data.get('entities', [])

    # Convert JSON data to pandas DataFrame
    df = pd.json_normalize(organizations)

    # Filter out the required columns
    df_filtered = df[
        ['properties.name', 'properties.categories', 'properties.location_identifiers', 'properties.short_description',
         'properties.last_funding_at', 'properties.num_funding_rounds', 
         'properties.last_funding_type', 'properties.ipo_status', 'properties.investor_names']
    ]

    # Rename columns
    df_filtered.columns = [
        'StartupName', 'Industries', 'HeadquartersLocation', 'Description', 'LastFundingDate',
        'NumberofFundingRounds', 'LastFundingType', 'IPOStatus', 'Top5Investors'
    ]

    # Save to CSV
    df_filtered.to_csv('filtered_startups.csv', index=False)
    print("Data saved to filtered_startups.csv")
else:
    print(f"Failed to fetch data: {response.status_code}, {response.text}")