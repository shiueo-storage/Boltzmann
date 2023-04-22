from PySide6.QtCore import QTimer
from PySide6.QtWidgets import *

from utils import global_path


class Boltzmann_Engine_GUI(QWidget):
    def __init__(self, PROJECT_PATH, PROJECT_NAME, DEV_NAME):
        super().__init__(parent=None)
        self.GRID = QGridLayout(parent=None)

        # update_ui용 타이머
        self.UPDATE_TIMER = QTimer()

        # 변수들
        self.PROJECT_PATH = PROJECT_PATH
        self.PROJECT_NAME = PROJECT_NAME
        self.DEV_NAME = DEV_NAME

        # 윈도우 설정
        self.setWindowTitle(
            f"Boltzmann Engine - {self.PROJECT_PATH} - {self.DEV_NAME} - {self.PROJECT_NAME}"
        )
        self.setMinimumSize(600, 200)
        self.initUI()

    def initUI(self):
        with open(
            file=global_path.get_proj_abs_path("assets/stylesheet.txt"), mode="r"
        ) as f:
            self.setStyleSheet(f.read())

        # 타이머 설정
        self.UPDATE_TIMER.setInterval(1000 / 4)
        self.UPDATE_TIMER.timeout.connect(lambda: self.updateUI())
        self.UPDATE_TIMER.start()

        # 프로젝트 이름
        self.setLayout(self.GRID)

    def updateUI(self):
        pass
