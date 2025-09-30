import os
from signals import Signal
from spectrum import Analyzer
from plotter import Graph

FREQUENCIES = [1, 2, 4, 8]
DURATION = 2.0
print("Генерация сигналов и спектров...")

def main():
    gen = Signal(DURATION)
    signals_data = []

    for f in FREQUENCIES:
        print(f"  -> Обработка {f} Гц...")

        sine_sig = gen.sine(f)
        sine_freqs, sine_spec = Analyzer.arifm(sine_sig, gen.fs, max_freq=50)

        square_sig = gen.unipolar_square(f)
        square_freqs, square_spec = Analyzer.arifm(square_sig, gen.fs, max_freq=50)

        signals_data.append((
            f,
            sine_sig,
            square_sig,
            sine_freqs,
            sine_spec,
            square_freqs,
            square_spec
        ))

    Graph.save_combined_plot(gen.t, signals_data, "all.png")

if __name__ == "__main__":
    main()