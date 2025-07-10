from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)