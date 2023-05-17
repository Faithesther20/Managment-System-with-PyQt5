import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QLabel, QProgressBar
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer


class SplashScreen(QDialog):
    def __init__(self):
        super(SplashScreen, self).__init__()
        loadUi("splashScreen.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.label = self.findChild(QLabel, "label")
        pixmap = QPixmap("./images/gradientBg.jpg")
        self.progress = self.findChild(QProgressBar, 'progressBar')
        self.label.setPixmap(pixmap)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)  # Update progress every 100 milliseconds

    def update_progress(self):
        current_value = self.progress.value()
        if current_value < self.progress.maximum():
            self.progress.setValue(current_value + 4)
        else:
            self.timer.stop()
            self.close()
            main_page = MainPage()
            main_page.exec_()


class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi("main.ui", self)
        self.signInBtn = self.findChild(QPushButton, "signInBtn")
        self.registerBtn = self.findChild(QPushButton, "registerBtn")
        self.signInBtn.clicked.connect(self.gotoSignIn)
        self.registerBtn.clicked.connect(self.gotoRegister)
        self.show()
    def gotoSignIn(self):
        self.hide()
        sign_in_page = SignInPage()
        sign_in_page.exec_()

    def gotoRegister(self):
        self.hide()
        register_page = RegisterPage()
        register_page.exec_()


class SignInPage(QDialog):
    def __init__(self):
        super(SignInPage, self).__init__()
        loadUi("signIn.ui", self)


class RegisterPage(QDialog):
    def __init__(self):
        super(RegisterPage, self).__init__()
        loadUi("register.ui", self)


app = QApplication(sys.argv)
window = SplashScreen()
window.show()
app.setQuitOnLastWindowClosed(False)
app.exec_()
