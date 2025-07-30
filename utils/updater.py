# utils/updater.py
import requests
from PyQt6.QtWidgets import QMessageBox

def check_for_updates(current_version):
    try:
        response = requests.get(
            "https://raw.githubusercontent.com/AlejandroJIMBUI/proyAssets/main/Sample_Browser_Assets/versions.json",
            timeout=5
        )
        data = response.json()
        if data["latest_version"] > current_version:
            return data
        return None
    except Exception as e:
        print(f"Error checking for updates: {e}")
        return None

def show_update_notification(parent, update_data):
    msg = QMessageBox(parent)
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setWindowTitle("Update available")
    msg.setText(f"Version {update_data['latest_version']} available.\nDo you want to download it?")
    msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    
    if msg.exec() == QMessageBox.StandardButton.Yes:
        import webbrowser
        webbrowser.open(update_data["download_url"])