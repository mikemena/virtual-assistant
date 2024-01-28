import sounddevice as sd
import numpy as np
import speech_recognition as sr
import io


def record_audio(duration=5, samplerate=44100):
    """Record audio with the specified duration and samplerate."""
    print("Recording...")
    recording = sd.rec(
        int(duration * samplerate), samplerate=samplerate, channels=1, dtype="int16"
    )
    sd.wait()  # Wait until the recording is finished
    print("Recording complete")
    return np.array(recording, dtype=np.int16)


def recognize_audio(audio_data, samplerate=44100):
    """Recognize speech from the audio data."""
    recognizer = sr.Recognizer()

    # Convert the NumPy array to audio data with the required parameters
    audio = sr.AudioData(
        audio_data, samplerate, 2
    )  # 2 bytes per sample for 'int16' dtype

    # Recognize speech using Google Web Speech API
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"Transcription: {text}")
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")


if __name__ == "__main__":
    # Record audio
    recorded_audio = record_audio(duration=5)

    # Convert the NumPy array to raw audio bytes
    audio_bytes = recorded_audio.tobytes()

    # Recognize the recorded audio
    recognize_audio(audio_bytes)
