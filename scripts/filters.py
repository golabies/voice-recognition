import numpy as np
import matplotlib.pyplot as plt


class Filters:
    def __init__(self, signal):
        self.sig = signal

    def smooth(self, wsz):
        out0 = np.convolve(self.sig, np.ones(wsz, dtype=float), 'valid') / wsz
        r = np.arange(1, wsz - 1, 2)
        start = np.cumsum(self.sig[:wsz - 1])[::2] / r
        stop = (np.cumsum(self.sig[:-wsz:-1])[::2] / r)[::-1]
        return np.concatenate((start, out0, stop))

    @staticmethod
    def show(func, *inputs):
        x = func(*inputs)
        y = np.arange(len(x))
        plt.plot(y, x)
        plt.show()
