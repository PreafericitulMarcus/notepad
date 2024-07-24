
from PyQt6.QtWidgets import QApplication, QTextEdit
from PyQt6.QtGui import QClipboard, QKeyEvent
from PyQt6.QtCore import Qt

class PlainTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

    def paste(self):
        clipboard = QApplication.clipboard()
        plain_text = clipboard.text(QClipboard.Mode.Clipboard)
        cursor = self.textCursor()
        cursor.insertText(plain_text)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_V and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            self.paste()
            return
        super().keyPressEvent(event)