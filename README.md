---

# Nova: Your Personal Voice-Activated Assistant

Nova is an intelligent, voice-activated assistant designed to streamline your daily tasks. With capabilities like fetching the latest news, opening the calculator, and simulating typing, Nova offers a seamless, interactive experience by leveraging a range of APIs and libraries.

## Key Features

- **Voice Recognition**: Powered by `speechrecognition` and `pyaudio` for smooth command listening.
- **News Fetching**: Get the latest updates from around the world with the `newsapi-python` library.
- **Open Calculator**: Launches the calculator application effortlessly.
- **Auto Typing**: Simulates automatic typing based on user input using `pyautogui`.
- **Conversation History**: Keeps track of your interactions with a history log saved in a JSON file.
- **Environment Variables**: Manage API keys and sensitive data securely with `python-dotenv`.

## Requirements

Nova requires the following Python packages:

- `pyaudio`
- `pygame`
- `speechrecognition`
- `python-dotenv`
- `newsapi-python`
- `openai`
- `pyautogui`

Install these dependencies with:

```sh
pip install -r requirements.txt
```

## Setup

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/nova.git
   cd nova
   ```

2. **Create a `.env` file**:

   ```sh
   touch .env
   ```

3. **Add your API keys to the `.env` file**:

   ```env
   NEWS_API_KEY=your_news_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Run the application**:

   ```sh
   python main.py
   ```

## Usage

- **Voice Commands**: Simply speak to Nova to fetch news, open the calculator, or type text.
- **Manual Input**: If preferred, you can manually input commands.

## Project Structure

```
.
├── __pycache__/
├── .env
├── .gitignore
├── .vscode/
│   └── tasks.json
├── conversation_history.json
├── getNews.py
├── listen.py
├── main.py
├── openCalc.py
├── requirements.txt
├── vars.py
└── writer.py
```

## Contributing

We welcome contributions! Feel free to open an issue or submit a pull request if you'd like to help improve Nova.

## License

This project is licensed under the MIT License.

---
