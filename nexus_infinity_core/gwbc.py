import numpy as np
from scipy.signal import butter, lfilter

class GravitationalWaveBasedCommunication:
    """
    Gravitational Wave-Based Communication for transmitting data through gravitational waves.

    Attributes:
    -----------
    fs : float
        Sampling frequency for the gravitational wave signal.
    """

    def __init__(self, fs):
        self.fs = fs

    def modulate(self, data, carrier_frequency):
        """
        Modulate the data onto a gravitational wave carrier signal.

        Parameters:
        -----------
        data : numpy.array
            Data to be transmitted.
        carrier_frequency : float
            Frequency of the gravitational wave carrier signal.

        Returns:
        -------
        modulated_signal : numpy.array
            Modulated gravitational wave signal.
        """
        # Generate a gravitational wave carrier signal
        t = np.arange(0, 1, 1 / self.fs)
        carrier_signal = np.sin(2 * np.pi * carrier_frequency * t)

        # Modulate the data onto the carrier signal
        modulated_signal = carrier_signal * data

        return modulated_signal

    def demodulate(self, modulated_signal, carrier_frequency):
        """
        Demodulate the received gravitational wave signal to extract the original data.

        Parameters:
        -----------
        modulated_signal : numpy.array
            Received modulated gravitational wave signal.
        carrier_frequency : float
            Frequency of the gravitational wave carrier signal.

        Returns:
        -------
        data : numpy.array
            Demodulated data.
        """
        # Demodulate the received signal
        data = modulated_signal * np.sin(2 * np.pi * carrier_frequency * np.arange(0, 1, 1 / self.fs))

        return data
