import pyaudio
from openai import OpenAI
import os
from dotenv import load_dotenv
import pygame
import time

load_dotenv()

def play_audio(audio_data, sample_rate=24000): #Added sample_rate as a parameter
    """Plays audio data using pyaudio.

    Args:
        audio_data: Base64-decoded audio data (bytes).
        sample_rate:  The sample rate of the audio data (in Hz).  Defaults to 24000 Hz.  Get this from the OpenAI response for better accuracy.
    """
    try:
        p = pyaudio.PyAudio()
        audio_stream = p.open(
            format=p.get_format_from_width(width=2),  # Assuming 16-bit audio
            channels=1,
            rate=sample_rate,
            output=True,
        )
        audio_stream.write(audio_data)
        audio_stream.stop_stream()
        audio_stream.close()
        p.terminate()
    except Exception as e:
        print(f"Error playing audio: {e}")

def eff(effect):
    pygame.mixer.init()
    pygame.mixer.music.load(effect)
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

# def speak():

#     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#     response = client.audio.speech.create(
#         model="tts-1-hd",
#         voice="sage",
#         input="Good bye! See you next time.",
#         response_format="wav",
#     )

#     response.stream_to_file("./sound_effects/bye.wav")
# speak()