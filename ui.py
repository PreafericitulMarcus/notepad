from PyQt6.QtWidgets import  QTextEdit, QApplication
from PyQt6.QtGui import QIcon, QFont, QAction
from text_editing import TextEditing
from file_operations import FileOperations
import helpful_features
from text_config import PlainTextEdit

class Ui_MainWindow:
    def setup_ui(self, MainWindow):
        # Initialize the text editor
        self.setWindowTitle("Notepad")
        self.text_edit = PlainTextEdit(MainWindow)
        self.text_edit.setFont(QFont("Consolas", 11))
        self.setCentralWidget(self.text_edit)

        # Initialize objects
        self.file_operations = FileOperations(self)
        self.text_editing = TextEditing(self)

        # Create the menu bar
        self.create_menu_bar(MainWindow)

    def create_menu_bar(self, MainWindow):
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")

        # Edit menu
        edit_menu = menubar.addMenu("Edit")

        # Helpful menu
        helpful_menu = menubar.addMenu("Helpful")

        # Alignment menu
        align_menu = edit_menu.addMenu("Alignment")

        # New action
        new_action = QAction(QIcon(), "New", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.file_operations.new_file)
        file_menu.addAction(new_action)

        # Open action
        open_action = QAction(QIcon(), "Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.file_operations.open_file)
        file_menu.addAction(open_action)

        # Save action
        save_action = QAction(QIcon(), "Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.file_operations.save_file)
        file_menu.addAction(save_action)

        # Save As action
        save_as_action = QAction(QIcon(), "Save As", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self.file_operations.save_file_as)
        file_menu.addAction(save_as_action)

        # Save recent file action
        self.recent_files_menu = file_menu.addMenu("Recent Files")
        self.update_recent_files_menu()

        # Exit action
        exit_action = QAction(QIcon(), "Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(MainWindow.close)
        file_menu.addAction(exit_action)

        # Move to end line action
        end_of_line_action = QAction(QIcon(), "End of Line", self)
        end_of_line_action.setShortcut("Ctrl+E")
        end_of_line_action.triggered.connect(
            self.text_editing.move_cursor_to_end_of_line
        )
        edit_menu.addAction(end_of_line_action)

        # Add line above action
        add_line_above_action = QAction(QIcon(), "Add line Above", self)
        add_line_above_action.setShortcut("Ctrl+Shift+L")
        add_line_above_action.triggered.connect(self.text_editing.add_line_above)
        edit_menu.addAction(add_line_above_action)

        # Add line below action
        add_line_below_action = QAction(QIcon(), "Add line Below", self)
        add_line_below_action.setShortcut("Ctrl+L")
        add_line_below_action.triggered.connect(self.text_editing.add_line_below)
        edit_menu.addAction(add_line_below_action)

        # Center text action
        center_text_action = QAction(QIcon(), "Center text", self)
        center_text_action.setShortcut("Ctrl+Alt+K")
        center_text_action.triggered.connect(self.text_editing.center_text)
        align_menu.addAction(center_text_action)

        # Move text to right action
        right_text_action = QAction(QIcon(), "Move text Right", self)
        right_text_action.setShortcut("Ctrl+Alt+L")
        right_text_action.triggered.connect(self.text_editing.right_text)
        align_menu.addAction(right_text_action)

        # Move text to left action
        left_text_action = QAction(QIcon(), "Move text Left", self)
        left_text_action.setShortcut("Ctrl+Alt+J")
        left_text_action.triggered.connect(self.text_editing.left_text)
        align_menu.addAction(left_text_action)

        # Find action
        find_text_action = QAction(QIcon(), "Find", self)
        find_text_action.setShortcut("Ctrl+F")
        find_text_action.triggered.connect(self.show_find_dialog)
        helpful_menu.addAction(find_text_action)
    
    
    def update_recent_files_menu(self):
        self.recent_files_menu.clear()
        for file_path in self.file_operations.recent_files:
            recent_file_action = QAction(file_path, self)
            recent_file_action.triggered.connect(
                lambda checked, path=file_path: self.file_operations.load_file(path)
            )
            self.recent_files_menu.addAction(recent_file_action)

    def show_find_dialog(self):
        self.find_dialog = helpful_features.FindDialog(self)
        self.find_dialog.show()
