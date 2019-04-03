import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
def plot(data, centers, colors, color_labels):
    plt.scatter(*data.T, c=color_labels, alpha=0.6)
    plt.scatter(*centers.T, c=colors, marker='s', edgecolor='yellow')

    plt.title("K-Means")
    plt.show()

def animate(data, centers, colors, color_labels):
    fig=plt.figure()

    x,y,c=*data.T, np.array(["#000000", "#000000", "#000000"])
    scat = plt.scatter(x, y, c=c)
    def setup():
        x, y, c = *data.T, np.array(["#000000", "#000000", "#000000"])
        scat = plt.scatter(x, y, c=c)
        return scat,

    def update(frame, scat):

        scat.set_color(np.array(["#00e1ff","#00e1ff","#00e1ff"]))
        return scat,

    ani=animation.FuncAnimation(fig, update, interval=10, frames=range(2), init_func=setup, fargs=(scat,))
    plt.show()
animate(np.array([[0,1], [2,3], [3,4]]), None, None, np.array([[(0,0,0), (0,0,0), (0,0,0)], [(0,255,255), (0,255,255), (0,255,255)]]))

