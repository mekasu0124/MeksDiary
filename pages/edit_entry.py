from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QTextEdit

from modules.styles import get_setup_font
from modules.styles import get_frame_style
from modules.styles import get_label_style
from modules.styles import get_button_style
from modules.styles import get_combo_style
from modules.styles import get_line_style
from modules.styles import get_text_line_style
from modules.styles import get_error_style
from modules.styles import get_error_label_style
from modules.styles import set_background_image

from data.database import get_combo_list
from data.database import update_db


class EditEntry(QMainWindow):
    def __init__(self, window_manager):
        super(EditEntry, self).__init__()

        self.window_manager = window_manager
        self.small_font = get_setup_font()
        self.frame_style = get_frame_style()
        self.label_style = get_label_style()
        self.button_style = get_button_style()
        self.line_style = get_line_style()
        self.line_text_style = get_text_line_style()
        self.combo_style = get_combo_style()
        self.error_style = get_error_style()
        self.error_label_style = get_error_label_style()

        self.combo_items = get_combo_list()
        self.item = ""

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

        self.label = QLabel("Select An Entry To Edit",self.frame)
        self.label.setGeometry(150,20,250,50)
        self.label.setStyleSheet(self.label_style)
        self.label.setFont(self.small_font)
        self.label.setWordWrap(False)
        self.label.setAlignment(Qt.AlignCenter)

        add_items = []

        for item in self.combo_items:
            id, title, date, details = item.split(" - ")

            text = f"{id} - {title} - {date}"
            add_items.append(text)

        self.combo = QComboBox(self.frame)
        self.combo.setGeometry(50,70,460,80)
        self.combo.setStyleSheet(self.combo_style)
        self.combo.setFont(self.small_font)
        self.combo.addItem("Select One")
        self.combo.addItems(add_items)

        self.button = QPushButton("Edit Entry", self.frame)
        self.button.setGeometry(100,450,350,50)
        self.button.setStyleSheet(self.button_style)
        self.button.setFont(self.small_font)
        self.button.clicked.connect(self.get_item_index)
        self.button.show()

        self.button = QPushButton("Back", self.frame)
        self.button.setGeometry(100,530,350,50)
        self.button.setStyleSheet(self.button_style)
        self.button.setFont(self.small_font)
        self.button.clicked.connect(self.back_button)
        self.button.show()

    def get_item_index(self):
        desired_item = self.combo.currentText()

        for item in self.combo_items:
            if item.startswith(desired_item):
                self.item = item
                break

        self.show_next_frame()

    def show_next_frame(self):
        self.frame.hide()

        self.frame2 = QFrame(self)
        self.frame2.setGeometry(20,20,560,760)
        self.frame2.setStyleSheet(self.frame_style)
        self.frame2.show()

        id, title, date, details = self.item.split(" - ")

        self.label = QLabel(f"Title For: {date}", self.frame2)
        self.label.setGeometry(150,20,250,50)
        self.label.setStyleSheet(self.label_style)
        self.label.setFont(self.small_font)
        self.label.setWordWrap(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.show()

        self.title = QLineEdit(self.frame2)
        self.title.setGeometry(50,70,460,80)
        self.title.setStyleSheet(self.line_style)
        self.title.setFont(self.small_font)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setText(title)
        self.title.show()

        self.label = QLabel(f"Entry For: {date}",self.frame2)
        self.label.setGeometry(150,160,250,50)
        self.label.setStyleSheet(self.label_style)
        self.label.setFont(self.small_font)
        self.label.setWordWrap(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.show()

        self.details = QTextEdit(self.frame2)
        self.details.setGeometry(50,210,460,340)
        self.details.setStyleSheet(self.line_text_style)
        self.details.setFont(self.small_font)
        self.details.setText(details)
        self.details.show()

        self.error_label = QLabel("Database Failed To Update. Contact Support.", self.frame2)
        self.error_label.setGeometry(50,600,460,50)
        self.error_label.setStyleSheet(self.error_label_style)
        self.error_label.setFont(self.small_font)
        self.error_label.setWordWrap(False)
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.hide()

        self.button1 = QPushButton("Submit", self.frame2)
        self.button1.setGeometry(50,640,460,50)
        self.button1.setStyleSheet(self.button_style)
        self.button1.setFont(self.small_font)
        self.button1.clicked.connect(self.check_inputs)
        self.button1.show()

        self.button = QPushButton("Back", self.frame2)
        self.button.setGeometry(50,700,460,50)
        self.button.setStyleSheet(self.button_style)
        self.button.setFont(self.small_font)
        self.button.clicked.connect(self.back_button)
        self.button.show()

    def check_inputs(self):
        id, title, date, details = self.item.split(" - ")

        try:
            today = datetime.now().strftime("%m/%d/%Y %H:%M:%S %p").lower()
            check_update = update_db(id, self.title.text(), today, self.details.toPlainText())

            if check_update:
                self.window_manager.close_window()
            else:
                self.error_label.show()

                self.timer = QTimer()
                self.timer.setInterval(600)
                self.timer.timeout.connect(self.reset_screen)
                self.timer.start()

        except Exception as e:
            raise e

    def back_button(self):
        self.window_manager.close_window()
        
    def reset_screen(self):
        self.timer.stop()

        self.title.clear()
        self.details.clear()

        self.title.setStyleSheet(self.label_style)
        self.details.setStyleSheet(self.line_style)

        self.show_next_frame()