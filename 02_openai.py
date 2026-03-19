from openai import OpenAI

# pip install openai
# if you save the key under a different enviroment variable name, you can do something like:
client = OpenAI(
  api_key="", # Enter Api key please

)

command = '''






















'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named sahil who speaks marathi as well as english. He is from India and is a coder. You analyze chat history and respond like Sahil."},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)
