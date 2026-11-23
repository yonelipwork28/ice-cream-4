from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('About Me')

        self.Title_welcom = QLabel('Welcome to Card of' , self)
        self.Title_welcom.setGeometry(50,20,300,60)
        self.Title_welcom.setStyleSheet("font-size: 30px ;")
        self.my_name = QLabel('Yonatan Lipshitz' , self)
        self.my_name.setGeometry(50,60,300,60)
        self.my_name.setStyleSheet("font-size: 30px ; font-Weight: bold; ")


        self.my_mail = QLabel('yonelip27@gmail.com' , self)
        self.my_mail.setGeometry(50,140,300,30)
        self.my_mail.setStyleSheet("font-size: 20px ;")

        self.my_Linkedin = QLabel(self)
        self.my_Linkedin.setGeometry(50,180,300,30)
        self.my_Linkedin.setText('<a href="https://il.linkedin.com/">My Linkedin</a>')
        self.my_Linkedin.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.my_Linkedin.setOpenExternalLinks(True)
        self.my_Linkedin.setStyleSheet("font-size: 20px ;")

        img_path = os.path.join(os.path.dirname(__file__), 'spongbob.jpeg')
        image = QPixmap(img_path).scaled(300,300)
        self.my_picture=QLabel(self)
        self.my_picture.setGeometry(20,260,300,300)
        self.my_picture.setPixmap(image)
        
        
if __name__=='__main__':
    app= QApplication()
    window = AboutWindow()
    window.show()
    app.exec()