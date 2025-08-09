import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import polars as pl
from datetime import datetime
from pathlib import Path
import pytz
from rich.pretty import pprint


class DirectoryPicker(QMainWindow):
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
            pprint(f"Selected Directory: {selected_directory}")
            consolidate_csv_files(csv_dir=selected_directory)
            QApplication.instance().quit()


def consolidate_csv_files(*, csv_dir: str):
    """Consolidate all CSV files in the dir and write new CSV file."""
    # Create a path
    dir_path = Path(csv_dir)

    # Get the CSV file paths
    csv_files = dir_path.glob(pattern="*.csv")

    # Create LazyFrames for each CSV and concatenate them
    consolidated_lazy_frame = pl.concat([pl.scan_csv(file) for file in csv_files])

    # Collect the LazyFrame into a DataFrame
    consolidated_df = consolidated_lazy_frame.collect()

    # Display the consolidated DataFrame (optional)
    pprint(consolidated_df)

    # Save the consolidated DataFrame to a new CSV file
    home_dir = Path.home()
    # Assuming us central
    timezone_name = "US/Central"
    # Create a tzinfo object from the timezone name
    tz = pytz.timezone(timezone_name)
    dt_str = datetime.now(tz=tz).strftime("%Y%m%d_%H%M%S")
    consolidated_file_path = home_dir / f"Documents/csv_consolidated_{dt_str}.csv"
    consolidated_df.write_csv(consolidated_file_path)
    pprint(f"Consolidated CSV file written to {consolidated_file_path}")


def main():
    app = QApplication(sys.argv)
    window = DirectoryPicker()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
