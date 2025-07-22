import sys
import time
from PyQt6.QtWidgets import QApplication
from views.sample_browser import SampleBrowser
from views.loading_screen import LoadingScreen
from utils.menu_themes import MenuThemes

if __name__ == "__main__":
    
    # Create the main application instance
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Initialize the ThemeManager
    theme_manager = MenuThemes(app, None)
    # load the initial theme (without showing notification)
    stylesheet, image_path, progress_style = theme_manager.load_initial_theme()
    # Apply the loaded stylesheet if available
    if stylesheet:
        app.setStyleSheet(stylesheet)
        
    # Initialize and display the loading screen
    splash = LoadingScreen(progress_style=progress_style)
    splash.show()
    # Set message and progress time intervals
    splash.update_progress(10, "Initializing application...")
    time.sleep(0.3)
    splash.update_progress(25, "Loading visual theme...")
    time.sleep(0.3)
    splash.update_progress(50, "Setting up the interface...")
    time.sleep(0.5)
    splash.update_progress(75, "Loading components...")
    time.sleep(0.4)   

    # Create the main application window
    browser = SampleBrowser(stylesheet=stylesheet, image_path=image_path)
    theme_manager.browser = browser # Set the browser instance in ThemeManager
    theme_manager.setup_menu() # Set up the theme menu
    splash.update_progress(100, "Ready!")
    time.sleep(0.3) # Simulate a short delay before finishing

    # Show the main window and close the loading screen
    browser.show()
    splash.finish(browser)
    sys.exit(app.exec()) # Start the application's event loop