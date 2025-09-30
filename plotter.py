import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

class Graph:
    @staticmethod
    def save_combined_plot(t, signals_data, filename="all_signals_and_spectra.png"):

        fig, axes = plt.subplots(4, 4, figsize=(16, 12))
        fig.suptitle("Анализ сигналов: гармонический и цифровой (меандр)", fontsize=16, fontweight='bold')

        for i, (freq, sine_sig, square_sig, sine_freqs, sine_spec, square_freqs, square_spec) in enumerate(signals_data):
            ax1 = axes[i, 0]
            ax1.plot(t, sine_sig, color='green', linewidth=1.2)
            ax1.set_title(f"Гармонический — {freq} Гц", fontsize=10)
            ax1.set_xlabel("Время (с)", fontsize=9)
            ax1.set_ylabel("Амплитуда", fontsize=9)
            ax1.grid(True, linestyle='--', alpha=0.6)
            ax1.set_xlim(0, 1.0)
            ax1.xaxis.set_major_locator(MultipleLocator(0.2))
            ax1.xaxis.set_minor_locator(MultipleLocator(0.05))
            ax1.yaxis.set_major_locator(MultipleLocator(0.5))
            ax1.yaxis.set_minor_locator(MultipleLocator(0.1))


            ax2 = axes[i, 1]
            ax2.stem(sine_freqs, sine_spec, linefmt='r-', markerfmt='ro', basefmt=" ")
            ax2.set_title(f"Спектр — {freq} Гц", fontsize=10)
            ax2.set_xlabel("Частота (Гц)", fontsize=9)
            ax2.set_ylabel("Амплитуда", fontsize=9)
            ax2.grid(True, linestyle='--', alpha=0.6)
            ax2.set_xlim(0, 50)
            ax2.xaxis.set_major_locator(MultipleLocator(10))
            ax2.xaxis.set_minor_locator(MultipleLocator(2))
            ax2.set_ylim(bottom=0)

            ax3 = axes[i, 2]
            ax3.plot(t, square_sig, color='blue', linewidth=1.2)
            ax3.set_title(f"Меандр — {freq} Гц", fontsize=10)
            ax3.set_xlabel("Время (с)", fontsize=9)
            ax3.set_ylabel("Амплитуда", fontsize=9)
            ax3.grid(True, linestyle='--', alpha=0.6)
            ax3.set_xlim(0, 1.0)
            ax3.xaxis.set_major_locator(MultipleLocator(0.2))
            ax3.xaxis.set_minor_locator(MultipleLocator(0.05))
            ax3.yaxis.set_major_locator(MultipleLocator(0.5))
            ax3.yaxis.set_minor_locator(MultipleLocator(0.1))


            ax4 = axes[i, 3]
            ax4.stem(square_freqs, square_spec, linefmt='purple', markerfmt='mo', basefmt=" ")
            ax4.set_title(f"Спектр — {freq} Гц", fontsize=10)
            ax4.set_xlabel("Частота (Гц)", fontsize=9)
            ax4.set_ylabel("Амплитуда", fontsize=9)
            ax4.grid(True, linestyle='--', alpha=0.6)
            ax4.set_xlim(0, 50)
            ax4.xaxis.set_major_locator(MultipleLocator(10))
            ax4.xaxis.set_minor_locator(MultipleLocator(2))
            ax4.set_ylim(bottom=0)

        plt.tight_layout(rect=[0, 0.02, 1, 0.95])
        os.makedirs("output", exist_ok=True)
        plt.savefig(f"output/{filename}", dpi=300, bbox_inches='tight')
        plt.close()