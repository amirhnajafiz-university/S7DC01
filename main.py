# importing numpy module for generating arrays of numbers
import numpy as np
# importing scipy module for generating signals
from scipy import signal
# importing matplotlib for displaying signals
import matplotlib.pyplot as plt



if __name__ == "__main__":
    a = 2
    w = 20

    t = np.linspace(-5, 5, 10000, endpoint=False)
    sig = 0.5 * (signal.square(2 * np.pi * 5 * t) + 1)
    car = a * np.cos(2 * np.pi * t * w)

    tresh = 0.005 * np.sin(2 * np.pi * t * 50)

    plt.subplot(3, 1, 1)

    plt.title("input pulse")
    plt.plot(t, sig)
    plt.ylim(-1, 2)

    plt.subplot(3, 1, 2)

    plt.title("carrier")
    plt.plot(t, car)
    plt.ylim(-1 + (-1) * a, a + 1)

    plt.subplot(3, 1, 3)

    plt.title("output signal")
    plt.plot(t, np.multiply(sig, car) + tresh)
    plt.ylim(-1 + (-1) * a, a + 1)

    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.show()