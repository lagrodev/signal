import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from signals import SignalGenerator
from spectrum import SpectrumAnalyzer
from plotter import Plotter

#main
class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Анализ сигналов")
        self.generator = SignalGenerator()

        layout = QVBoxLayout()


        controls = QHBoxLayout()
        self.fs_input = QLineEdit("1000")
        self.duration_input = QLineEdit("1")

        controls.addWidget(QLabel("duration (с):"))
        controls.addWidget(self.duration_input)

        self.button = QPushButton("Построить")
        self.button.clicked.connect(self.create)

        self.canvas = None

        layout.addLayout(controls)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def create(self):
        fs = int(self.fs_input.text())
        duration = float(self.duration_input.text())
        self.generator.update_params(fs, duration)

        freqs_to_test = [1, 2, 4, 8]
        last_fig = None

        for f in freqs_to_test:
            #  синус
            sig = self.generator.generate_sine(f)
            fr, sp = SpectrumAnalyzer.compute_fft(sig, fs)

            Plotter.save_signal(
                self.generator.t, sig,
                f"Гармонический сигнал - {f} Гц",
                f"signal_garm_{f}.png"
            )
            Plotter.save_spectrum(
                fr, sp,
                f"Гармонический {f} Гц",
                f"spectrum_garm_{f}.png"
            )

            last_fig = Plotter.make_combined_plot(
                self.generator.t, sig, fr, sp,
                f"Синус {f} Гц"
            )

            # меандр
            sig = self.generator.generate_square(f)
            fr, sp = SpectrumAnalyzer.compute_fft(sig, fs)

            Plotter.save_signal(
                self.generator.t, sig,
                f"Меандр {f} Гц",
                f"signal_square_{f}.png",
                True
            )
            Plotter.save_spectrum(
                fr, sp,
                f"Меандр {f} Гц",
                f"spectrum_square_{f}.png"
            )

            # last_fig = Plotter.make_combined_plot(
            #     self.generator.t, sig, fr, sp,
            #     f"Меандр {f} Гц",
            #     True
            # )

        if self.canvas:
            self.layout().removeWidget(self.canvas)
            self.canvas.deleteLater()

        self.canvas = FigureCanvas(last_fig)
        self.layout().addWidget(self.canvas)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
