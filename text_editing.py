from PyQt6.QtCore import Qt

class TextEditing:
    def __init__(self, main_window):
        self.main_window = main_window

    def move_cursor_to_end_of_line(self):
        cursor = self.main_window.text_edit.textCursor()
        cursor.movePosition(cursor.MoveOperation.EndOfLine)
        self.main_window.text_edit.setTextCursor(cursor)

    def add_line_above(self):
        cursor = self.main_window.text_edit.textCursor()
        cursor.movePosition(cursor.MoveOperation.StartOfLine)
        cursor.insertText("\n")
        cursor.movePosition(cursor.MoveOperation.Up)
        self.main_window.text_edit.setTextCursor(cursor)

    def add_line_below(self):
        cursor = self.main_window.text_edit.textCursor()
        cursor.movePosition(cursor.MoveOperation.EndOfLine)
        cursor.insertText("\n")
        self.main_window.text_edit.setTextCursor(cursor)

    def center_text(self):
        cursor = self.main_window.text_edit.textCursor()
        block_format = cursor.blockFormat()
        block_format.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cursor.setBlockFormat(block_format)
        self.main_window.text_edit.setTextCursor(cursor)

    def right_text(self):
        cursor = self.main_window.text_edit.textCursor()
        block_format = cursor.blockFormat()
        block_format.setAlignment(Qt.AlignmentFlag.AlignRight)
        cursor.setBlockFormat(block_format)
        self.main_window.text_edit.setTextCursor(cursor)

    def left_text(self):
        cursor = self.main_window.text_edit.textCursor()
        block_format = cursor.blockFormat()
        block_format.setAlignment(Qt.AlignmentFlag.AlignLeft)
        cursor.setBlockFormat(block_format)
        self.main_window.text_edit.setTextCursor(cursor)
