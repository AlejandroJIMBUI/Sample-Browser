<div align="center">
  <img alt="logo" width="120" src="https://github.com/AlejandroJIMBUI/proyAssets/blob/main/Sample_Browser_Assets/icon.png?raw=true"/>
  <h1>Sample Browser</h1>
</div>

<div align="center">
   <a href="https://www.python.org/downloads/" target="_blank">
   <img src="https://img.shields.io/static/v1?style=flat-square&label=Python&message=3.9.0%2B&logo=python&labelColor=282828&logoColor=3776AB&color=414b32" alt="Python: 3.9.0+" />
   </a>
</div>

**Sample Browser** is a Python-based desktop application built with PyQt6, designed for music producers working across multiple DAWs. It enables efficient audio file browsing, previewing, and management, featuring an intuitive and customizable interface with support for visual themes and persistent settings.

---

# Characteristics

- **File Explorer**: Navigate your file system using tree and list views.
- **Audio Preview**: Play supported audio files directly within the application.
- **Multi-Format Support**:Supports a wide range of audio formats (`.wav`, `.mp3`, `.aif`, `.ogg`, `.flac`) as well as project/plugin formats (`.mid`, `.amxd`, `.adg`, `.fst`, `.fxp`, `.fxb`).  
- **Customizable Interface**: Switch visual themes and save settings such as the last opened directory, window geometry, and panel states.
- **Drag and Drop**: Supports dragging files directly from the file list.
- **Theme Loader**: Customize the app's appearance with visual styles.

---

# System Requirements

- **Operating System**: Windows 10/11 (64-bit)
- **Python**: Version 3.9 or higher
- **Dependencies**:
  - PyQt6

> [!NOTE]
>
> I'm still working on the MAC and Linux versions.
---

# Installation

### Option 1: Executable (Recommended)
1. Download the installer from [Sample Browser v2.0.0](https://github.com/AlejandroJIMBUI/Sample-Browser/releases/tag/v2.0.0).
2. Run the installer and follow the on-screen instructions.
3. Once installed, launch the application from the Start menu.

### Option 2: Source Code Installation
1. Clone this repository using the following command:
   ```bash
   git clone https://github.com/AlejandroJIMBU/Sample-Browser.git
   cd sample-browser
   ```
2. Create a Virtual Environment and Install Dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run the Application:
   ```bash
   python src/main.py
   ```

---

# interface screenshoots

<details close>
  <summary>Images</summary>

### Theme: dark
![Theme: dark](https://github.com/AlejandroJIMBUI/proyAssets/blob/main/Sample_Browser_Assets/dark_screenshot.png?raw=true)

### Theme: softBlue
![Theme: softBlue](https://github.com/AlejandroJIMBUI/proyAssets/blob/main/Sample_Browser_Assets/softBlue_screenshot.png?raw=true)

### Theme: 1bitMonitorGlow
![Theme: 1bitMonitorGlow](https://github.com/AlejandroJIMBUI/proyAssets/blob/main/Sample_Browser_Assets/1bitMonitorGlow_screenshot.png?raw=true)

### Theme: everglowDiamond
![Theme: everglowDiamond](https://github.com/AlejandroJIMBUI/proyAssets/blob/main/Sample_Browser_Assets/everglowDiamond_screenshot.png?raw=true)

Future releases will introduce new themes and additional features

</details>


---

# Usage

1. Upon launching the application, select a directory using the built-in file explorer.
2. Preview audio files by clicking on them.
3. Customize your experience through the settings menu to:
   - Switch visual themes
4. Drag and drop files directly from the file list to external applications.

---

# Development

### Setting Up the Development Environment
- Install Development Dependencies
   ```bash
   pip install -r requirements.txt
   ```

### Building the Application
- Generating Executables with PyInstaller
   ```bash
   pyinstaller --onefile --windowed main.py
   ```

### Key Build Options:
- `--onefile`: Single executable output
- `--windowed`: Prevent console window display (GUI apps)
- `--name`: Set output application name
- `--icon`: Specify application icon
- `--add-data`: Include additional resource files

### Post-Build Verification:
- Check generated files in /dist directory
- Test executable functionality
- Validate resource inclusion

---

# Downloads

**Latest Release**: [Sample Browser Ver 2.0.0](https://github.com/AlejandroJIMBUI/Sample-Browser/releases/tag/v2.0.0)
