import speech_recognition as sr
import pygame

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        pygame.mixer.init()
        pygame.mixer.music.load("wake_detected.mp3")
        # Set the volume (0.0 to 1.0)
        pygame.mixer.music.set_volume(0.3)  # Adjust the volume level here

        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None