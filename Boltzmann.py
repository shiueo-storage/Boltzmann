import os.path
import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import *

from utils import global_path
from view import Boltzmann_engine

global_path.set_proj_abs_path(os.path.abspath(__file__))


class Boltzmann_GUI(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.GRID = QGridLayout(parent=None)

        # update_ui용 타이머
        self.UPDATE_TIMER = QTimer()

        # 프로젝트 이름
        self.PROJECT_NAME_LAYOUT = QHBoxLayout()
        self.PROJECT_NAME_LINEEDIT = QLineEdit()
        self.PROJECT_NAME_LABEL = QLabel("Project Name:")

        # 개발자 이름
        self.PROJECT_DEV_NAME_LAYOUT = QHBoxLayout()
        self.PROJECT_DEV_NAME_LINEEDIT = QLineEdit()
        self.PROJECT_DEV_NAME_LABEL = QLabel("DEV Name:")

        # 프로젝트 위치 / 위치설정 창
        self.PROJECT_LOCATION_LAYOUT = QHBoxLayout()
        self.PROJECT_LOCATION_LINEEDIT = QLineEdit()
        self.PROJECT_LOCATION_LABEL = QLabel("Location:")
        self.PROJECT_LOCATION_FILE_DIALOG = QFileDialog()
        self.PROJECT_LOCATION_FILE_DIALOG_BUTTON = QPushButton("Find Location")
        self.PROJECT_LOCATION_FILE_DIALOG_BUTTON.clicked.connect(
            lambda: self.CLICKED_PROJECT_LOCATION_FILE_DIALOG_BUTTON()
        )

        # 적용 버튼
        self.APPLY_BUTTON = QPushButton("APPLY")
        self.APPLY_BUTTON.clicked.connect(lambda: self.CLICKED_APPLY_BUTTON())

        # 프로젝트 열기 버튼
        self.OPEN_BUTTON = QPushButton("OR OPEN")
        self.OPEN_PROJECT_DIALOG = QFileDialog()
        self.OPEN_BUTTON.clicked.connect(lambda: self.CLICKED_OPEN_BUTTON())

        # 상태 라벨
        self.STATUS_LABEL = QLabel("WAITING")

        # 변수들

        # 윈도우 설정
        self.setWindowTitle("Boltzmann Engine")
        self.setMinimumSize(600, 200)
        self.initUI()

    def initUI(self):
        with open(
            file=global_path.get_proj_abs_path("assets/stylesheet.txt"), mode="r"
        ) as f:
            self.setStyleSheet(f.read())

        # 타이머 설정
        self.UPDATE_TIMER.setInterval(1000 / 3)
        self.UPDATE_TIMER.timeout.connect(lambda: self.updateUI())
        self.UPDATE_TIMER.start()

        # 프로젝트 이름
        self.PROJECT_NAME_LAYOUT.addWidget(self.PROJECT_NAME_LABEL)
        self.PROJECT_NAME_LAYOUT.addWidget(self.PROJECT_NAME_LINEEDIT)

        # 개발자 이름
        self.PROJECT_DEV_NAME_LAYOUT.addWidget(self.PROJECT_DEV_NAME_LABEL)
        self.PROJECT_DEV_NAME_LAYOUT.addWidget(self.PROJECT_DEV_NAME_LINEEDIT)

        # 프로젝트 위치 / 위치설정 창
        self.PROJECT_LOCATION_LAYOUT.addWidget(self.PROJECT_LOCATION_LABEL)
        self.PROJECT_LOCATION_LAYOUT.addWidget(self.PROJECT_LOCATION_LINEEDIT)
        self.PROJECT_LOCATION_LAYOUT.addWidget(self.PROJECT_LOCATION_FILE_DIALOG_BUTTON)

        self.GRID.addLayout(self.PROJECT_NAME_LAYOUT, 0, 0, 1, 1)
        self.GRID.addLayout(self.PROJECT_DEV_NAME_LAYOUT, 1, 0, 1, 1)
        self.GRID.addLayout(self.PROJECT_LOCATION_LAYOUT, 2, 0, 1, 1)
        self.GRID.addWidget(self.APPLY_BUTTON, 3, 0, 1, 1)
        self.GRID.addWidget(self.OPEN_BUTTON, 4, 0, 1, 1)
        self.GRID.addWidget(self.STATUS_LABEL, 5, 0, 1, 1)
        self.setLayout(self.GRID)

    def updateUI(self):
        pass

    def CLICKED_PROJECT_LOCATION_FILE_DIALOG_BUTTON(self):
        f = self.PROJECT_LOCATION_FILE_DIALOG.getExistingDirectory(
            self, "Select Directory"
        )

        if f:
            self.PROJECT_LOCATION_LINEEDIT.setText(f)

    def CLICKED_APPLY_BUTTON(self):
        if (
            self.PROJECT_NAME_LINEEDIT.text()
            and self.PROJECT_DEV_NAME_LINEEDIT.text()
            and self.PROJECT_LOCATION_LINEEDIT.text()
        ):
            ENGINE = Boltzmann_engine.Boltzmann_Engine_GUI(
                PROJECT_PATH=self.PROJECT_LOCATION_LINEEDIT.text(),
                PROJECT_NAME=self.PROJECT_NAME_LINEEDIT.text(),
                DEV_NAME=self.PROJECT_DEV_NAME_LINEEDIT.text(),
            )
            ENGINE.showMaximized()
            self.close()

        else:
            self.STATUS_LABEL.setText("Please write the right information")

    def CLICKED_OPEN_BUTTON(self):
        f = self.PROJECT_LOCATION_FILE_DIALOG.getExistingDirectory(
            self, "Select Directory"
        )

        if f:
            pass


if __name__ == "__main__":
    Boltzmann_Q_App = QApplication()
    Boltzmann_app_GUI = Boltzmann_GUI()
    Boltzmann_app_GUI.show()
    sys.exit(Boltzmann_Q_App.exec())
