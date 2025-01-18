import pvporcupine
import sounddevice as sd
import numpy as np
from main import nova
import os
from dotenv import load_dotenv
load_dotenv()
# Global variable to control the loop
running = True

def wake():
    global running

    # Replace "YOUR_ACCESS_KEY" with the access key you got from Picovoice Console
    access_key = os.getenv("PPM_ACCESS_KEY")

    # Load Porcupine with the access key and custom wake word model
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=["A:\\Project Nova\\voice_activation\\hey_nova.ppn"]  # Path to your custom-trained wake word model
    )

    def audio_callback(indata, frames, time, status):
        global running
        if status:
            print(f"Error: {status}")
            return
        pcm = np.frombuffer(indata, dtype=np.int16)

        # Check if wake word is detected
        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            print("Nova is now active!")
            nova()  # Activate Nova

    print("Listening for wake word: 'Hey Nova'...")

    try:
        with sd.InputStream(
            callback=audio_callback,
            channels=1,
            samplerate=porcupine.sample_rate,
            blocksize=porcupine.frame_length,
            dtype="int16"
        ):
            while running:  # Keep running until the flag is set to False
                pass
    except KeyboardInterrupt:
        print("Program stopped by user.")
    finally:
        porcupine.delete()  # Free Porcupine resources
        print("Cleaned up resources and exiting.")

# if __name__ == "__main__":
#     try:
#         detect_wake_word()
#     except KeyboardInterrupt:
#         running = False
#         print("Stopping wake word detection. Goodbye!")
