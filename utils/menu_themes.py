from PyQt6.QtWidgets import QMenuBar, QMessageBox
from PyQt6.QtCore import QSettings
from PyQt6.QtGui import QIcon
from utils.helpers import resource_path
from utils.helpers import load_theme

class MenuThemes:
    def __init__(self, app, browser):
        self.app = app
        self.browser = browser
        self.settings = QSettings("SampleBrowser", "SampleBrowserPro")
        self.themes = ["dark", "softBlue", "1bitMonitorGlow", "everglowDiamond"]
        self.is_initial_load = True

    def setup_menu(self):
        """
        Creates the theme selection menu and adds it to the browser's menu bar.
        """
        if self.browser is None:    
            return
            
        menu_bar = QMenuBar(self.browser)
        themes_menu = menu_bar.addMenu("Themes")

        # Add an action for each theme, connecting it to the selection handler
        for theme in self.themes:
            action = themes_menu.addAction(theme)
            # Use a lambda to pass the theme name to the handler
            action.triggered.connect(lambda checked, t=theme: self.select_theme(t))

        self.browser.setMenuBar(menu_bar)

    def select_theme(self, selected_theme):
        """
        Handles user theme selection, saves it, 
        and applies the theme with notification.
        """
        self.settings.setValue("selected_theme", selected_theme)
        self.apply_theme(selected_theme, show_notification=True)

    def apply_theme(self, theme_name, show_notification=False):
        """
        Applies the selected theme to the app and browser, 
        optionally showing a notification.
        """
        if self.app is None:
            return
        
        # Load theme resources (stylesheet, image, progress bar style)    
        stylesheet, mage_path, progress_style = load_theme(theme_name)
        
        # Apply stylesheet to the main app
        self.app.setStyleSheet(stylesheet)
        
        # Apply stylesheet to the browser window if available
        if self.browser is not None:
            self.browser.setStyleSheet(stylesheet)
        
        # Show notification only if not the initial load and notification is requested
        if show_notification and not self.is_initial_load:
            self.show_theme_changed_notification(theme_name)

    def show_theme_changed_notification(self, theme_name):
        """
        Displays a message box notifying the user that the theme has changed.
        """
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Theme Changed")
        msg_box.setText(f"Theme changed to {theme_name} successfully.")
        
        # Set window icon using a helper function for resource path
        msg_box.setWindowIcon(QIcon(resource_path("resources/icons/icon.ico")))
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        # Use the current app stylesheet for consistency
        msg_box.setStyleSheet(self.app.styleSheet())
        msg_box.exec()

    def load_initial_theme(self):
        """
        Loads the initial theme from settings without showing a notification.
        """
        theme_name = self.settings.value("selected_theme", "dark")
        
        # Fallback to default theme if the saved theme is not available
        if theme_name not in self.themes:
            theme_name = "dark"
        
        self.apply_theme(theme_name)
        """
        Mark that the initial load is complete so notifications can be shown later
        """
        self.is_initial_load = False
        
        # Return theme resources for further use if needed
        return load_theme(theme_name)