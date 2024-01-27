import pyaudio

p = pyaudio.PyAudio()

stream = p.open(
    format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024
)

data = stream.read(1024)
