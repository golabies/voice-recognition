# here we want to read microphone or voice file
import sounddevice as sd
from scipy.io import wavfile
import os
import numpy as np
import matplotlib.pyplot as plt


class ReadData:
    def __init__(self, fs=44100, channels=1):
        # channels is the Number of microphones
        address = '/'.join(os.getcwd().split('/')[:-1])
        os.chdir(address)
        os.chdir('wave_files')
        self.fs = fs
        self.ch = channels
        self.name = 'out_put'
        self.duration = 5  # second
        self.voice = np.array([])

    def recording(self, duration=5):
        # read data from microphone
        # duration is the length of time you want to record
        self.duration = duration
        self.voice = sd.rec(self.duration * self.fs, samplerate=self.fs, channels=self.ch, dtype='float64')
        sd.wait()
        self.voice = self.voice.T.copy()

    def play(self):
        sd.play(self.voice.T.copy(), self.fs)
        sd.wait()

    def show(self):
        for i in range(len(self.voice)):
            plt.plot(np.arange(len(self.voice[i])), self.voice[i]+i*5)
        plt.show()

    def save_data(self, name='out_put'):
        # be careful last file will delete
        self.name = name
        for i in range(len(self.voice)):
            wavfile.write(self.name+'_'+str(i)+'.wav', rate=len(self.voice[0]), data=self.voice[i])

    def read_wave(self, name='out_put_0.wav'):
        self.name = name
        _, self.voice = wavfile.read(self.name)
        self.voice: np.ndarray
        self.voice = np.array([self.voice])

    def output(self):
        return self.voice, self.fs


if __name__ == '__main__':
    read = ReadData()
    print('Recording')
    read.read_wave()
    # read.recording()
    print('Play')
    read.play()
    read.show()
    read.save_data()
