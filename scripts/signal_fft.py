import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt


class MyFt:
    def __init__(self, signal, fs):
        self.signal = signal
        self.fs = fs
        self.freq = []
        self.out_put = []

    def my_ft(self):
        mft = fft(self.signal)
        freq = np.linspace(-self.fs / 2, self.fs / 2, len(self.signal))
        mft = mft[freq >= 0]
        freq = freq[freq >= 0]
        mft = mft[::-1]
        mft[2:] = 2 * mft[2:]
        self.freq = freq
        self.out_put = abs(mft) / len(self.signal)
        return self.freq, self.out_put

    def show(self):
        plt.plot(self.freq, np.log10(self.out_put))
        plt.show()
