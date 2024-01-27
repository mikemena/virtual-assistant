import sounddevice as sd
import numpy as np


def test_sounddevice():
    # Parameters
    duration = 5  # seconds
    samplerate = 44100  # Hz
    channels = 1  # 1 = Mono , 2 = Stereo

    # Record audio
    print("Recording...")
    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=channels,
        dtype="float64",
    )
    sd.wait()  # Wait until recording is finished
    print("Recording complete. Playing back...")

    # Play back audio
    sd.play(recording, samplerate)
    sd.wait()  # Wait until playback is finished


if __name__ == "__main__":
    test_sounddevice()
