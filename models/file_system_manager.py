from PyQt6.QtGui import QFileSystemModel

class FileSystemManager:
    """
    A manager class for handling the file system model, which is used to display
    and filter files in the application.
    """
    def __init__(self):
        """
        Initialize the file system manager with a QFileSystemModel.
        The model is configured to filter and display specific audio file formats.
        """
        self.model = QFileSystemModel()  # Create a file system model instance
        self.model.setRootPath("")  # Set the root path to the entire file system
        self.model.setNameFilters(["*.wav", "*.mp3", "*.aif", "*.flac"])  # Filter for audio file formats
        self.model.setNameFilterDisables(False)  # Ensure non-matching files are hidden