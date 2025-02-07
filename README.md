# Astra: Your Personal Voice-Activated Assistant 🌟✨🎙️

Astra is an intelligent, voice-activated assistant designed to streamline your daily tasks. With capabilities like fetching the latest news, opening the calculator, and simulating typing, Astra offers a seamless, interactive experience by leveraging a range of APIs and libraries. 🚀💡🎧

## Key Features 🎯💻🔊

- **Voice Recognition with Wake Word**: Activate Astra by simply saying "Hey Astra" using Picovoice's Porcupine engine and a custom `.ppn` model for wake word detection. 🗣️🖥️
- **News Fetching**: Get the latest updates from around the world with the newsapi-python library. 🌍📰✨
- **Open Calculator**: Launches the calculator application effortlessly. ➕🖩⚡
- **Auto Typing**: Simulates automatic typing based on user input using pyautogui. ⌨️🤖💬
- **Conversation History**: Keeps track of your interactions with a history log saved in a JSON file. 📜🕒📂
- **Environment Variables**: Manage API keys and sensitive data securely with python-dotenv. 🔑🛡️📄

## Requirements 📦🛠️⚙️

Astra requires the following Python packages:

- pyaudio
- pygame
- speechrecognition
- python-dotenv
- newsapi-python
- openai
- pyautogui
- pvporcupine
- sounddevice

Install these dependencies with:

```sh
pip install -r requirements.txt
```

## Setup 🛠️🔧📋

1. **Clone the repository**: 🖥️📂

   ```sh
   git clone https://github.com/yourusername/Astra.git
   cd Astra
   ```

2. **Create a .env file**: 📝🔐

   ```sh
   touch .env
   ```

3. **Add your API keys to the .env file**: 🔑🗝️

   ```env
   NEWS_API_KEY=your_news_api_key
   OPENAI_API_KEY=your_openai_api_key
   PPM_ACCESS_KEY=your_ppm_access_key
   ```

4. **Add your custom `.ppn` model**: 🎤🖥️

   - Place your `.ppn` file (e.g., `hey_Astra.ppn`) in the `voice_activation/` directory.
   - Ensure the path is correctly referenced in `wake.py`. 🌟🗂️

5. **Get Your Own `.ppn` Model**: 🌐🔊

   - Visit [Picovoice Console](https://console.picovoice.ai/). 🌍✨
   - Sign up or log in to your account. 🔐💻
   - Create a new wake word model by specifying the desired wake word (e.g., "Hey Astra"). 🎙️🖊️
   - Download the `.ppn` model file and place it in the `voice_activation/` directory. 📥🗂️

6. **Run the application**: 🚀💡

   ```sh
   python main.py
   ```

## Usage 🎤🖥️✨

- **Voice Commands**: Activate Astra by saying "Hey Astra" and give commands to fetch news, open the calculator, or type text. 🎙️💻
- **Manual Input**: If preferred, you can manually input commands. ✍️🔧

## Project Structure 📂🛠️✨

```
.
├── __pycache__/
├── .env
├── .gitignore
├── .vscode/
│   └── tasks.json
├── sound_effects/
│   ├── bye.wav
│   ├── error_msg.mp3
│   ├── error.wav
│   ├── listening.wav
│   └── recognised.wav
├── tools/
│   ├── __pycache__/
│   ├── getNews.py
│   ├── openCalc.py
│   └── writer.py
├── voice_activation/
│   ├── __pycache__/
│   ├── hey_Astra.ppn
│   ├── wake.py
├── chat.py
├── history_management.py
├── history.json
├── listen.py
├── main.py
├── play_audio.py
├── README.md
├── requirements.txt
└── vars.py
```

## Contributing 🤝🌟✨

We welcome contributions! Feel free to open an issue or submit a pull request if you'd like to help improve Astra. 💻🌍🎉

## License 📝⚖️📂

This project is licensed under the MIT License. 📜✨

