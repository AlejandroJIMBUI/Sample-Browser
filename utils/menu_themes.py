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
        """Configura el menú de temas"""
        if self.browser is None:
            return
            
        menu_bar = QMenuBar(self.browser)
        themes_menu = menu_bar.addMenu("Themes")

        for theme in self.themes:
            action = themes_menu.addAction(theme)
            action.triggered.connect(lambda checked, t=theme: self.select_theme(t))

        self.browser.setMenuBar(menu_bar)

    def select_theme(self, selected_theme):
        """Selección de tema por el usuario (con notificación)"""
        self.settings.setValue("selected_theme", selected_theme)
        self.apply_theme(selected_theme, show_notification=True)

    def apply_theme(self, theme_name, show_notification=False):
        """Aplica el tema con opción de mostrar notificación"""
        if self.app is None:
            return
            
        stylesheet, image_path, progress_style = load_theme(theme_name)
        
        self.app.setStyleSheet(stylesheet)
        
        if self.browser is not None:
            self.browser.setStyleSheet(stylesheet)
        
        # Solo muestra notificación si no es la carga inicial y está habilitado
        if show_notification and not self.is_initial_load:
            self.show_theme_changed_notification(theme_name)

    def show_theme_changed_notification(self, theme_name):
        """Muestra notificación de cambio de tema"""
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Theme Changed")
        msg_box.setText(f"Theme changed to {theme_name} successfully.")
        msg_box.setWindowIcon(QIcon(resource_path("resources/icons/icon.ico")))
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setStyleSheet(self.app.styleSheet())
        msg_box.exec()

    def load_initial_theme(self):
        """Carga el tema inicial sin mostrar notificación"""
        theme_name = self.settings.value("selected_theme", "dark")
        if theme_name not in self.themes:
            theme_name = "dark"
        
        self.apply_theme(theme_name)
        self.is_initial_load = False  # Marca que la carga inicial ha terminado
        return load_theme(theme_name)