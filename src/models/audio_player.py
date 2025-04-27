from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl

class AudioPlayer:
    """
    A simple audio player class that uses PyQt6's QMediaPlayer and QAudioOutput
    to play audio files.
    """
    def __init__(self):
        """
        Initialize the audio player with a media player and audio output.
        """
        self.player = QMediaPlayer()  # Create a media player instance
        self.audio_output = QAudioOutput()  # Create an audio output instance
        self.player.setAudioOutput(self.audio_output)  # Link the audio output to the media player

    def play(self, path):
        """
        Play an audio file from the specified file path.

        Args:
            path (str): The file path to the audio file to be played.
        """
        self.player.setSource(QUrl.fromLocalFile(path))  # Set the audio file as the media source
        self.player.play()  # Start playback