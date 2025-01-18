import base64
import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from play_audio import play_audio
import vars
from history_management import save_history
from tools import getNews
from tools import openCalc
from tools import writer

load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Chat function
def chat(user_input):
    print("Processing...")
    # Append the user's input to the conversation history
    vars.history.append(
        {"role": "user", "content": [{"type": "text", "text": user_input}]}
    )

    # Generate response from OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini-audio-preview",
            modalities=["text", "audio"],
            audio={"voice": "sage", "format": "wav"},
            messages=vars.history,
            tools=vars.tools,
            tool_choice="auto",
        )
        message = response.choices[0].message

    except Exception as e:
        print(f"Error during OpenAI API call: {e}")
        return "I encountered an error while processing your request."

    if message.audio:
        wav_bytes = base64.b64decode(response.choices[0].message.audio.data)
        play_audio(wav_bytes)

    if hasattr(message, "tool_calls") and message.tool_calls:
        tool_name = message.tool_calls[0].function.name
        arguments_string = message.tool_calls[0].function.arguments

        try:
            tool_args = json.loads(arguments_string)
        except json.JSONDecodeError as e:
            # print(f"Error decoding tool arguments: {e}")
            # print("Attempting to fix JSON by replacing single quotes with double quotes...")
            try:
                # Attempt to fix common JSON errors like single quotes
                arguments_string = arguments_string.replace("'", '"')
                arguments_string = arguments_string.replace("True", 'true')
                arguments_string = arguments_string.replace("False", 'false')
                arguments_string = arguments_string.replace("None", 'null')
                tool_args = json.loads(arguments_string)
                # print("JSON fix successful.")
            except json.JSONDecodeError as e:
                print(f"Failed to decode tool arguments even after fix: {e}")
                return "I encountered an issue understanding the tool's requirements."

        if tool_name == "get_top_news":
            topic = tool_args.get("topic")
            tool_response = getNews.get_top_news(topic)
        elif tool_name == "open_calculator":
            tool_response = openCalc.open_calculator()
        elif tool_name == "writer":
            # Handle writer function call and type out the content
            writer_input = tool_args.get("user_input")
            tool_response = writer.writer(writer_input)

        # Append function response to history
        vars.history.append(
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "id": message.tool_calls[0].id,
                        "type": "function",
                        "function": {"name": tool_name, "arguments": str(tool_args)},
                    }
                ],
            }
        )
        save_history()  # Save updated history
        vars.history.append(
            {
                "role": "tool",
                "content": [{"type": "text", "text": tool_response}],
                "tool_call_id": message.tool_calls[0].id,
            },
        )
        save_history()

        # Generate a refined response
        refined_response = client.chat.completions.create(
            model="gpt-4o-mini-audio-preview",
            modalities=["text", "audio"],
            audio={"voice": "sage", "format": "wav"},
            messages=vars.history,
        )
        # Append Astra's response to history
        final_response = refined_response.choices[0].message.audio.transcript
        vars.history.append(
            {
                "role": "assistant",
                "audio": {"id": refined_response.choices[0].message.audio.id},
            }
        )
        save_history()  # Save updated history

        wav_bytes = base64.b64decode(refined_response.choices[0].message.audio.data)
        play_audio(wav_bytes)
        return final_response

    # Append Astra's direct response to history
    vars.history.append(
        {
            "role": "assistant",
            "audio": {"id": message.audio.id},
        }
    )
    save_history()  # Save updated history
    return message.audio.transcript