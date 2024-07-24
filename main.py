import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class Notepad(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Notepad()
    window.resize(800, 450)
    window.show()
    sys.exit(app.exec())
