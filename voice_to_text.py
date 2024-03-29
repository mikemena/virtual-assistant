import sounddevice as sd
import numpy as np
import speech_recognition as sr


def record_audio(duration=5, samplerate=44100):  # default 44100 Hz is CD quality
    """Record audio with the specified duration and samplerate."""
    print("Recording...")
    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16",  # common format for audio
    )
    sd.wait()  # Wait until the recording is finished
    print("Recording complete")
    return np.array(recording, dtype=np.int16)
    # converted to an int16 NumPy array before returning, to match the expected format for speech recognition.


def transform_audio_into_text(audio_data, samplerate=44100):
    """Recognize speech from the audio data."""
    r = sr.Recognizer()

    # Convert the NumPy array to audio data with the required parameters
    audio = sr.AudioData(
        audio_data, samplerate, 2
    )  # 2 bytes per sample for 'int16' dtype

    # Recognize speech using Google Web Speech API
    try:
        print("Recognizing...")
        # Recognize speech using Google Web Speech API
        text = r.recognize_google(audio, language="en'us")
        print(f"Transcription: {text}")
        return text  # Return the recognized text
    except sr.UnknownValueError:
        # Google Web Speech API couldn't understand the audio
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        # A request error occurred
        print(f"Could not request results from Google Web Speech API; {e}")

    return None


if __name__ == "__main__":
    # Record audio
    recorded_audio = record_audio(duration=5)

    # Convert the NumPy array to raw audio bytes
    audio_bytes = recorded_audio.tobytes()

    # Recognize the recorded audio
    transform_audio_into_text(audio_bytes)
