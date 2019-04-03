import matplotlib.pyplot as plt
import numpy as np

def plot(data, centers, colors, color_labels):
    plt.scatter(*data.T, c=color_labels, alpha=0.6)
    plt.scatter(*centers.T, c=colors, marker='s', edgecolor='yellow')

    plt.title("K-Means")
    plt.show()
