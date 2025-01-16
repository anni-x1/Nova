# Description: Main file to run the chatbot

import history_management
from chat import chat

if __name__ == "__main__":
    print("✨ Welcome to Nova: Your Intelligent Chat Assistant! ✨")
    print(
        "Nova is here to assist you with conversations and even auto-type your responses with precision. 🚀"
    )
    print(
        "💡 Pro Tip: When using the writer function, ensure your cursor is placed where you want the text to appear."
    )
    history_management.load_history()  # Load history on startup
    while True:
        # user_input = listen.listen()
        user_input = input("You: ")  # for manual input
        # print("You: ", user_input)
        if user_input.lower() == "exit":
            print("Goodbye! See you next time. 😊")
            break
        response = chat(user_input)
        print(f"Nova: {response}")