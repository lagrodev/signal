import numpy as np

class Analyzer:
    @staticmethod
    def arifm(signal: np.ndarray, fs: int, max_freq: float = 50.0):
        n = len(signal)
        freqs_full = np.fft.rfftfreq(n, d=1 / fs)
        spectrum_full = np.abs(np.fft.rfft(signal)) / n
        spectrum_full[0] = 0

        freqs = freqs_full[freqs_full <= max_freq]
        spectrum = spectrum_full[freqs_full <= max_freq]

        return freqs, spectrum