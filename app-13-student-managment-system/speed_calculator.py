from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox
import sys


class AverageSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # create widgets
        distance_label = QLabel("Distance:")
        self.distance_box = QLineEdit()
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Metric (km)", "Imperial (miles)"])

        time_label = QLabel("Time (hours):")
        self.time_box = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)
        average_speed_label = QLabel("Average Speed:")
        self.output_label = QLabel("")

        # add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_box, 0, 1)
        grid.addWidget(self.combo_box, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_box, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(average_speed_label, 3, 0)
        grid.addWidget(self.output_label, 3, 1)

        self.setLayout(grid)

    def calculate(self):
        if self.combo_box.currentText() == "Metric (km)":
            speed = float(self.distance_box.text()) / float(self.time_box.text())
            self.output_label.setText(f"{speed} km/h")
        if self.combo_box.currentText() == "Imperial (miles)":
            speed = float(self.distance_box.text()) / float(self.time_box.text())
            self.output_label.setText(f"{speed} MPH")


app = QApplication(sys.argv)
speed_calculator = AverageSpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())

