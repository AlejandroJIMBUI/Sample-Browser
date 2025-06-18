import os
from PyQt6.QtWidgets import (QMainWindow, QTreeView, QListView, 
                             QSplitter, QVBoxLayout, QWidget, 
                             QLabel, QSizePolicy)
from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtGui import QIcon, QPixmap

from utils.helpers import *
from models.file_system_manager import FileSystemManager
from models.audio_player import AudioPlayer

# Main class for the Sample Browser application
class SampleBrowser(QMainWindow):
    def __init__(self, stylesheet=None, image_path=None):
        """
        Initialize the main window of the Sample Browser application.
        
        Args:
            stylesheet (str): Optional stylesheet for the application.
            image_path (str): Optional path to an image to display in the UI.
        """
        super().__init__()
        self.setWindowTitle("Sample Browser")
        self.setGeometry(100, 100, 1600, 1000)
        self.setWindowIcon(QIcon(resource_path("resources/icons/sp_b_icon.ico")))

        # Persistent settings for the application
        self.settings = QSettings("SampleBrowser", "SampleBrowserPro")

        # Initialize file system manager and audio player
        self.fs_manager = FileSystemManager()
        self.model = self.fs_manager.model
        self.audio_player = AudioPlayer()

        # Create UI components
        self.tree = QTreeView()
        self.list = QListView()
        self.splitter = QSplitter(Qt.Orientation.Horizontal)

        # Set up the file system model for the tree and list views
        self.tree.setModel(self.model)
        self.list.setModel(self.model)

        # Set the root path for the file system view
        root_path = Path("C:/" if os.name == "nt" else "/")
        self.tree.setRootIndex(self.model.index(str(root_path)))
        self.tree.setAnimated(True)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)

        # Connect tree view click event to update the list view
        self.tree.clicked.connect(self.on_tree_clicked)

        # Create labels for displaying information and images
        self.info_label = QLabel("select sample")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add tree and list views to the splitter
        self.splitter.addWidget(self.tree)
        self.splitter.addWidget(self.list)
        self.splitter.setSizes([400, 800])

        # Set up the main layout
        layout = QVBoxLayout()
        layout.addWidget(self.splitter, 8)
        layout.addWidget(self.info_label, 1)
        layout.addWidget(self.image_label, 1)
        layout.setSpacing(5)

        # Create a container widget and set it as the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Apply optional stylesheet
        if stylesheet:
            self.setStyleSheet(stylesheet)

        # Configure drag-and-drop for the list view
        self.list.setDragEnabled(True)
        self.list.setSelectionMode(QListView.SelectionMode.SingleSelection)
        self.list.setDragDropMode(QListView.DragDropMode.DragOnly)

        # Connect list view click event to preview audio samples
        self.list.clicked.connect(self.preview_sample)

        # Load saved settings (e.g., last opened path, window geometry)
        self.load_settings()

    def on_tree_clicked(self, index):
        """
        Handle clicks on the tree view to update the list view.
        
        Args:
            index (QModelIndex): The index of the clicked item in the tree view.
        """
        path = self.model.filePath(index)
        self.list.setRootIndex(self.model.index(path))
        self.settings.setValue("last_path", path)

    def preview_sample(self, index):
        """
        Preview an audio sample when an item in the list view is clicked.
        
        Args:
            index (QModelIndex): The index of the clicked item in the list view.
        """
        path = self.model.filePath(index)
        if path.lower().endswith(('.wav', '.mp3', '.aif', '.flac')):
            self.audio_player.play(path)
            file_info = self.model.fileInfo(index)
            size = file_info.size() / (1024 * 1024)
            self.info_label.setText(f"▶ {file_info.fileName()} | {size:.2f}MB | {file_info.path()}")

    def load_settings(self):
        """
        Load persistent settings such as the last opened path, window geometry,
        and splitter state.
        """
        last_path = self.settings.value("last_path", "")
        if last_path and os.path.exists(last_path):
            self.list.setRootIndex(self.model.index(last_path))
            path = Path(last_path)
            parents = []
            while path != path.parent:
                parents.append(path)
                path = path.parent
            current_index = self.model.index(str(parents[-1] if parents else ""))
            for p in reversed(parents[:-1]):
                self.tree.expand(current_index)
                current_index = self.model.index(str(p))
        geometry = self.settings.value("window_geometry")
        if geometry:
            self.restoreGeometry(geometry)
        splitter_state = self.settings.value("splitter_state")
        if splitter_state:
            self.splitter.restoreState(splitter_state)

    def closeEvent(self, event):
        """
        Save settings (e.g., last opened path, window geometry, splitter state)
        when the application is closed.
        
        Args:
            event (QCloseEvent): The close event.
        """
        current_index = self.list.rootIndex()
        current_path = self.model.filePath(current_index)
        if current_path:
            self.settings.setValue("last_path", current_path)
        self.settings.setValue("window_geometry", self.saveGeometry())
        self.settings.setValue("splitter_state", self.splitter.saveState())
        super().closeEvent(event)