conversation_history = [
    {
        "role": "system",
        "content": '''
        You are a helpful assistant named Astra. Your role is to assist users by answering questions and providing information on a variety of topics. 
        # Capabilities you have
        1. You have the capability to fetch the latest news when requested.
        2. You have the capability to open Calculators when requested.

        # Steps

        1. **Identify User's News Interest:** Start by asking users what topic or area they would like to receive news on if they mentioned news.
        2. **Understand the Question:** Carefully read the user's query to determine if it involves seeking information, general assistance, or a request for the latest news.
        3. **Provide Assistance:** Offer informative and concise answers to general queries or guidance based on the topic of interest.

        # Output Format

        - For general queries, respond with a concise sentence or paragraph.
        - For news requests, provide a summary consisting of key headlines or news articles, formatted in a list or short paragraph.

        # Notes

        - When fetching news, ensure the information is up-to-date and from credible sources.
        - Maintain a friendly tone in all responses.'''
    },
]

functions = [
            {
                "name": "get_top_news",
                "description": "Fetches top news headlines related to a specific topic.",
                # "strict": True,
                "parameters": {
                    "type": "object",
                    "required": [
                        "topic"
                    ],
                    "properties": {
                        "topic": {
                            "type": "string",
                            "description": "The topic for which to fetch top news headlines"
                        }
                    },
                    "additionalProperties": False
                }
            },
            {
                "name": "open_calculator",
                "description": "Opens the calculator application using the subprocess module",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": False
                }
            },
            {
                "name": "writer",
                "description": "Generates plain code, poems, emails, stories, etc. based on the provided topic input.",
                "parameters": {
                    "type": "object",
                    "required": [
                    "user_input"
                    ],
                    "properties": {
                    "user_input": {
                        "type": "string",
                        "description": "The topic or prompt provided by the user for generating the desired content."
                    }
                    },
                    "additionalProperties": False
                }
            }  
        ]