from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFrame
)
from PySide6.QtGui import QFont, QPixmap, QLinearGradient, QPalette, QColor, QBrush
from PySide6.QtCore import Qt, QSize
import sys

class WeatherUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather UI")
        self.setFixedSize(800, 500)
        self.setStyleSheet("background-color: #2c3e50; border-radius: 20px;")

        layout = QHBoxLayout(self)

        # Left gradient panel
        left_panel = QFrame()
        left_panel.setFixedSize(400, 500)
        left_panel.setStyleSheet("""
            QFrame {
                border-top-left-radius: 20px;
                border-bottom-left-radius: 20px;
                background-image: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                                                  stop:0 #6dd5fa, stop:1 #2980b9);
            }
        """)
        left_layout = QVBoxLayout(left_panel)
        left_layout.setAlignment(Qt.AlignTop)
        left_layout.setContentsMargins(30, 30, 30, 30)

        date_label = QLabel("Tuesday\n20 Jun 2022")
        date_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        location_label = QLabel("Biarritz, FR")
        location_label.setStyleSheet("color: white; font-size: 14px;")

        icon = QLabel()
        pixmap = QPixmap("sun.png").scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon.setPixmap(pixmap)

        temp_label = QLabel("29 °C")
        temp_label.setStyleSheet("color: white; font-size: 36px; font-weight: bold;")

        condition_label = QLabel("Sunny")
        condition_label.setStyleSheet("color: white; font-size: 18px;")

        for w in [date_label, location_label, icon, temp_label, condition_label]:
            left_layout.addWidget(w)
            left_layout.addSpacing(10)

        # Right panel
        right_panel = QFrame()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setAlignment(Qt.AlignTop)
        right_layout.setContentsMargins(30, 30, 30, 30)

        # Info rows
        info_layout = QVBoxLayout()
        for label, value in [("PRECIPITATION", "0%"), ("HUMIDITY", "42%"), ("WIND", "3 km/h")]:
            row = QHBoxLayout()
            lbl = QLabel(label)
            lbl.setStyleSheet("color: white; font-size: 14px; font-weight: bold;")
            val = QLabel(value)
            val.setStyleSheet("color: white; font-size: 14px;")
            row.addWidget(lbl)
            row.addStretch()
            row.addWidget(val)
            info_layout.addLayout(row)
            info_layout.addSpacing(5)
        right_layout.addLayout(info_layout)
        right_layout.addSpacing(20)

        # Forecast row
        forecast_layout = QHBoxLayout()
        for day, temp, icon_file in [("Tue", "30 °C", "sun.png"),
                                     ("Wed", "22 °C", "cloud.png"),
                                     ("Thu", "06 °C", "rain.png"),
                                     ("Fri", "26 °C", "sun.png")]:
            box = QVBoxLayout()
            icon = QLabel()
            pix = QPixmap(icon_file).scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon.setPixmap(pix)
            day_lbl = QLabel(day)
            temp_lbl = QLabel(temp)
            for el in [day_lbl, temp_lbl]:
                el.setStyleSheet("color: white; font-size: 12px;")
                el.setAlignment(Qt.AlignCenter)
            box.addWidget(icon, alignment=Qt.AlignCenter)
            box.addWidget(day_lbl)
            box.addWidget(temp_lbl)
            forecast_layout.addLayout(box)

        right_layout.addLayout(forecast_layout)
        right_layout.addSpacing(30)

        # Change location button
        change_btn = QPushButton("Change Location")
        change_btn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 14px;
                border-radius: 10px;
                padding: 10px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                            stop:0 #6dd5fa, stop:1 #2980b9);
            }
        """)
        right_layout.addWidget(change_btn)

        layout.addWidget(left_panel)
        layout.addWidget(right_panel)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherUI()
    window.show()
    sys.exit(app.exec())