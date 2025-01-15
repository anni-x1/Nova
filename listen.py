# import speech_recognition as sr
# import pygame
# import time
# import os


# def get_microphone():
#     """List available microphones and return the default one."""
#     mic_list = sr.Microphone.list_microphone_names()
#     # print("Available microphones:", mic_list)
#     return sr.Microphone(device_index=None)  # Uses default microphone


# def listen():
#     """
#     Listen for audio input and convert speech to text.
#     Returns: str or None: Transcribed text if successful, None if failed
#     """
#     recognizer = sr.Recognizer()

#     try:
#         # Get microphone
#         microphone = get_microphone()

#         # Initialize audio parameters
#         with microphone as source:
#             # Adjust for ambient noise
#             print("Adjusting for ambient noise... Please wait.")
#             recognizer.adjust_for_ambient_noise(source, duration=1)

#             # Set energy threshold for better recognition
#             recognizer.energy_threshold = 500  # Adjust based on your environment
#             recognizer.dynamic_energy_threshold = True

#             # Initialize pygame mixer
#             pygame.mixer.init()
#             pygame.mixer.music.load("wake_detected.mp3")
#             print("Listening...")
#             pygame.mixer.music.set_volume(0.3)

#             # Play wake sound
#             pygame.mixer.music.play()
#             time.sleep(0.5)  # Small delay to ensure sound plays

#             try:
#                 # Listen for audio input
#                 audio = recognizer.listen(
#                     source,
#                     timeout=5,  # Maximum time to wait for phrase to start
#                     phrase_time_limit=10,  # Maximum time for phrase to complete
#                 )

#                 # Attempt to recognize speech
#                 print("Recognizing...")
#                 text = recognizer.recognize_google(audio)
#                 print(f"User: {text}")
#                 return text.lower()

#             except sr.WaitTimeoutError:
#                 print("Listening timed out. No speech detected.")
#                 return None
#             except sr.UnknownValueError:
#                 print("Sorry, I couldn't understand the audio.")
#                 return None
#             except sr.RequestError as e:
#                 print(
#                     f"Could not request results from Google Speech Recognition service; {e}"
#                 )
#                 return None

#     except FileNotFoundError as e:
#         print(f"Error: {e}")
#         return None
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return None
#     finally:
#         # Clean up resources
#         if pygame.mixer.get_init():
#             pygame.mixer.quit()


# if __name__ == "__main__":
#     # Example usage
#     try:
#         while True:
#             result = listen()
#             if result:
#                 print(f"Processed text: {result}")
#                 # Add your command processing logic here

#             # Optional: Add a small delay between listening attempts
#             time.sleep(0.5)

#     except KeyboardInterrupt:
#         print("\nProgram terminated by user")
#     finally:
#         # Ensure cleanup
#         if pygame.mixer.get_init():
#             pygame.mixer.quit()
import speech_recognition as sr
import pygame
import time


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
            recognizer.energy_threshold = 700  # Adjust based on your environment
            recognizer.dynamic_energy_threshold = True

            while True:
                pygame.mixer.init()
                pygame.mixer.music.load("wake_detected.mp3")
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play()
                time.sleep(0.5)

                print("Listening...")
                try:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    print("Recognizing...")
                    text = recognizer.recognize_google(audio)
                    return text  # Return the recognized text

                except sr.UnknownValueError:
                    print("Sorry, I didn't catch that. Please speak again.")
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
