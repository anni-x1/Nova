import os
from dotenv import load_dotenv
import json
from openai import OpenAI
import vars
import getNews
import openCalc
import writer
import listen
import pyaudio
import base64

load_dotenv()
# File path to save conversation history
HISTORY_FILE = "conversation_history.json"

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Load conversation history from file
def load_conversation_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            vars.conversation_history = json.load(file)
            print("Conversation history loaded successfully!")
    except FileNotFoundError:
        vars.conversation_history = []
        print("No previous conversation history found. Starting fresh.")
    except json.JSONDecodeError:
        vars.conversation_history = []
        print("Corrupted history file. Starting fresh.")


# Save conversation history to file
def save_conversation_history():
    try:
        with open(HISTORY_FILE, "w") as file:
            json.dump(vars.conversation_history, file, indent=4)
    except Exception as e:
        print(f"Failed to save conversation history: {e}")


# Chat function
def chat(user_input):
    print("Processing...")
    # Append the user's input to the conversation history
    vars.conversation_history.append({"role": "user", "content": user_input})

    # Generate response from OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "sage", "format": "wav"},
        messages=vars.conversation_history,
        functions=vars.functions,
        function_call="auto",
    )

    message = response.choices[0].message
    if message.audio:
        wav_bytes = base64.b64decode(response.choices[0].message.audio.data)
        p = pyaudio.PyAudio()
        audio_stream = p.open(
            format=p.get_format_from_width(width=2),
            channels=1,
            rate=24000,  # Example rate; replace with the actual rate from the response metadata
            output=True,
        )

        # Stream the audio directly from memory
        audio_stream.write(wav_bytes)
        audio_stream.stop_stream()
        audio_stream.close()
        p.terminate()
    if hasattr(message, "function_call") and message.function_call:
        function_name = message.function_call.name
        function_args = json.loads(message.function_call.arguments)

        if function_name == "get_top_news":
            topic = function_args.get("topic")
            function_response = getNews.get_top_news(topic)
        elif function_name == "open_calculator":
            function_response = openCalc.open_calculator()
        elif function_name == "writer":
            # Handle writer function call and type out the content
            writer_input = function_args.get("user_input")
            function_response = writer.writer(writer_input)

        # Append function response to history
        vars.conversation_history.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )

        # Generate a refined response
        refined_response = client.chat.completions.create(
            model="gpt-4o-mini-audio-preview",
            modalities=["text", "audio"],
            audio={"voice": "sage", "format": "wav"},
            messages=vars.conversation_history,
        )

        # Append Astra's response to history
        final_response = refined_response.choices[0].message.audio.transcript
        vars.conversation_history.append(
            {"role": "assistant", "content": final_response}
        )
        save_conversation_history()  # Save updated history
        wav_bytes = base64.b64decode(refined_response.choices[0].message.audio.data)
        p = pyaudio.PyAudio()
        audio_stream = p.open(
            format=p.get_format_from_width(width=2),
            channels=1,
            rate=24000,  # Example rate; replace with the actual rate from the response metadata
            output=True,
        )

        # Stream the audio directly from memory
        audio_stream.write(wav_bytes)
        audio_stream.stop_stream()
        audio_stream.close()
        p.terminate()
        return final_response

    save_conversation_history()  # Save updated history
    # Append Astra's direct response to history
    vars.conversation_history.append(
        {"role": "assistant", "content": message.audio.transcript}
    )
    return message.audio.transcript


if __name__ == "__main__":
    print("✨ Welcome to Nova: Your Intelligent Chat Assistant! ✨")
    print(
        "Nova is here to assist you with conversations and even auto-type your responses with precision. 🚀"
    )
    print(
        "💡 Pro Tip: When using the writer function, ensure your cursor is placed where you want the text to appear."
    )
    load_conversation_history()  # Load history on startup
    while True:
        user_input = listen.listen()
        # user_input = input("You: ") #for manual input
        print("You: ", user_input)
        if user_input.lower() == "exit":
            save_conversation_history()  # Save before exiting
            print("Goodbye! See you next time. 😊")
            break
        response = chat(user_input)
        print(f"Nova: {response}")
