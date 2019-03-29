# here we want to read microphone or voice file
import sounddevice as sd
import numpy as np


class ReadData:
    def __init__(self, fs=44100, channels=2):
        self.fs = fs
        self.ch = channels
        self.duration = 5  # second
        self.voice = np.array([])

    def recording(self, duration=5):
        self.duration = duration
        self.voice = sd.rec(self.duration * self.fs, samplerate=self.fs, channels=self.ch, dtype='float64')
        sd.wait()

    def play(self):
        sd.play(self.voice, self.fs)
        sd.wait()


if __name__ == '__main__':
    read = ReadData()
    read.recording()
    read.play()
