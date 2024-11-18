from openai import OpenAI

# pip install openai
# if you save the key under a different enviroment variable name, you can do something like:
client = OpenAI(
  api_key="sk-proj--Wx17ehGk2PnwmzCHcDwT3BlbkFJMj6bYTk9jG1bqZaFTcj", # Enter Api key please

)

command = '''

[6:01 PM, 10/31/2024] Sahil: Hi
[6:01 PM, 10/31/2024] Sis: Kya
[6:01 PM, 10/31/2024] Sahil: Kahi nahi
[6:01 PM, 10/31/2024] Sis: Bye
[6:01 PM, 10/31/2024] Sahil: Bye
[6:01 PM, 10/31/2024] Sahil: Good night
[6:01 PM, 10/31/2024] Sis: Good night
[6:02 PM, 10/31/2024] Sis: What about your coding ?
[6:02 PM, 10/31/2024] Sahil: Quite good
[6:02 PM, 10/31/2024] Sis: Ok
[6:02 PM, 10/31/2024] Sahil: Bye
[6:02 PM, 10/31/2024] Sis: Bye




















'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named sahil who speaks marathi as well as english. He is from India and is a coder. You analyze chat history and respond like Sahil."},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)