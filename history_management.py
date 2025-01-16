import json
import vars

# File path to save conversation history
HISTORY_FILE = "history.json"

# Load conversation history from file
def load_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            vars.history = json.load(file)
            print("Conversation history loaded successfully!")
    except FileNotFoundError:
        vars.history = []
        print("No previous conversation history found. Starting fresh.")
    except json.JSONDecodeError:
        vars.history = []
        print("Corrupted history file. Starting fresh.")

# Save conversation history to file
def save_history():
    try:
        with open(HISTORY_FILE, "w") as file:
            json.dump(vars.history, file, indent=4)
    except Exception as e:
        print(f"Failed to save conversation history: {e}")
