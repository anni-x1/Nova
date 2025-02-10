# Description: Main file to run the chatbot

import history_management
from chat import chat
from listen import listen
from play_audio import eff
from voice_activation import wake
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def astra():
    print("✨ Welcome to Astra: Your Intelligent Chat Assistant! ✨")
    print(
        "Astra is here to assist you with conversations and even auto-type your responses with precision. 🚀"
    )
    print(
        "💡 Pro Tip: When using the writer function, ensure your cursor is placed where you want the text to appear."
    )
    history_management.load_history()  # Load history on startup
    while True:
        user_input = listen() # for voice input
        # user_input = input("You: ")  # for manual input
        print("You: ", user_input)
        if user_input.lower() == "exit":
            eff("./sound_effects/bye.wav")
            print("Goodbye! See you next time. 😊")
            break
        response = chat(user_input)
        print(f"Astra: {response}")
@app.route('/')
def index():
    return "ok"
@app.route('/wake', methods=['GET'])
def wake_endpoint():
    try:
        wake.wake()
    except KeyboardInterrupt:
        running = False
        print("Stopping wake word detection. Goodbye!")

if __name__ == "__main__":
    # app.run(debug=True)
    try:
        wake.wake()
    except KeyboardInterrupt:
        running = False
        print("Stopping wake word detection. Goodbye!")
    