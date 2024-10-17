import os
from openai import OpenAI
from dotenv import load_dotenv  # Importa la función para cargar las variables de entorno

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def query_openai(prompt, model):
    print("\nExecuting Call_OpenAI Function")
    response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )
    
    output = response.choices[0].message.content.strip()
    print("\nOutput OpenAI: ")
    print(output)

    return output
