import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
  api_key="sk-proj--Wx17ehGk2PnwmzCHcDwT3BlbkFJMj6bYTk9jG1bqZaFTcj", # Enter Api key please

)
def is_last_message_from_sender(chat_log, sender_name="Sis"):
    messages = chat_log.strip().split("\2024]n ")[-1]
    if sender_name in messages:
        return True
    return False

   

# Step 1: Click on the icon at (1123, 1159)
pyautogui.click(1123, 1159)
# Adding a delay to ensure the program has time to respond
time.sleep(1)  # Adjust as necessary

while True:
    

    # Step 2: Drag from (675, 179) to (1885, 1026) to select text
    pyautogui.moveTo(902, 248)
    pyautogui.dragTo(1027, 1103 , duration=1.0, button = 'left')  # Adjust the duration if necessary

    # Step 3: Copy selected text to clipboard
    pyautogui.hotkey('ctrl', 'c')

    # Adding a small delay to ensure the text has been copied
    time.sleep(2)
    pyautogui.click(1740, 260)


    # Step 4: Get copied text from clipboard
    chat_history = pyperclip.paste()

    print(chat_history)
    
    print(is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named sahil who speaks marathi as well as english. You are from India and is a coder. You analyze chat history and respond like Sahil. Output should be next chat repond (text messege only)"},
            {"role": "user", "content": chat_history}
        ]
        )

        reponse = completion.choices[0].message.content
        pyperclip.copy(reponse)


        # Step 5: Click at (1455, 1089) to focus the input area and paste
        pyautogui.click(1455, 1089)  # Adjust coordinates as needed
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'v')  # Paste the copied text
        time.sleep(1)

        # Step 6: Press Enter to send the message
        pyautogui.press('enter')