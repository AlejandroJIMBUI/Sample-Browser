from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import QDir, Qt

class FileSystemManager:
    def __init__(self):
        self.model = QFileSystemModel()
        self.model.setRootPath("")
        
        # Configurar los filtros para mostrar archivos y directorios
        self.model.setFilter(QDir.Filter.AllDirs | 
                           QDir.Filter.Files | 
                           QDir.Filter.NoDotAndDotDot | 
                           QDir.Filter.Hidden)
        
        # Establecer los filtros de nombre para tipos de audio
        self.model.setNameFilters(["*.wav", "*.mp3", "*.aif", "*.flac", 
                                 "*.mid", "*.amxd", "*.adg", "*.fst", 
                                 "*.fxp", "*.fxb", "*.ogg"])
        self.model.setNameFilterDisables(False)