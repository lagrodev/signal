import numpy as np
from scipy import signal
# SignalGenerator
class SignalGenerator:
    def __init__(self, fs=100, duration=1.0):
        self.fs = 10000
        self.duration = duration
        self.t = np.linspace(0, duration, int(fs * duration), endpoint=False)

    def update_params(self, fs, duration):
        self.fs = 10000
        self.duration = duration
        self.t = np.linspace(0, duration, int(fs * duration), endpoint=False)

    def generate_sine(self, freq):
        return np.sin(2 * np.pi * freq * self.t)

    def generate_square(self, freq):
        period = 1.0 / freq
        phase = (self.t % period) / period
        square_wave = np.where(phase < 0.5, 1, 0)
        return square_wave
