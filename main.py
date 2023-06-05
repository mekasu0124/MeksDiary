import sys
import json

from PySide6.QtWidgets import QApplication

from pages.home import Home
from pages.setup import Setup

from modules.manager import WindowManager

from server.createDb import create_db

if __name__ == '__main__':
    create_db()
    app = QApplication(sys.argv)
    window_manager = WindowManager()

    with open('./server/config.json','r',encoding="utf-8-sig") as f:
        data = json.load(f)

        if data["setup"] == "True":
            window = Home(window_manager)
        else:
            window = Setup(window_manager)

        window_manager.open_window(window)

    sys.exit(app.exec())