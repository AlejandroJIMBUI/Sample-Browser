import sys
from pathlib import Path
import json


def resource_path(relative_path):
    """
    Get the absolute path to a resource, compatible with PyInstaller.

    Args:
        relative_path (str): The relative path to the resource.

    Returns:
        str: The absolute path to the resource.
    """
    base_path = getattr(sys, '_MEIPASS', Path(__file__).parent.parent)  # Handle PyInstaller's temporary folder
    return str(Path(base_path) / relative_path)


def load_theme(theme_name, widgets=None):
    """
    Load a theme from a JSON file and apply styles to widgets.

    Args:
        theme_name (str): The name of the theme to load (key in the JSON file).
        widgets (dict, optional): A dictionary of widgets to apply specific styles to. 
                                  Keys should match the widget names in the theme.

    Returns:
        tuple: A tuple containing:
            - stylesheet (str): The global stylesheet for the application.
            - image_path (str): The path to the theme's image resource.
            - progress_style (str): The stylesheet for the progress bar.
    """
    try:
        # Load the JSON file containing theme definitions
        with open(resource_path("themes.json"), "r") as file:
            themes = json.load(file)  # Parse the JSON file
            theme = themes.get(theme_name, {})  # Get the theme by name, or an empty dictionary if not found

            # Generate the global stylesheet by excluding specific widget styles
            stylesheet = "\n".join(
                [f"{selector} {{ {rules} }}" for selector, rules in theme.items()
                 if selector not in ["info_label", "footer_label", "image", "progress_bar"]]
            )

            # Get the progress bar style
            progress_style = theme.get("progress_bar", "")

            # Get the path to the theme's image resource
            image_path = resource_path(theme.get("image", ""))

            # Apply specific styles to widgets if provided
            if widgets:
                if "info_label" in theme and "info_label" in widgets:
                    widgets["info_label"].setStyleSheet(theme["info_label"])
                if "footer_label" in theme and "footer_label" in widgets:
                    widgets["footer_label"].setStyleSheet(theme["footer_label"])

            # Return the global stylesheet, image path, and progress bar style
            return stylesheet, image_path, progress_style

    except (FileNotFoundError, json.JSONDecodeError) as e:
        # Handle errors when the theme file is missing or contains invalid JSON
        print(f"Error loading theme: {e}")
        return "", "", ""  # Return empty values as a fallback