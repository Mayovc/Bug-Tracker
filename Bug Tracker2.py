import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog

class BugTrackerGUI(QMainWindow):
    def __init__(self, bug_tracker):
        super().__init__()
        self.bug_tracker = bug_tracker

        # Create the main menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Create the "Open" action
        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_bug_tracker)
        self.file_menu.addAction(open_action)

        # Create the "Save" action
        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_bug_tracker)
        self.file_menu.addAction(save_action)

        # Create the "Exit" action
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        self.file_menu.addAction(exit_action)

        # Create the text edit widget
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Set the window properties
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle("Bug Tracker")
        self.show()

    def open_bug_tracker(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Bug Tracker", "", "Bug Tracker Files (*.bt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "r") as file:
                self.bug_tracker = load_bug_tracker(file)
                self.update_text_edit()

    def save_bug_tracker(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Bug Tracker", "", "Bug Tracker Files (*.bt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "w") as file:
                save_bug_tracker(self.bug_tracker, file)

    def update_text_edit(self):
        self.text_edit.clear()
        for i, bug in enumerate(self.bug_tracker.bugs):
            self.text_edit.append(f"Bug {i+1}: {bug.description}")
class BugTracker:
    def __init__(self):
        self.bugs = []

    def add_bug(self, bug):
        self.bugs.append(bug)

    def remove_bug(self, bug):
        self.bugs.remove(bug)

bug_tracker = BugTracker()
# initialize the bug tracker with some bugs

app = QApplication(sys.argv)


import pickle

def load_bug_tracker(file):
    return pickle.load(file)

def save_bug_tracker(bug_tracker, file):
    pickle.dump(bug_tracker, file)


