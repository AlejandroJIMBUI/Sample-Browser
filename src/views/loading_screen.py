from PyQt6.QtWidgets import QSplashScreen, QProgressBar, QLabel, QApplication
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from utils.helpers import resource_path

class LoadingScreen(QSplashScreen):
    def __init__(self, progress_style=None):
        """
        Initialize the loading screen with a background image, progress bar, and message label.
        
        Args:
            progress_style (str): Optional stylesheet for customizing the progress bar appearance.
        """
        # Load the background image and scale it to fit the splash screen
        pixmap = QPixmap(resource_path("resources/images/splash_screen.png")).scaled(
            800, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        )
        super().__init__(pixmap)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Remove window borders for a clean look

        # Create a label to display loading messages
        self.label = QLabel(self)
        self.label.setText("Cargando aplicación...")  # Default loading message
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center-align the text
        self.label.setStyleSheet("""
            QLabel {
                color: #888189;
                font-size: 14px;
                font-family: "Arial";
                padding: 5px;
                background: none;  /* Remove background */
            }
        """)
        self.label.setGeometry(0, pixmap.height() - 60, pixmap.width(), 30)  # Position above the progress bar

        # Create a progress bar to show loading progress
        self.progress = QProgressBar(self)
        self.progress.setRange(0, 100)  # Set progress range from 0 to 100
        self.progress.setTextVisible(False)  # Hide the percentage text on the progress bar
        if progress_style:
            self.progress.setStyleSheet(progress_style)  # Apply custom styles if provided
        self.progress.setGeometry(0, pixmap.height() - 20, pixmap.width(), 20)  # Position at the bottom of the image

    def update_progress(self, value, message=None):
        """
        Update the progress bar value and optionally display a new loading message.
        
        Args:
            value (int): The current progress value (0-100).
            message (str): Optional message to display above the progress bar.
        """
        self.progress.setValue(value)  # Update the progress bar value
        if message:
            self.label.setText(message)  # Update the loading message if provided
        QApplication.processEvents()  # Process UI events to ensure updates are visible immediately