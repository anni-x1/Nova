import os
from dotenv import load_dotenv
from openai import OpenAI
import pyautogui
import time

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Writer function for generating and typing content
def writer(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "developer",
                "content": "You are a function that takes a topic as input and outputs plain, concise, and practical text. Generate exactly what is needed for the given topic—nothing more, nothing less. Avoid unnecessary embellishments or flowery language. The content should be to the point and contextually appropriate. Do not markdown your responses."
            },
            {"role": "user", "content": user_input}
        ]
    )
    content = response.choices[0].message.content

    # Type out the generated content
    print("Moving to typing area in 3 seconds... Place your cursor where you want the text to be typed.")
    time.sleep(3)

    # Set up PyAutoGUI for safe typing
    pyautogui.FAILSAFE = True

    # Introduce faster dynamic speed variation
    # for char in content:
        # pyautogui.write(char)
        # time.sleep(0.000001)  # Slightly faster variation
    pyautogui.write(content, interval=0.000001)  # No delay between keystrokes
    # print(content)
    ret = "I have successfully typed " + user_input
    return ret