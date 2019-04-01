from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np


class Cluster:
    def __init__(self, signal):
        self.signal = signal
        self.labels = []

    def clustering(self):
        self.signal = self.signal.reshape(-1, 1)
        cls = KMeans(n_clusters=3)
        cls.fit(self.signal)
        self.labels = cls.labels_

    def show(self):
        y = self.signal
        x = np.arange(len(y))
        plt.scatter(x, y, c=self.labels, s=0.1)
        plt.show()
