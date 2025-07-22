from PyQt6.QtWidgets import QMenuBar, QMessageBox
from PyQt6.QtCore import QSettings
from PyQt6.QtGui import QIcon
from utils.helpers import resource_path
from utils.helpers import load_theme

class MenuThemes:
    def __init__(self, app, browser):
        """
        Initialize the ThemeManager.

        Args:
            app (QApplication): The main application instance.
            browser (QMainWindow): The main application window.
        """
        self.app = app
        self.browser = browser
        self.settings = QSettings("SampleBrowser", "SampleBrowserPro")
        self.themes = ["dark", "softBlue", "1bitMonitorGlow", "everglowDiamond"]

    def setup_menu(self):
        """
        Set up the menu bar for theme selection.
        """
        menu_bar = QMenuBar(self.browser)
        themes_menu = menu_bar.addMenu("Themes")

        for theme in self.themes:
            action = themes_menu.addAction(theme)
            action.triggered.connect(lambda checked, t=theme: self.select_theme(t))

        self.browser.setMenuBar(menu_bar)

    def select_theme(self, selected_theme):
        """
        Update the theme, save the selection, and prompt for a restart.

        Args:
            selected_theme (str): The name of the selected theme.
        """
        self.settings.setValue("selected_theme", selected_theme)

        # Show a message box to inform the user
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Restart Required")
        msg_box.setText("The application needs to restart to apply the selected theme.")
        msg_box.setWindowIcon(QIcon(resource_path("resources/icons/icon.ico")))

        # Apply a specific style to the QMessageBox
        msg_box.setStyleSheet("""
            }
            QMessageBox QLabel {
                color: #ffffff;
            }
        """)

        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()  # Show the message box

        self.app.quit()  # Restart the application to apply the new theme

    def load_theme(self):
        """
        Load the last selected theme or default to "dark".

        Returns:
            tuple: A tuple containing the stylesheet, image path, and progress style.
        """
        theme_name = self.settings.value("selected_theme", "dark")
        if theme_name not in self.themes:
            theme_name = "dark"  # Default to "dark" if the saved theme is not available

        return load_theme(theme_name)