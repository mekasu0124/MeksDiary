from PySide6.QtGui import QFont, QFontDatabase

def set_custom_font():
    new_font = QFontDatabase.addApplicationFont("./fonts/ShadowsIntoLight-Regular.ttf")

    if new_font <0:
        raise

    font_family = QFontDatabase.applicationFontFamilies(new_font)
    return font_family[0]


def get_font():
    font = QFont()

    font.setFamily(set_custom_font())
    font.setBold(True)
    font.setItalic(True)
    font.setPointSize(20)

    return font

def get_setup_font():
    font = QFont()
    font.setFamily(set_custom_font())
    font.setBold(True)
    font.setItalic(True)
    font.setPointSize(15)

    return font

def get_frame_style():
    return "border: 2px solid blue;\
                border-radius: 20px;\
                    background: transparent;"

def get_label_style():
    return "border: none;\
                color: blue;\
                    background: transparent;"
def get_button_style():
    return "color: blue;\
                background: transparent;"

def get_line_style():
    return "border: 2px solid blue;\
                border-radius: 20px;\
                    background-color: transparent;\
                        color: blue;"

def get_text_line_style():
    return "border: 2px solid blue;\
                border-radius: 10px;\
                    background-color: transparent;\
                        color: blue;\
                            padding: 10px;"

def get_error_style():
    return "border: 2px solid red;\
                background-color: yellow;"

def get_error_label_style():
    return "border: 2px solid red;\
                border-radius: 20px;\
                    color: red;"

def get_combo_style():
    return "border: 2px solid blue;\
                border-radius: 10px;\
                    background-color: transparent;\
                        color: blue;"

def set_background_image():
    return "background-image: url('./images/bg_image.jpg');\
                background-repeat: no-repeat;\
                    background-position: center;"