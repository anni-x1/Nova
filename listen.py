import speech_recognition as sr
import pygame
import time
from play_audio import eff

def listen():
    """
    Listen for audio input and convert speech to text.
    Returns: str or None: Transcribed text if successful, None if failed
    """
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            # Adjust for ambient noise once at the beginning
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            # Set energy threshold for better recognition
            recognizer.energy_threshold = 400  # Adjust based on your environment
            recognizer.dynamic_energy_threshold = True

            while True:
                print("Listening...")
                eff("./sound_effects/listening.wav")
                try:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    print("Recognizing...")
                    text = recognizer.recognize_google(audio)
                    eff("./sound_effects/recognised.wav")
                    return text  # Return the recognized text

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
    except FileNotFoundError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        pygame.mixer.quit()


if __name__ == "__main__":
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
