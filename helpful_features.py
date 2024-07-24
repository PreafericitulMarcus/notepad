from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QMessageBox,
)


class FindDialog(QDialog):
    def __init__(self, main_window=None):
        super().__init__(main_window)
        self.setWindowTitle("Find")
        self.setGeometry(100, 100, 300, 100)

        self.layout = QVBoxLayout()

        self.label = QLabel("Find what:")
        self.layout.addWidget(self.label)

        self.find_input = QLineEdit()
        self.layout.addWidget(self.find_input)

        self.find_button = QPushButton("Find")
        self.find_button.clicked.connect(self.find_text)
        self.layout.addWidget(self.find_button)

        self.setLayout(self.layout)

        self.main_window = main_window

    def find_text(self):
        text = self.find_input.text()
        if text:
            cursor = self.main_window.text_edit.textCursor()
            document = self.main_window.text_edit.document()

            cursor = document.find(text, cursor)
            if cursor.isNull():
                cursor = document.find(text)
                

            if cursor.isNull():
                QMessageBox.information(self, "Notepad", f"'{text}' not found")
            else:
                self.main_window.text_edit.setTextCursor(cursor)
        else:
            QMessageBox.warning(self, "Notepad", "Please enter a text to find")
