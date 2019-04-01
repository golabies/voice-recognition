import numpy as np
import matplotlib.pyplot as plt


class Filters:
    def __init__(self):
        pass

    @staticmethod
    def smooth(signal, wsz):
        out0 = np.convolve(signal, np.ones(wsz, dtype=float), 'valid') / wsz
        r = np.arange(1, wsz - 1, 2)
        start = np.cumsum(signal[:wsz - 1])[::2] / r
        stop = (np.cumsum(signal[:-wsz:-1])[::2] / r)[::-1]
        return np.concatenate((start, out0, stop))

    @staticmethod
    def differences(signal):
        diff = []
        for i in range(1, len(signal)):
            diff.append(abs(signal[i] - signal[i-1]))
        diff = np.array(diff)
        return diff

    @staticmethod
    def show(func, *inputs):
        x = func(*inputs)
        y = np.arange(len(x))
        plt.plot(y, x)
        plt.show()
