import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=api_key)

response = client.responses.create(
    input="What is CS50x?",
    model="gpt-4o-mini"
)

print(response.output_text)
