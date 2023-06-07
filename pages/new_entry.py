from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QTextEdit
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton

from modules.styles import get_font
from modules.styles import get_setup_font
from modules.styles import get_frame_style
from modules.styles import get_label_style
from modules.styles import get_button_style
from modules.styles import get_line_style
from modules.styles import get_error_style
from modules.styles import get_text_line_style
from modules.styles import get_success_style
from modules.styles import get_error_label_style
from modules.styles import set_background_image

from data.database import add_to_db


class NewEntry(QMainWindow):
    def __init__(self, window_manager):
        super(NewEntry, self).__init__()

        self.window_manager = window_manager
        self.small_font = get_setup_font()
        self.regular_font = get_font()
        self.frame_style = get_frame_style()
        self.label_style = get_label_style()
        self.button_style = get_button_style()
        self.line_style = get_line_style()
        self.line_text_style = get_text_line_style()
        self.error_style = get_error_style()
        self.success_style = get_success_style()
        self.error_label_style = get_error_label_style()

        self.setStyleSheet(set_background_image())
        self.setWindowTitle("Mek's Diary - New Entry")
        self.UiComponents()
        self.setMinimumHeight(800)
        self.setMinimumWidth(600)
        self.show()

    def UiComponents(self):
        self.frame = QFrame(self)
        self.frame.setGeometry(20,20,560,760)
        self.frame.setStyleSheet(self.frame_style)

        self.label = QLabel("Title",self.frame)
        self.label.setGeometry(150,20,250,50)
        self.label.setStyleSheet(self.label_style)
        self.label.setFont(self.regular_font)
        self.label.setWordWrap(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.title = QLineEdit(self.frame)
        self.title.setGeometry(50,70,460,80)
        self.title.setStyleSheet(self.line_style)
        self.title.setFont(self.regular_font)
        self.title.setAlignment(Qt.AlignCenter)

        self.label = QLabel("Entry",self.frame)
        self.label.setGeometry(150,160,250,50)
        self.label.setStyleSheet(self.label_style)
        self.label.setFont(self.regular_font)
        self.label.setWordWrap(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.details = QTextEdit(self.frame)
        self.details.setGeometry(50,210,460,340)
        self.details.setStyleSheet(self.line_text_style)
        self.details.setFont(self.small_font)

        self.success_label = QLabel("Your Submission Has Been Saved!",self.frame)
        self.success_label.setGeometry(50,580,460,50)
        self.success_label.setStyleSheet(self.success_style)
        self.success_label.setWordWrap(False)
        self.success_label.setFont(self.regular_font)
        self.success_label.setAlignment(Qt.AlignCenter)
        self.success_label.hide()

        self.error_label = QLabel("Your Submission Failed To Submit. Contact Support.", self.frame)
        self.error_label.setGeometry(50,580,460,50)
        self.error_label.setStyleSheet(self.error_label_style)
        self.error_label.setWordWrap(False)
        self.error_label.setFont(self.regular_font)
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.hide()

        self.button = QPushButton("Submit", self.frame)
        self.button.setGeometry(50,640,460,50)
        self.button.setStyleSheet(self.button_style)
        self.button.setFont(self.regular_font)
        self.button.clicked.connect(self.check_inputs)

        self.button = QPushButton("Back", self.frame)
        self.button.setGeometry(50,700,460,50)
        self.button.setStyleSheet(self.button_style)
        self.button.setFont(self.regular_font)
        self.button.clicked.connect(self.back_button)
        
    def check_inputs(self):
        if len(self.title.text()) > 5:
            if len(self.details.toPlainText()) > 5:
                today = datetime.now().strftime("%m/%d/%Y %H:%M:%S %p").lower()
                write_check = add_to_db(self.title.text(), today, self.details.toPlainText())

                if write_check:
                    self.success_label.show()

                    self.timer = QTimer()
                    self.timer.setInterval(600)
                    self.timer.timeout.connect(self.previous_screen)
                    self.timer.start()
                else:
                    raise
            else:
                self.details.setStyleSheet(self.error_style)

                self.timer = QTimer()
                self.timer.setInterval(600)
                self.timer.timeout.connect(self.reset_screen)
                self.timer.start()
        else:
            self.title.setStyleSheet(self.error_style)

            self.timer = QTimer()
            self.timer.setInterval(600)
            self.timer.timeout.connect(self.reset_screen)
            self.timer.start()

    def back_button(self):
        self.window_manager.close_window()
        
    def reset_screen(self):
        self.timer.stop()

        self.title.clear()
        self.details.clear()

        self.title.setStyleSheet(self.label_style)
        self.details.setStyleSheet(self.line_style)
    
    def previous_screen(self):
        self.timer.stop()

        self.window_manager.close_window()