import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

# plotter
class Plotter:
    @staticmethod
    def save_signal(t, signal, title, filename, draw_initial_pulse = False):
        os.makedirs("graphics", exist_ok=True)
        plt.figure(figsize=(8, 4))
        plt.plot(t, signal, linewidth=1.5)

        if draw_initial_pulse:
            plt.vlines(0, 0.5, 1,linewidth=1.5)

        plt.title(title, fontsize=14)
        plt.xlabel("Время (с)", fontsize=12)
        plt.ylabel("Амплитуда", fontsize=12)

        ax = plt.gca()

        x_range = t[-1] - t[0]
        if x_range <= 1:
            x_major_step = 0.1
            x_minor_step = 0.02
        elif x_range <= 5:
            x_major_step = 0.5
            x_minor_step = 0.1
        else:
            x_major_step = 1
            x_minor_step = 0.2

        ax.xaxis.set_major_locator(MultipleLocator(x_major_step))
        ax.xaxis.set_minor_locator(MultipleLocator(x_minor_step))

        y_range = np.max(signal) - np.min(signal)
        if y_range <= 1:
            y_major_step = 0.1
            y_minor_step = 0.02
        elif y_range <= 5:
            y_major_step = 0.5
            y_minor_step = 0.1
        else:
            y_major_step = 1
            y_minor_step = 0.2

        ax.yaxis.set_major_locator(MultipleLocator(y_major_step))
        ax.yaxis.set_minor_locator(MultipleLocator(y_minor_step))

        plt.grid(True, which='major', alpha=0.5)
        plt.grid(True, which='minor', alpha=0.2)

        plt.tight_layout()
        plt.savefig(os.path.join("graphics", filename), dpi=150)
        plt.close()

    @staticmethod
    def save_spectrum(freqs, spectrum, title, filename):
        os.makedirs("graphics", exist_ok=True)
        plt.figure(figsize=(8, 4))
        plt.plot(freqs, spectrum, linewidth=1.5)
        plt.title(title, fontsize=14)
        plt.xlabel("Частота (Гц)", fontsize=12)
        plt.ylabel("Амплитуда", fontsize=12)

        ax = plt.gca()

        x_range = freqs[-1] if len(freqs) > 0 else 50
        if x_range <= 10:
            x_major_step = 1
            x_minor_step = 0.2
        elif x_range <= 50:
            x_major_step = 5
            x_minor_step = 1
        elif x_range <= 100:
            x_major_step = 10
            x_minor_step = 2
        else:
            x_major_step = 20
            x_minor_step = 5

        ax.xaxis.set_major_locator(MultipleLocator(x_major_step))
        ax.xaxis.set_minor_locator(MultipleLocator(x_minor_step))

        y_max = np.max(spectrum) if len(spectrum) > 0 else 1
        if y_max <= 0.1:
            y_major_step = 0.02
            y_minor_step = 0.005
        elif y_max <= 0.5:
            y_major_step = 0.1
            y_minor_step = 0.02
        elif y_max <= 1:
            y_major_step = 0.2
            y_minor_step = 0.05
        else:
            y_major_step = 0.5
            y_minor_step = 0.1

        ax.yaxis.set_major_locator(MultipleLocator(y_major_step))
        ax.yaxis.set_minor_locator(MultipleLocator(y_minor_step))

        plt.grid(True, which='major', alpha=0.5)
        plt.grid(True, which='minor', alpha=0.2)

        plt.tight_layout()
        plt.savefig(os.path.join("graphics", filename), dpi=150)
        plt.close()

    @staticmethod
    def make_combined_plot(t, signal, freqs, spectrum, title, draw_initial_pulse = False):
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        axes[0].plot(t, signal, linewidth=1.5)

        axes[0].set_title(f"{title} — сигнал", fontsize=14)
        axes[0].set_xlabel("Время (с)", fontsize=12)
        axes[0].set_ylabel("Амплитуда", fontsize=12)

        x_range = t[-1] - t[0]
        if x_range <= 1:
            x_major_step = 0.1
            x_minor_step = 0.02
        else:
            x_major_step = 0.5
            x_minor_step = 0.1

        axes[0].xaxis.set_major_locator(MultipleLocator(x_major_step))
        axes[0].xaxis.set_minor_locator(MultipleLocator(x_minor_step))

        y_range = np.max(signal) - np.min(signal)
        if y_range <= 1:
            y_major_step = 0.1
            y_minor_step = 0.02
        else:
            y_major_step = 0.5
            y_minor_step = 0.1

        axes[0].yaxis.set_major_locator(MultipleLocator(y_major_step))
        axes[0].yaxis.set_minor_locator(MultipleLocator(y_minor_step))

        axes[0].grid(True, which='major', alpha=0.5)
        axes[0].grid(True, which='minor', alpha=0.2)

        axes[1].plot(freqs, spectrum, linewidth=1.5)


        axes[1].set_title(f"{title} — спектр", fontsize=14)
        axes[1].set_xlabel("Частота (Гц)", fontsize=12)
        axes[1].set_ylabel("Амплитуда", fontsize=12)

        x_range = freqs[-1] if len(freqs) > 0 else 50
        if x_range <= 10:
            x_major_step = 1
            x_minor_step = 0.2
        elif x_range <= 50:
            x_major_step = 5
            x_minor_step = 1
        else:
            x_major_step = 10
            x_minor_step = 2

        axes[1].xaxis.set_major_locator(MultipleLocator(x_major_step))
        axes[1].xaxis.set_minor_locator(MultipleLocator(x_minor_step))

        y_max = np.max(spectrum) if len(spectrum) > 0 else 1
        if y_max <= 0.1:
            y_major_step = 0.02
            y_minor_step = 0.005
        elif y_max <= 0.5:
            y_major_step = 0.1
            y_minor_step = 0.02
        else:
            y_major_step = 0.2
            y_minor_step = 0.05

        axes[1].yaxis.set_major_locator(MultipleLocator(y_major_step))
        axes[1].yaxis.set_minor_locator(MultipleLocator(y_minor_step))

        axes[1].grid(True, which='major', alpha=0.5)
        axes[1].grid(True, which='minor', alpha=0.2)

        plt.tight_layout()
        return fig