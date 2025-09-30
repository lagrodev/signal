import numpy as np

# SpectrumAnalyzer
class SpectrumAnalyzer:
    @staticmethod
    def compute_fft(signal, fs, max_freq=50):
        n = len(signal)
        freqs = np.fft.rfftfreq(n, 1 / fs)
        spectrum = np.abs(np.fft.rfft(signal)) / n
        spectrum[0] = 0

        mask = freqs <= max_freq
        limited_freqs = freqs[mask]
        limited_spectrum = spectrum[mask]


        return limited_freqs, limited_spectrum
