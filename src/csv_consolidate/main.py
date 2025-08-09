import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


class FileDialogExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("CSV Consolidate")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("Select CSV Directory", self)
        self.button.clicked.connect(self.select_directory_dialog)
        self.button.setGeometry(150, 150, 150, 30)

    def select_directory_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle(
            "CSV Consolidate: Select Directory with Only CSV Files to Consolidate",
        )
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)
        file_dialog.setViewMode(QFileDialog.ViewMode.List)

        if file_dialog.exec():
            selected_directory = file_dialog.selectedFiles()[0]
            print("Selected Directory:", selected_directory)


def main():
    app = QApplication(sys.argv)
    window = FileDialogExample()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
