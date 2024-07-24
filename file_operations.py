from PyQt6.QtWidgets import QFileDialog, QMessageBox


class FileOperations:
    def __init__(self, main_window):
        self.main_window = main_window
        self.recent_files = []
        self.max_recent_files = 5
        self.current_file = None

    def new_file(self):
        self.main_window.text_edit.clear()
        self.current_file = None

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self.main_window, "Open File", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            self.load_file(file_name)

    def load_file(self, file_name):
        try:
            with open(file_name, "r") as file:
                self.main_window.text_edit.setText(file.read())
            self.current_file = file_name
            self.add_recent_file(file_name)
        except Exception as e:
            QMessageBox.critical(self.main_window, "Error", f"Failed to open file: {e}")

    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, "w") as file:
                    file.write(self.main_window.text_edit.toPlainText())
            except Exception as e:
                QMessageBox.critical(
                    self.main_window, "Error", f"Failed to save file: {e}"
                )
        else:
            self.save_file_as()

    def save_file_as(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self.main_window, "Save File As", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            try:
                with open(file_name, "w") as file:
                    file.write(self.main_window.text_edit.toPlainText())
                self.current_file = file_name
                self.add_recent_file(file_name)
            except Exception as e:
                QMessageBox.critical(
                    self.main_window, "Error", f"Failed to save file: {e}"
                )

    def add_recent_file(self, file_path):
        if file_path not in self.recent_files:
            self.recent_files.insert(0, file_path)
            if len(self.recent_files) > self.max_recent_files:
                self.recent_files.pop()
        else:
            self.recent_files.remove(file_path)
            self.recent_files.insert(0, file_path)
        self.main_window.update_recent_files_menu()
