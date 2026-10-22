import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.responses.create(
    input="What is CS50x?",
    model="gpt-4o-mini"
)

print(response.output_text)
