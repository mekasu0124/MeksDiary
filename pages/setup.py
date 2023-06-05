import json
import sys
import re 

from PySide6.QtCore import Qt
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton

from modules.styles import get_font
from modules.styles import get_setup_font
from modules.styles import get_frame_style
from modules.styles import get_label_style
from modules.styles import get_button_style
from modules.styles import get_line_style
from modules.styles import get_error_style
from modules.styles import set_background_image

from pages.home import Home

class Setup(QMainWindow):
    def __init__(self, window_manager):
        super(Setup, self).__init__()

        self.window_manager = window_manager
        self.setup_font = get_setup_font()
        self.regular_font = get_font()
        self.frame_style = get_frame_style()
        self.label_style = get_label_style()
        self.button_style = get_button_style()
        self.line_style = get_line_style()
        self.error_style = get_error_style()

        self.setStyleSheet(set_background_image())
        self.setWindowTitle("Mek's Diary - Setup")
        self.UiComponents()
        self.setMinimumHeight(800)
        self.setMinimumWidth(600)
        self.show()

    def UiComponents(self):
        self.frame = QFrame(self)
        self.frame.setGeometry(20,20,560,760)
        self.frame.setStyleSheet(self.frame_style)

        label_parts = [
            "Welcome To Mek's Dairy. This application is designed to be",
            "used by one person at the time. This app does not share your",
            "information, diary entries, or other information you submit",
            "to anyone, anywhere, at any time. This program is setup to",
            "locally host the database that holds your diary entries. What",
            "does this mean? This means that the database is created within",
            "the file directory of the application itself and any information",
            "that is shared is information that you willingly posted/shared yourself.",
            "The name and email that is provided to this application is locally stored",
            "within the local json file itself and this application is not setup to share",
            "that information with anyone unless you, the user, willingly does so through",
            "the share options that are setup within this application. When you are ready",
            "to begin the setup, click the \"Begin Setup\" button or click the \"Exit\" button",
            "to exit the application."
        ]

        self.label = QLabel(' '.join(label_parts),self.frame)
        self.label.setGeometry(10,50,540,480)
        self.label.setStyleSheet(self.label_style)
        self.label.setFont(self.setup_font)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton("Begin Setup",self.frame)
        self.button.setGeometry(10,620,540,50)
        self.button.setStyleSheet(self.button_style)
        self.button.setFont(self.setup_font)
        self.button.clicked.connect(self.show_next_frame)

        self.button = QPushButton("Exit",self.frame)
        self.button.setGeometry(10,690,540,50)
        self.button.setStyleSheet(self.button_style)
        self.button.setFont(self.setup_font)
        self.button.clicked.connect(self.exit_button)

    def show_next_frame(self):
        self.frame.hide()

        self.frame2 = QFrame(self)
        self.frame2.setGeometry(20,20,560,760)
        self.frame2.setStyleSheet(self.frame_style)
        self.frame2.show()

        self.label = QLabel("Your Name",self.frame2)
        self.label.setGeometry(150,50,250,50)
        self.label.setStyleSheet(self.label_style)
        self.label.setFont(self.regular_font)
        self.label.setWordWrap(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.show()

        self.user_name = QLineEdit(self.frame2)
        self.user_name.setGeometry(100,100,350,80)
        self.user_name.setStyleSheet(self.line_style)
        self.user_name.setFont(self.regular_font)
        self.user_name.setAlignment(Qt.AlignCenter)
        self.user_name.show()

        self.label = QLabel("Your Email",self.frame2)
        self.label.setGeometry(150,250,250,50)
        self.label.setStyleSheet(self.label_style)
        self.label.setFont(self.regular_font)
        self.label.setWordWrap(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.show()

        self.user_email = QLineEdit(self.frame2)
        self.user_email.setGeometry(100,300,350,80)
        self.user_email.setStyleSheet(self.line_style)
        self.user_email.setFont(self.regular_font)
        self.user_email.setAlignment(Qt.AlignCenter)
        self.user_email.show()

        self.button = QPushButton("Complete Setup", self.frame2)
        self.button.setGeometry(100,450,350,50)
        self.button.setStyleSheet(self.button_style)
        self.button.setFont(self.regular_font)
        self.button.clicked.connect(self.check_inputs)
        self.button.show()

        self.button = QPushButton("Exit Setup", self.frame2)
        self.button.setGeometry(100,530,350,50)
        self.button.setStyleSheet(self.button_style)
        self.button.setFont(self.regular_font)
        self.button.clicked.connect(self.exit_button)
        self.button.show()

    def exit_button(self):
        sys.exit()

    def check_inputs(self):
        if len(self.user_name.text()) > 5:
            if not self.check(self.user_email.text()):
                self.user_email.setStyleSheet(self.error_style)

                self.timer = QTimer()
                self.timer.setInterval(600)
                self.timer.timeout.connect(self.reset_screen)
                self.timer.start()
            else:
                write_check = self.write_to_json(self.user_name.text(), self.user_email.text())

                if write_check:
                    self.window_manager.open_window(Home(self.window_manager))
                    print("Loading Home Page")
                else:
                    raise
        else:
            self.user_name.setStyleSheet(self.error_style)

            self.timer = QTimer()
            self.timer.setInterval(600)
            self.timer.timeout.connect(self.reset_screen)
            self.timer.start()
        
        

    def check(self,email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if re.search(regex, email):
            return True
        else:
            return False
        
    def reset_screen(self):
        self.timer.stop()

        self.user_name.setStyleSheet(self.label_style)
        self.user_email.setStyleSheet(self.line_style)

        self.user_name.clear()
        self.user_email.clear()

        self.show_next_frame()

    def write_to_json(self, name, email):
        with open("./server/config.json",'r',encoding="utf-8-sig") as f:
            data = json.load(f)

            data["setup"] = "True"

            data["profile"] = {
                "name": name,
                "email": email
            }

            try:
                with open("./server/config.json",'w+',encoding="utf-8-sig") as new:
                    data = json.dump(data, new, indent=4)

                return True
            except Exception as e:
                raise e