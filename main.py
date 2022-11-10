# importing numpy module for generating arrays of numbers
import numpy as np
# importing scipy module for generating signals
from scipy import signal
# importing matplotlib for displaying signals
import matplotlib.pyplot as plt



if __name__ == "__main__":
    t = np.linspace(-0.5, 0.5, 500, endpoint=False)
    sig = 0.5 * (signal.square(2 * np.pi * 5 * t) + 1)

    plt.subplot(3, 1, 1)

    plt.title("input pulse")
    plt.plot(t, sig)
    plt.ylim(-2, 2)

    plt.subplot(3, 1, 2)

    plt.title("carrier")
    plt.plot(t, np.cos(2 * np.pi * t))
    plt.ylim(-2, 2)

    plt.subplot(3, 1, 3)

    plt.title("output signal")
    plt.plot(t, np.multiply(sig, np.cos(2 * np.pi * t)))
    plt.ylim(-2, 2)

    plt.show()