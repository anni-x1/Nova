conversation_history = []

tools = [
    {
        "type": "function",
        "name": "get_top_news",
        "description": "Fetches top news headlines related to a specific topic.",
        "function": {
            "name": "get_top_news",
            "parameters": {
                "type": "object",
                "required": ["topic"],
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "The topic for which to fetch top news headlines",
                    }
                },
                "additionalProperties": False,
            }
        }
    },
    {
        "type": "function",
        "name": "open_calculator",
        "description": "Opens the calculator application using the subprocess module.",
        "function": {
            "name": "open_calculator",
            "parameters": {
                "type": "object",
                "properties": {},
                "additionalProperties": False,
            }
        }
    },
    {
        "type": "function",
        "name": "writer",
        "description": "Generates plain code, poems, emails, stories, etc. based on the provided topic input.",
        "function": {
            "name": "writer",
            "parameters": {
                "type": "object",
                "required": ["user_input"],
                "properties": {
                    "user_input": {
                        "type": "string",
                        "description": "The topic or prompt provided by the user for generating the desired content.",
                    }
                },
                "additionalProperties": False,
            }
        }
    },
]
