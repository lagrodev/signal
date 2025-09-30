import numpy as np

class Signal:
    def __init__(self, duration: float):
        self.fs = 10000
        self.duration = duration
        self.t = np.linspace(0, duration, int(self.fs * duration), endpoint=False)

    def sine(self, freq: float) -> np.ndarray:
        self.fs = 10000
        return np.sin(2 * np.pi * freq * self.t)

    def unipolar_square(self, freq: float) -> np.ndarray:
        period_samples = int(self.fs / freq)
        signal = np.zeros_like(self.t)
        signal[:period_samples // 2] = 1

        for i in range(0, len(signal), period_samples):
            end = min(i + period_samples // 2, len(signal))
            signal[i:end] = 1
        return signal