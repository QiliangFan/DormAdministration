from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#老师登陆按钮
class loginbuttonTea(QPushButton):
    def __init__(self, parent=None):
        super(loginbuttonTea, self).__init__(parent)
        self.pix = QPixmap("./src/image/buttonLogin.png")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setCursor(Qt.PointingHandCursor)

    def paintEvent(self, QPaintEvent):
        super().paintEvent(QPaintEvent)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

#老师登陆界面返回
class returnButtonTea(QPushButton):
    def __init__(self, parent=None):
        super(returnButtonTea, self).__init__(parent)
        self.pix = QPixmap("./src/image/buttonExit.png")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setCursor(Qt.PointingHandCursor)

    def paintEvent(self, QPaintEvent):
        super().paintEvent(QPaintEvent)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

#主界面退出
class exitButton2(QPushButton):
    def __init__(self, parent=None):
        super(exitButton2, self).__init__(parent)
        self.pix = QPixmap("./src/image/exitButton2.png")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.setCursor(Qt.PointingHandCursor)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

#教师注册
class logupButtonTea(QPushButton):
    def __init__(self, parent=None):
        super(logupButtonTea, self).__init__(parent)
        self.pix = QPixmap("./src/image/buttonLogupTea.png")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.setAttribute(Qt.WA_TranslucentBackground)
        f = QFont("Microsoft YaHei")
        f.setBold(True)
        self.setFont(f)
        self.setCursor(Qt.PointingHandCursor)

    def paintEvent(self, QPaintEvent):
        super().paintEvent(QPaintEvent)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

#学生登陆
class login(QPushButton):
    def __init__(self, parent=None):
        super(login, self).__init__(parent)
        self.pix = QPixmap("./src/image/login.png")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.setAttribute(Qt.WA_TranslucentBackground)
        f = QFont("Microsoft YaHei")
        f.setBold(True)
        self.setFont(f)
        self.setCursor(Qt.PointingHandCursor)

    def paintEvent(self, QPaintEvent):
        super().paintEvent(QPaintEvent)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

#学生注册
class logup(QPushButton):
    def __init__(self, parent=None):
        super(logup, self).__init__(parent)
        self.pix = QPixmap("./src/image/logup.png")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.setAttribute(Qt.WA_TranslucentBackground)
        f = QFont("Microsoft YaHei")
        f.setBold(True)
        self.setFont(f)
        self.setCursor(Qt.PointingHandCursor)

    def paintEvent(self, QPaintEvent):
        super().paintEvent(QPaintEvent)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

#学生登陆返回
class returnFromLog(QPushButton):
    def __init__(self, parent=None):
        super(returnFromLog, self).__init__(parent)
        self.pix = QPixmap("./src/image/returnFromLogin.png")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.setAttribute(Qt.WA_TranslucentBackground)
        f = QFont("Microsoft YaHei")
        f.setBold(True)
        self.setFont(f)
        self.setCursor(Qt.PointingHandCursor)

    def paintEvent(self, QPaintEvent):
        super().paintEvent(QPaintEvent)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

#注册确认按钮
class submitButton(QPushButton):
    def __init__(self,parent=None):
        super(submitButton,self).__init__(parent)
        self.pix=QPixmap("./src/image/submitButton.png")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.setCursor(Qt.PointingHandCursor)

    def paintEvent(self, QPaintEvent):
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),self.pix)

#注册取消按钮
class cancelButton(QPushButton):
    def __init__(self,parent=None):
        super(cancelButton,self).__init__(parent)
        self.pix=QPixmap("./src/image/cancelButton.png")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.setCursor(Qt.PointingHandCursor)

    def paintEvent(self, QPaintEvent):
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),self.pix)