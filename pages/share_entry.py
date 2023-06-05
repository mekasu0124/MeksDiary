from PySide6.QtCore import Qt
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QComboBox

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

"""
This page is still under construction as I am not sure how
to use PySide6 to generate a text file and then prompt a user
on where to save said file. Once I am able to get this completed,
the share button will be enabled!
"""

class ShareEntry(QMainWindow):
    def __init__(self, window_manager):
        super(ShareEntry, self).__init__()

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

        self.label = QLabel("Select An Entry To Share",self.frame)
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

        self.create_text_file()

    def create_text_file(self):
        id, title, date, details = self.item.split(" - ")

        file_name = title + " " + date

        file = QFile(file_name)