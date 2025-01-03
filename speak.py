from elevenlabs import play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="sk_e1617f48447068dd5b500ba0b716edd20a2aa22edab1ffec", # Defaults to ELEVEN_API_KEY or ELEVENLABS_API_KEY
)
def speak(text):
    audio = client.generate(
        text=text,
        voice="Brian",
        model="eleven_multilingual_v2"
    )
    play(audio)
# speak("hello")