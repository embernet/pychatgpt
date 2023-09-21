import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

system_prompt = """You are an expert advisor.
You provide advice with explanations, history,
related topics, and examples"""

message = """How can I use generative AI?"""

print("Testing OpenAI API...")
print(f"system_prompt: {system_prompt}")
print(f"message: {message}")
print("Calling API...")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
        {
            "role": "system",
            "content": system_prompt},
       {"role": "user", "content": message}
    ],
)

output = response.choices[0]["message"]["content"]
print(f"response:\n{output}")

