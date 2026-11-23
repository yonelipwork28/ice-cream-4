import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QWidget


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Me")

        title = QLabel("Welcome to Card of", self)
        title.setGeometry(50, 20, 300, 60)
        title.setStyleSheet("font-size: 30px;")

        name = QLabel("Yonatan Lipshitz", self)
        name.setGeometry(50, 60, 300, 60)
        name.setStyleSheet("font-size: 30px; font-weight: bold;")

        mail = QLabel("yonelip27@gmail.com", self)
        mail.setGeometry(50, 140, 300, 30)
        mail.setStyleSheet("font-size: 20px;")

        linkedin = QLabel(self)
        linkedin.setGeometry(50, 180, 300, 30)
        linkedin.setText('<a href="https://il.linkedin.com/">My Linkedin</a>')
        linkedin.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        linkedin.setOpenExternalLinks(True)
        linkedin.setStyleSheet("font-size: 20px;")

        image_path = os.path.join(os.path.dirname(__file__), "spongbob.jpeg")
        image = QLabel(self)
        image.setGeometry(20, 260, 300, 300)
        if os.path.exists(image_path):
            image.setPixmap(QPixmap(image_path).scaled(300, 300))


if __name__ == "__main__":
    app = QApplication.instance() or QApplication([])
    window = AboutWindow()
    window.show()
    app.exec()
