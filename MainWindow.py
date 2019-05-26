from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from MyWidgetSelf.Button import *
from MyWidgetSelf.Window import *


class chooseWindow(QWidget):
    def __init__(self, parent=None):
        super(chooseWindow, self).__init__(parent)
        self.pix = QPixmap("./src/image/nk.jpg")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.stuButton = QPushButton(self)
        self.teaButton = QPushButton(self)
        self.pixStu = QPixmap("./src/image/student.png")
        self.pixTea = QPixmap("./src/image/professor.png")
        self.stuLabel = QLabel(self)
        self.teaLabel = QLabel(self)
        self.exitButton2 = exitButton2(self)
        self.stuwin = stulogWindow()
        self.teawin = tealogWindow()
        self.init()

    def init(self):
        self.resize(self.pix.size())
        self.setGeometry(QDesktopWidget().geometry().width() / 2 - self.width() / 2,
                         QDesktopWidget().geometry().height() / 2 - self.height() / 2,
                         self.width(),
                         self.height())
        self.stuButton.resize(200, 100)
        self.teaButton.resize(200, 100)
        self.stuButton.setGeometry(self.width() / 2 - 2 * self.stuButton.width(), self.height() / 2,
                                   self.stuButton.width(), self.stuButton.height())
        self.teaButton.setGeometry(self.width() / 2 + self.teaButton.width(), self.height() / 2, self.teaButton.width(),
                                   self.teaButton.height())
        self.stuButton.setText("学生登陆")
        self.teaButton.setText("管理员登陆")
        self.stuButton.setStyleSheet(
            "background-color:rgb(126, 12, 110);font-size:40px;bord-width:0;border-style:outset;font:bold;font-size:20px;")
        self.teaButton.setStyleSheet(
            "background-color:rgb(126, 12, 110);font-size:40px;bord-width:0;border-style:outset;font:bold;font-size:20px;")
        self.stuButton.setCursor(Qt.PointingHandCursor)
        self.teaButton.setCursor(Qt.PointingHandCursor)
        self.stuLabel.setPixmap(self.pixStu)
        self.teaLabel.setPixmap(self.pixTea)
        self.stuLabel.resize(self.pixStu.size())
        self.teaLabel.resize(self.pixTea.size())
        self.teaLabel.setGeometry(self.width() / 2 + 1.4 * self.teaLabel.width(),
                                  self.height() / 2 - self.teaLabel.height(),
                                  self.teaLabel.width(), self.teaLabel.height())
        self.stuLabel.setGeometry(self.width() / 2 - 2.6 * self.stuLabel.width(),
                                  self.height() / 2 - self.stuLabel.height(),
                                  self.stuLabel.width(), self.stuLabel.height())
        self.exitButton2.setGeometry(self.width() / 2 - self.exitButton2.width() / 2,
                                     self.exitButton2.height() / 2,
                                     self.exitButton2.width(),
                                     self.exitButton2.height())
        self.exitButton2.clicked.connect(self.close)
        self.exitButton2.setToolTip("点击以关闭程序")
        self.stuButton.clicked.connect(self.close)
        self.stuButton.clicked.connect(self.stuwin.show)
        self.stuwin.ReturnFromLog.clicked.connect(self.stuwin.close)
        self.stuwin.ReturnFromLog.clicked.connect(self.show)
        self.teaButton.clicked.connect(self.close)
        self.teaButton.clicked.connect(self.teawin.show)
        self.teawin.returnback.clicked.connect(self.show)
        self.teawin.returnback.clicked.connect(self.teawin.close)
    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)
