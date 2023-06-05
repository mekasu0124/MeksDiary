import json
import sys

from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton

from modules.styles import get_font
from modules.styles import get_frame_style
from modules.styles import get_label_style
from modules.styles import get_button_style
from modules.styles import set_background_image

from pages.new_entry import NewEntry
from pages.edit_entry import EditEntry
from pages.share_entry import ShareEntry

class Home(QMainWindow):
    def __init__(self, window_manager):
        super(Home, self).__init__()

        self.window_manager = window_manager
        self.regular_font = get_font()
        self.frame_style = get_frame_style()
        self.label_style = get_label_style()
        self.button_style = get_button_style()
        self.today = datetime.now().strftime("%m/%d/%Y %H:%M:%S %p").lower()

        with open("./server/config.json",'r',encoding="utf-8-sig") as f:
            data = json.load(f)

            self.name = data["profile"]["name"].split(" ")[0]

        self.setStyleSheet(set_background_image())
        self.setWindowTitle("Mek's Diary - Home")
        self.UiComponents()
        self.setMinimumHeight(800)
        self.setMinimumWidth(600)
        self.show()

    def UiComponents(self):
        self.frame = QFrame(self)
        self.frame.setGeometry(20,20,560,760)
        self.frame.setStyleSheet(self.frame_style)

        self.label = QLabel(f"Hi, {self.name}! It is {self.today}. What would you like to do?", self.frame)
        self.label.setGeometry(10,20,520,100)
        self.label.setStyleSheet(self.label_style)
        self.label.setFont(self.regular_font)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton("New Entry", self.frame)
        self.button.setGeometry(60,185,450,80)
        self.button.setStyleSheet(self.button_style)
        self.button.setFont(self.regular_font)
        self.button.clicked.connect(self.new_entry)

        self.button = QPushButton("Edit Entry", self.frame)
        self.button.setGeometry(60,340,450,80)
        self.button.setStyleSheet(self.button_style)
        self.button.setFont(self.regular_font)
        self.button.clicked.connect(self.edit_entry)

        self.button = QPushButton("Share Entry", self.frame)
        self.button.setGeometry(60,495,450,80)
        self.button.setStyleSheet(self.button_style)
        self.button.setFont(self.regular_font)
        # self.button.clicked.connect(self.share_entry)
        self.button.setEnabled(False)

        self.button = QPushButton("Exit Program", self.frame)
        self.button.setGeometry(60,650,450,80)
        self.button.setStyleSheet(self.button_style)
        self.button.setFont(self.regular_font)
        self.button.clicked.connect(self.exit_button)

    def new_entry(self):
        self.window_manager.open_window(NewEntry(self.window_manager))

    def edit_entry(self):
        self.window_manager.open_window(EditEntry(self.window_manager))

    def share_entry(self):
        self.window_manager.open_window(ShareEntry(self.window_manager))

    def exit_button(self):
        sys.exit()