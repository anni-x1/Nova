import os
import speech_recognition as sr
import pygame
import time
from io import BytesIO
from pydub import AudioSegment
from groq import Groq
from play_audio import eff
from dotenv import load_dotenv

load_dotenv()

def initialize_audio():
    """Initialize Pygame mixer to ensure sound effects play properly."""
    pygame.mixer.init()

def listen():
    """
    Listen for audio input and convert speech to text using Groq.
    
    Returns:
        str or None: Transcribed text if successful, None if failed.
    """
    recognizer = sr.Recognizer()
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    try:
        with sr.Microphone(sample_rate=16000) as source:
            print("Calibrating for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=2)  # Adaptive noise reduction

            # Adjust sensitivity
            recognizer.energy_threshold = 300  # Adjust as needed
            recognizer.dynamic_energy_threshold = True  # Adaptive sensitivity

            print("Ready to listen!")

            while True:
                print("Listening...")
                eff("./sound_effects/listening.wav")

                try:
                    audio = recognizer.listen(
                        source, 
                        timeout=5, 
                        phrase_time_limit=10, 
                    )
                    print("Recognizing...")

                    # Convert WAV to M4A (AAC codec)
                    audio_data = audio.get_wav_data()
                    audio_wav = BytesIO(audio_data)
                    audio_m4a = BytesIO()

                    sound = AudioSegment.from_wav(audio_wav)
                    sound.export(audio_m4a, format="mp4")  # Export as M4A (mp4 format)

                    # Set filename for API compatibility
                    audio_m4a.name = "speech.m4a"

                    transcription = client.audio.transcriptions.create(
                        file=audio_m4a,
                        model="whisper-large-v3-turbo",
                        response_format="verbose_json"
                    )

                    if transcription.text:
                        eff("./sound_effects/recognised.wav")
                        return transcription.text

                except sr.UnknownValueError:
                    eff("./sound_effects/error.wav")
                    print("Sorry, I didn't catch that. Please speak again.")
                    eff("./sound_effects/error_msg.mp3")
                    continue
                except sr.WaitTimeoutError:
                    print("No audio detected. Listening again...")
                    continue

    except sr.RequestError as e:
        print(f"Error with recognition service: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        pygame.mixer.quit()

if __name__ == "__main__":
    initialize_audio()  # Ensure sound effects work properly

    try:
        while True:
            result = listen()
            if result:
                print(f"Processed text: {result}")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    finally:
        pygame.mixer.quit()
