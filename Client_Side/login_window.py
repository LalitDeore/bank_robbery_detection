from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import webbrowser
import requests
import json
from settings_window import SettingsWindow

# LoginWindow class that manages login and opening the setting window
class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi('UI/login_window.ui', self)

        self.register_button.clicked.connect(self.go_to_register_page)
        self.login_button.clicked.connect(self.go_to_settings_window)

        self.show()

    def go_to_register_page(self):
        print("go to register page")
    
    def go_to_settings_window(self):
        self.settings_window = SettingsWindow(1)
        self.settings_window.displayInfo()
        self.close()
        