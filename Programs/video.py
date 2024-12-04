import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
from SessionManager import SessionManager

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reproductor de Video")
        self.setGeometry(100, 100, 800, 600)

        self.session = SessionManager()

        self.video_widget = QVideoWidget()
        self.open_button = QPushButton("Open Video")
        self.open_button.clicked.connect(self.open_file)

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addWidget(self.open_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file(self):
        data = self.session.load_session()
        init_dir = ""
        if data:
            last_user, init_dir = list(data.items())[-1]
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir Video", init_dir, "Archivos de Video (*.mp4 *.avi *.mkv)")
        if file_path:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.media_player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())

