from openai import OpenAI
client=OpenAI(api_key="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")

response=client.responses.create(
    input="What is CS50x?",
    model="gpt-4o-mini"
)

print(response.output_text)