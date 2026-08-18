
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

print("Welcome to NOVAXPT AI")
print("Your AI assistant is connected to OpenAI.")

response = client.responses.create(
    model="gpt-5.6",
    input="Hello NOVAXPT. Introduce yourself in one short sentence."
)

print(response.output_text)
