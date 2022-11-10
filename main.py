# importing numpy module for generating arrays of numbers
import numpy as np
# importing scipy module for generating signals
from scipy import signal
# importing matplotlib for displaying signals
import matplotlib.pyplot as plt



if __name__ == "__main__":
    # carrier signal components
    carrier_amplitude = 2
    carrier_w0 = 4

    # time component
    time_component = 2

    # noise signal components
    noise_amplitude = 0.005
    noise_w0 = 200

    # creating a time series signal
    t = np.linspace((-1) * time_component, time_component, 250*time_component, endpoint=False)

    # our main input signal
    sig = 0.5 * (signal.square(2 * np.pi * 5 * t) + 1)

    # our signal carrier
    car = carrier_amplitude * np.cos(2 * np.pi * t * carrier_w0)

    # creating the noise signal
    noise = noise_amplitude * np.cos(2 * np.pi * t * noise_w0)

    # creating output signal
    # (input * carrier) + noise
    output = np.multiply(sig, car) + noise

    # display signals
    plt.subplot(3, 1, 1)

    plt.title("input pulse")
    plt.plot(t, sig)
    plt.ylim(-1, 2)

    plt.subplot(3, 1, 2)

    plt.title("carrier")
    plt.plot(t, car)
    plt.ylim(-1 + (-1) * carrier_amplitude, carrier_amplitude + 1)

    plt.subplot(3, 1, 3)

    plt.title("output signal")
    plt.plot(t, output)
    plt.ylim(-1 + (-1) * carrier_amplitude, carrier_amplitude + 1)

    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.show()