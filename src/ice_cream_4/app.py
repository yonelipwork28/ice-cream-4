import csv
import sys
from pathlib import Path

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from .about import AboutWindow


class IceCreamSalesWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("IceCreamSalesWindow")
        self.setWindowTitle("ניתוח מכירות גלידה")
        self.resize(1100, 760)
        self.setMinimumSize(780, 580)
        self.selected_file_path = ""
        self.about_window = AboutWindow()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 24, 28, 24)
        layout.setSpacing(16)

        title = QLabel("ניתוח מכירות גלידה")
        title.setObjectName("pageTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel("בחירת קובץ נתונים, הצגת הקשר בין הטמפרטורה להכנסות ושמירת הגרף")
        subtitle.setObjectName("pageSubtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setWordWrap(True)

        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(12)
        actions_layout.addStretch(1)

        self.open_file_button = QPushButton("בחירת קובץ CSV")
        self.open_file_button.setObjectName("primaryButton")
        self.open_file_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.open_file_button.clicked.connect(self.select_csv_file)

        self.about_button = QPushButton("About")
        self.about_button.setObjectName("secondaryButton")
        self.about_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.about_button.clicked.connect(self.about_window.show)

        actions_layout.addWidget(self.open_file_button)
        actions_layout.addWidget(self.about_button)
        actions_layout.addStretch(1)

        self.file_status = QLabel("מציג נתוני תצוגה לדוגמה")
        self.file_status.setObjectName("fileStatus")
        self.file_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.figure = Figure(figsize=(9, 5), facecolor="#ffffff")
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setObjectName("plotCanvas")
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.toolbar.setObjectName("plotToolbar")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addLayout(actions_layout)
        layout.addWidget(self.file_status)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas, 1)

        stylesheet_path = Path(__file__).with_name("ice cream graph.qss")
        if not stylesheet_path.exists():
            stylesheet_path = Path(__file__).parents[2] / "ice cream graph.qss"
        if stylesheet_path.exists():
            with stylesheet_path.open(encoding="utf-8") as stylesheet_file:
                self.setStyleSheet(stylesheet_file.read())

        self.draw_graph(
            temperatures=[10, 15, 20, 25, 30, 35, 40],
            revenues=[250, 350, 470, 590, 690, 810, 920],
        )

    def draw_graph(self, temperatures, revenues):
        self.axes.clear()
        self.axes.bar(temperatures, revenues, width=1.2, color="#4263eb")
        self.axes.set_title("Ice Cream Sales vs. Temperature", fontsize=15, pad=14)
        self.axes.set_xlabel("Temperature (°C)", labelpad=10)
        self.axes.set_ylabel("Ice Cream Sales Revenue", labelpad=10)
        self.axes.spines["top"].set_visible(False)
        self.axes.spines["right"].set_visible(False)
        self.axes.grid(True, color="#e8edf5", linewidth=0.8)
        self.axes.set_axisbelow(True)
        self.figure.tight_layout()
        self.canvas.draw_idle()

    def select_csv_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "בחירת קובץ נתונים",
            "",
            "CSV files (*.csv)",
        )
        if not file_path:
            return

        try:
            temperatures = []
            revenues = []
            with open(file_path, newline="", encoding="utf-8-sig") as csv_file:
                rows = csv.DictReader(csv_file)
                for row in rows:
                    temperatures.append(float(row["Temperature"]))
                    revenues.append(float(row["Revenue"]))
        except (KeyError, TypeError, ValueError, OSError) as error:
            self.file_status.setText(f"שגיאה בקריאת הקובץ: {error}")
            return

        if not temperatures:
            self.file_status.setText("הקובץ אינו מכיל נתונים")
            return

        self.selected_file_path = file_path
        self.file_status.setText(f"קובץ נבחר: {Path(file_path).name}")
        self.draw_graph(temperatures, revenues)


def main() -> None:
    app = QApplication.instance() or QApplication(sys.argv)
    window = IceCreamSalesWindow()
    window.show()
    sys.exit(app.exec())
