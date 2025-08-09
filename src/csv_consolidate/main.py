import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


class FileDialogExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("QFileDialog Example - Select Directory")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("Select Directory", self)
        self.button.clicked.connect(self.selectDirectoryDialog)
        self.button.setGeometry(150, 150, 150, 30)

    def selectDirectoryDialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Select Directory")
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
