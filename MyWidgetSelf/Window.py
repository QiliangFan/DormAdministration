from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MyWidgetSelf.Button import *
import MyWidgetSelf.Button
from DDL.query import *
from DDL.insert import *
from MyWidgetSelf.subWindow import *
import sys


# 学生操作界面
class stuWindow(QWidget):
    def __init__(self, account, parent=None):
        super(stuWindow, self).__init__(parent)
        self.pix = QPixmap("./src/image/stuWindow.png")
        self.setWindow()
        self.account = account
        self.first = firstWindow(self.account, self)
        self.second = secondWindow(self.account, self)
        self.second.hide()
        self.third = thirdWindow(self.account, self)
        self.third.hide()
        self.forth = forthWindow(self.account, self)
        self.forth.hide()
        self.account_label = QLabel(self)
        self.iniButton()
        self.initSignalSlot()
        self.iniWindow()
        self.iniLabel()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.setGeometry(QDesktopWidget().geometry().width() / 2 - self.width() / 2,
                         QDesktopWidget().geometry().height() / 2 - self.height() / 2,
                         self.width(),
                         self.height())

    def iniWindow(self):
        self.first.setGeometry(300, 100, 900, 800)
        self.second.setGeometry(300, 100, 900, 800)
        self.third.setGeometry(300, 100, 900, 800)
        self.forth.setGeometry(300, 100, 900, 800)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def initSignalSlot(self):
        pass

    def getAccount(self, account):
        self.account = account

    def iniLabel(self):
        f = QFont()
        f.setBold(True)
        self.account_label.setFont(f)
        self.account_label.setText("%s" % (self.account,))
        self.account_label.setGeometry(950, 11, 200, 50)
        self.account_label.setVisible(True)

    def iniButton(self):
        self.firstButton = QPushButton(self)
        self.secondButton = QPushButton(self)
        self.thirdButton = QPushButton(self)
        self.forthButton = QPushButton(self)
        self.firstButton.setGeometry(50, 110, 200, 40)
        self.secondButton.setGeometry(50, 210, 200, 40)
        self.thirdButton.setGeometry(50, 260, 200, 40)
        self.forthButton.setGeometry(50, 310, 200, 40)
        self.firstButton.setStyleSheet("background:transparent;")
        self.secondButton.setStyleSheet("background:transparent;")
        self.thirdButton.setStyleSheet("background:transparent;")
        self.forthButton.setStyleSheet("background:transparent;")

        self.firstButton.setCursor(Qt.PointingHandCursor)
        self.secondButton.setCursor(Qt.PointingHandCursor)
        self.thirdButton.setCursor(Qt.PointingHandCursor)
        self.forthButton.setCursor(Qt.PointingHandCursor)

        self.firstButton.clicked.connect(self.first.show)
        self.firstButton.clicked.connect(self.second.hide)
        self.firstButton.clicked.connect(self.third.hide)
        self.firstButton.clicked.connect(self.forth.hide)

        self.secondButton.clicked.connect(self.first.hide)
        self.secondButton.clicked.connect(self.second.show)
        self.secondButton.clicked.connect(self.third.hide)
        self.secondButton.clicked.connect(self.forth.hide)

        self.thirdButton.clicked.connect(self.first.hide)
        self.thirdButton.clicked.connect(self.second.hide)
        self.thirdButton.clicked.connect(self.third.show)
        self.thirdButton.clicked.connect(self.forth.hide)

        self.forthButton.clicked.connect(self.first.hide)
        self.forthButton.clicked.connect(self.second.hide)
        self.forthButton.clicked.connect(self.third.hide)
        self.forthButton.clicked.connect(self.forth.show)

        self.exitButton = QPushButton(self)
        self.exitButton.setGeometry(900, 20, 200, 50)
        self.exitButton.setCursor(Qt.PointingHandCursor)
        self.exitButton.setStyleSheet("background:transparent;")
        self.exitButton.clicked.connect(self.exit)

    def exit(self):
        sys.exit(0)


# 管理员操作界面
class teaWindow(QWidget):
    def __init__(self, account, parent=None):
        super(teaWindow, self).__init__(parent)
        self.pix = QPixmap("./src/image/teaWindow.png")
        self.account = account
        self.first = managerfirstWindow(self.account, self)
        self.second = managersecondWindow(self.account, self)
        self.third=managerthirdWindow(self.account,self)
        self.forth=managerforthWindow(self.account,self)
        self.fifth=managerfifthWindow(self.account,self)
        self.sixth=managersixthWindow(self.account,self)
        self.seventh=managerseventhWindow(self.account,self)
        self.eighth=managereightWindow(self.account,self)
        self.ninth=managerninthWindow(self.account,self)
        self.tenth=managertenthWindow(self.account,self)
        self.eleventh=managereleventhWindow(self.account,self)
        self.setWindow()
        self.iniWindow()
        self.iniLabelEdit()
        self.iniButton()
        self.iniSignalSlot()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.setGeometry(QDesktopWidget().geometry().width() / 2 - self.width() / 2,
                         QDesktopWidget().geometry().height() / 2 - self.height() / 2,
                         self.pix.width(),
                         self.pix.height())

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def getAccount(self, account):
        self.account = account

    def iniButton(self):
        self.firstButton = QPushButton(self)
        self.firstButton.setGeometry(50, 100, 200, 50)
        self.firstButton.setCursor(Qt.PointingHandCursor)
        self.firstButton.setStyleSheet("background:transparent;")
        self.secondButton=QPushButton(self)
        self.secondButton.setGeometry(50, 200, 200, 30)
        self.secondButton.setCursor(Qt.PointingHandCursor)
        self.secondButton.setStyleSheet("background:transparent;")
        self.thirdButton=QPushButton(self)
        self.thirdButton.setGeometry(50,250,200,30)
        self.thirdButton.setCursor(Qt.PointingHandCursor)
        self.thirdButton.setStyleSheet("background:transparent;")

        self.forthButton=QPushButton(self)
        self.forthButton.setGeometry(50, 290, 200, 30)
        self.forthButton.setCursor(Qt.PointingHandCursor)
        self.forthButton.setStyleSheet("background:transparent;")

        self.fifthButton = QPushButton(self)
        self.fifthButton.setGeometry(50, 330, 200, 30)
        self.fifthButton.setCursor(Qt.PointingHandCursor)
        self.fifthButton.setStyleSheet("background:transparent;")

        self.sixthButton = QPushButton(self)
        self.sixthButton.setGeometry(50, 420, 200, 30)
        self.sixthButton.setCursor(Qt.PointingHandCursor)
        self.sixthButton.setStyleSheet("background:transparent;")

        self.seventhButton = QPushButton(self)
        self.seventhButton.setGeometry(50, 460, 200, 30)
        self.seventhButton.setCursor(Qt.PointingHandCursor)
        self.seventhButton.setStyleSheet("background:transparent;")

        self.eighthButton = QPushButton(self)
        self.eighthButton.setGeometry(50, 550, 200, 30)
        self.eighthButton.setCursor(Qt.PointingHandCursor)
        self.eighthButton.setStyleSheet("background:transparent;")

        self.ninthButton = QPushButton(self)
        self.ninthButton.setGeometry(50, 590, 200, 30)
        self.ninthButton.setCursor(Qt.PointingHandCursor)
        self.ninthButton.setStyleSheet("background:transparent;")

        self.tenthButton = QPushButton(self)
        self.tenthButton.setGeometry(50, 635, 200, 30)
        self.tenthButton.setCursor(Qt.PointingHandCursor)
        self.tenthButton.setStyleSheet("background:transparent;")

        self.eleventhButton=QPushButton(self)
        self.eleventhButton.setGeometry(50, 675, 200, 30)
        self.eleventhButton.setCursor(Qt.PointingHandCursor)
        self.eleventhButton.setStyleSheet("background:transparent;")

        self.exitButton = QPushButton(self)
        self.exitButton.setGeometry(850, 20, 400, 50)
        self.exitButton.setCursor(Qt.PointingHandCursor)
        self.exitButton.setStyleSheet("background:transparent;")
        self.exitButton.clicked.connect(self.exit)

    def iniLabelEdit(self):
        self.accLabel=QLabel(self)
        self.accLabel.setText(str(self.account))
        self.accLabel.setGeometry(950,20,100,30)

    def exit(self):
        sys.exit(0)

    def iniSignalSlot(self):
        self.firstButton.clicked.connect(self.first.show)
        self.firstButton.clicked.connect(self.second.hide)
        self.firstButton.clicked.connect(self.third.hide)
        self.firstButton.clicked.connect(self.forth.hide)
        self.firstButton.clicked.connect(self.fifth.hide)
        self.firstButton.clicked.connect(self.sixth.hide)
        self.firstButton.clicked.connect(self.seventh.hide)
        self.firstButton.clicked.connect(self.eighth.hide)
        self.firstButton.clicked.connect(self.ninth.hide)
        self.firstButton.clicked.connect(self.tenth.hide)
        self.firstButton.clicked.connect(self.eleventh.hide)

        self.secondButton.clicked.connect(self.first.hide)
        self.secondButton.clicked.connect(self.second.show)
        self.secondButton.clicked.connect(self.third.hide)
        self.secondButton.clicked.connect(self.forth.hide)
        self.secondButton.clicked.connect(self.fifth.hide)
        self.secondButton.clicked.connect(self.sixth.hide)
        self.secondButton.clicked.connect(self.seventh.hide)
        self.secondButton.clicked.connect(self.eighth.hide)
        self.secondButton.clicked.connect(self.ninth.hide)
        self.secondButton.clicked.connect(self.tenth.hide)
        self.secondButton.clicked.connect(self.eleventh.hide)

        self.thirdButton.clicked.connect(self.first.hide)
        self.thirdButton.clicked.connect(self.second.hide)
        self.thirdButton.clicked.connect(self.third.show)
        self.thirdButton.clicked.connect(self.forth.hide)
        self.thirdButton.clicked.connect(self.fifth.hide)
        self.thirdButton.clicked.connect(self.sixth.hide)
        self.thirdButton.clicked.connect(self.seventh.hide)
        self.thirdButton.clicked.connect(self.eighth.hide)
        self.thirdButton.clicked.connect(self.ninth.hide)
        self.thirdButton.clicked.connect(self.tenth.hide)
        self.thirdButton.clicked.connect(self.eleventh.hide)

        self.forthButton.clicked.connect(self.first.hide)
        self.forthButton.clicked.connect(self.second.hide)
        self.forthButton.clicked.connect(self.third.hide)
        self.forthButton.clicked.connect(self.forth.show)
        self.forthButton.clicked.connect(self.fifth.hide)
        self.forthButton.clicked.connect(self.sixth.hide)
        self.forthButton.clicked.connect(self.seventh.hide)
        self.forthButton.clicked.connect(self.eighth.hide)
        self.forthButton.clicked.connect(self.ninth.hide)
        self.forthButton.clicked.connect(self.tenth.hide)
        self.forthButton.clicked.connect(self.eleventh.hide)

        self.fifthButton.clicked.connect(self.first.hide)
        self.fifthButton.clicked.connect(self.second.hide)
        self.fifthButton.clicked.connect(self.third.hide)
        self.fifthButton.clicked.connect(self.forth.hide)
        self.fifthButton.clicked.connect(self.fifth.show)
        self.fifthButton.clicked.connect(self.sixth.hide)
        self.fifthButton.clicked.connect(self.seventh.hide)
        self.fifthButton.clicked.connect(self.eighth.hide)
        self.fifthButton.clicked.connect(self.ninth.hide)
        self.fifthButton.clicked.connect(self.tenth.hide)
        self.fifthButton.clicked.connect(self.eleventh.hide)

        self.sixthButton.clicked.connect(self.first.hide)
        self.sixthButton.clicked.connect(self.second.hide)
        self.sixthButton.clicked.connect(self.third.hide)
        self.sixthButton.clicked.connect(self.forth.hide)
        self.sixthButton.clicked.connect(self.fifth.hide)
        self.sixthButton.clicked.connect(self.sixth.show)
        self.sixthButton.clicked.connect(self.seventh.hide)
        self.sixthButton.clicked.connect(self.eighth.hide)
        self.sixthButton.clicked.connect(self.ninth.hide)
        self.sixthButton.clicked.connect(self.tenth.hide)
        self.sixthButton.clicked.connect(self.eleventh.hide)

        self.seventhButton.clicked.connect(self.first.hide)
        self.seventhButton.clicked.connect(self.second.hide)
        self.seventhButton.clicked.connect(self.third.hide)
        self.seventhButton.clicked.connect(self.forth.hide)
        self.seventhButton.clicked.connect(self.fifth.hide)
        self.seventhButton.clicked.connect(self.sixth.hide)
        self.seventhButton.clicked.connect(self.seventh.show)
        self.seventhButton.clicked.connect(self.eighth.hide)
        self.seventhButton.clicked.connect(self.ninth.hide)
        self.seventhButton.clicked.connect(self.tenth.hide)
        self.seventhButton.clicked.connect(self.eleventh.hide)

        self.eighthButton.clicked.connect(self.first.hide)
        self.eighthButton.clicked.connect(self.second.hide)
        self.eighthButton.clicked.connect(self.third.hide)
        self.eighthButton.clicked.connect(self.forth.hide)
        self.eighthButton.clicked.connect(self.fifth.hide)
        self.eighthButton.clicked.connect(self.sixth.hide)
        self.eighthButton.clicked.connect(self.seventh.hide)
        self.eighthButton.clicked.connect(self.eighth.show)
        self.eighthButton.clicked.connect(self.ninth.hide)
        self.eighthButton.clicked.connect(self.tenth.hide)
        self.eighthButton.clicked.connect(self.eleventh.hide)

        self.ninthButton.clicked.connect(self.first.hide)
        self.ninthButton.clicked.connect(self.second.hide)
        self.ninthButton.clicked.connect(self.third.hide)
        self.ninthButton.clicked.connect(self.forth.hide)
        self.ninthButton.clicked.connect(self.fifth.hide)
        self.ninthButton.clicked.connect(self.sixth.hide)
        self.ninthButton.clicked.connect(self.seventh.hide)
        self.ninthButton.clicked.connect(self.eighth.hide)
        self.ninthButton.clicked.connect(self.ninth.show)
        self.ninthButton.clicked.connect(self.tenth.hide)
        self.ninthButton.clicked.connect(self.eleventh.hide)

        self.tenthButton.clicked.connect(self.first.hide)
        self.tenthButton.clicked.connect(self.second.hide)
        self.tenthButton.clicked.connect(self.third.hide)
        self.tenthButton.clicked.connect(self.forth.hide)
        self.tenthButton.clicked.connect(self.fifth.hide)
        self.tenthButton.clicked.connect(self.sixth.hide)
        self.tenthButton.clicked.connect(self.seventh.hide)
        self.tenthButton.clicked.connect(self.eighth.hide)
        self.tenthButton.clicked.connect(self.ninth.hide)
        self.tenthButton.clicked.connect(self.tenth.show)
        self.tenthButton.clicked.connect(self.eleventh.hide)

        self.eleventhButton.clicked.connect(self.first.hide)
        self.eleventhButton.clicked.connect(self.second.hide)
        self.eleventhButton.clicked.connect(self.third.hide)
        self.eleventhButton.clicked.connect(self.forth.hide)
        self.eleventhButton.clicked.connect(self.fifth.hide)
        self.eleventhButton.clicked.connect(self.sixth.hide)
        self.eleventhButton.clicked.connect(self.seventh.hide)
        self.eleventhButton.clicked.connect(self.eighth.hide)
        self.eleventhButton.clicked.connect(self.ninth.hide)
        self.eleventhButton.clicked.connect(self.tenth.hide)
        self.eleventhButton.clicked.connect(self.eleventh.show)


    def iniWindow(self):
        self.first.setGeometry(300, 100, 900, 800)
        self.first.show()
        self.second.setGeometry(300, 100, 900, 800)
        self.second.hide()
        self.third.setGeometry(300, 100, 900, 800)
        self.third.hide()
        self.forth.setGeometry(300, 100, 900, 800)
        self.forth.hide()
        self.fifth.setGeometry(300, 100, 900, 800)
        self.fifth.hide()
        self.sixth.setGeometry(300, 100, 900, 800)
        self.sixth.hide()
        self.seventh.setGeometry(300, 100, 900, 800)
        self.seventh.hide()
        self.eighth.setGeometry(300, 100, 900, 800)
        self.eighth.hide()
        self.ninth .setGeometry(300, 100, 900, 800)
        self.ninth.hide()
        self.tenth .setGeometry(300, 100, 900, 800)
        self.tenth.hide()
        self.eleventh .setGeometry(300, 100, 900, 800)
        self.eleventh.hide()


# 学生登陆界面
class stulogWindow(QWidget):
    success = pyqtSignal()

    def __init__(self, parent=None):
        super(stulogWindow, self).__init__(parent)

        self.pix = QPixmap("./src/image/loginWindow.png")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.setAttribute(Qt.WA_TranslucentBackground)

        # return
        self.ReturnFromLog = MyWidgetSelf.Button.returnFromLog(self)
        self.ReturnFromLog.setGeometry(self.width() / 2 - 3.2 * self.ReturnFromLog.width(),
                                       self.height() / 2 + 0.2 * self.ReturnFromLog.height(),
                                       self.ReturnFromLog.width(),
                                       self.ReturnFromLog.height())
        self.ReturnFromLog.clicked.connect(self.close)

        # logup
        self.logupbutton = MyWidgetSelf.Button.logup(self)
        self.logupbutton.setGeometry(self.width() / 2 + 1.8 * self.logupbutton.width(),
                                     self.height() / 2 - 0.2 * self.logupbutton.height(),
                                     self.logupbutton.width(),
                                     self.logupbutton.height())

        # login
        self.loginbutton = MyWidgetSelf.Button.login(self)
        self.loginbutton.setGeometry(self.width() / 2 - 0.5 * self.loginbutton.width(),
                                     self.height() / 2 + 0.4 * self.loginbutton.height(),
                                     self.loginbutton.width(),
                                     self.loginbutton.height())

        # account
        self.account = QLineEdit(self)
        self.account.setGeometry(self.width() / 2 - 1.8 * self.account.width() / 2,
                                 self.height() / 2 - 1.2 * self.account.height(),
                                 240, 35)
        self.account.setStyleSheet("background:transparent;bord-width:0;border-style:outset")
        f = QFont()
        f.setBold(True)
        self.account.setFont(f)
        self.account.setPlaceholderText("请输入账号")

        # password
        self.pwd = QLineEdit(self)
        self.pwd.setGeometry(self.width() / 2 - 1.8 * self.pwd.width() / 2,
                             self.height() / 2 + 1.5 * self.pwd.height(),
                             240, 35)
        self.pwd.setStyleSheet("background:transparent;bord-width:0;border-style:outset;")
        self.pwd.setEchoMode(QLineEdit.Password)
        self.pwd.setPlaceholderText("请输入密码")
        self.pwd.setFont(f)
        self.logupWIn = logupWindowStu()
        self.submit_login()
        self.initSignalSlot()
        self.login()

    def submit_login(self):
        self.logupWIn.success.connect(self.logupWIn.close)
        self.logupWIn.success.connect(self.show)

    def initSignalSlot(self):
        self.logupbutton.clicked.connect(self.account.clear)
        self.ReturnFromLog.clicked.connect(self.account.clear)
        self.logupbutton.clicked.connect(self.pwd.clear)
        self.ReturnFromLog.clicked.connect(self.pwd.clear)

        ###
        self.logupbutton.clicked.connect(self.logupWIn.show)
        self.logupbutton.clicked.connect(self.hide)

        self.logupWIn.cancel.clicked.connect(self.show)
        self.logupWIn.cancel.clicked.connect(self.logupWIn.close)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Return:
            self.loginbutton.clicked.emit()

    def login(self):
        self.loginbutton.clicked.connect(self.verify)

    def verify(self):
        if self.account.text() == "" or self.pwd.text() == "" or len(selectAllByAccount(self.account.text())) == 0 \
                or selectTypeByAccount(self.account.text()) != "student" \
                or self.pwd.text() != selectPwdByAccount(self.account.text()):
            self.mes = QMessageBox()
            self.mes.setWindowTitle("注意")
            self.mes.setText("密码错误或用户名不存在")
            self.account.clear()
            self.pwd.clear()
            self.mes.show()
        else:
            self.stuOperate = stuWindow(self.account.text())
            self.pwd.clear()
            self.account.clear()
            self.stuOperate.show()
            self.stuOperate.getAccount(self.account.text())
            self.hide()


# 老师登陆界面
class tealogWindow(QWidget):
    def __init__(self, parent=None):
        super(tealogWindow, self).__init__(parent)
        self.pix = QPixmap("./src/image/loginWindow2.png")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.setGeometry(QDesktopWidget().geometry().width() / 2 - self.width() / 2,
                         QDesktopWidget().geometry().height() / 2 - self.height() / 2,
                         self.pix.width(),
                         self.pix.height())
        self.logupButton = logupButtonTea(self)
        self.loginButton = loginbuttonTea(self)
        self.returnback = returnButtonTea(self)
        self.logupButton.setGeometry(self.width() / 2 + 3.4 * self.logupButton.width(),
                                     self.height() / 2 + 2.3 * self.logupButton.height(),
                                     self.logupButton.width(),
                                     self.logupButton.height())
        self.loginButton.setGeometry(self.width() / 2 - 3.7 * self.loginButton.width(),
                                     self.height() / 2 + 1.8 * self.loginButton.height(),
                                     self.loginButton.width(),
                                     self.loginButton.height())
        self.returnback.setGeometry(self.width() / 2 + 1.6 * self.returnback.width(),
                                    self.height() / 2 + 2.7 * self.returnback.height(),
                                    self.returnback.width(),
                                    self.returnback.height())
        self.account = QLineEdit(self)
        self.pwd = QLineEdit(self)
        self.logupWin = logupWindowTea()

        self.submit_login()
        self.logupButton.clicked.connect(self.logupWin.show)
        self.logupButton.clicked.connect(self.hide)

        self.logupWin.cancel.clicked.connect(self.show)
        self.logupWin.cancel.clicked.connect(self.logupWin.close)

        f = QFont()
        f.setBold(True)
        self.account.setFont(f)
        self.login()

    def submit_login(self):
        self.account.setPlaceholderText("请输入账号")
        self.pwd.setPlaceholderText("请输入密码")
        self.pwd.setEchoMode(QLineEdit.Password)
        self.account.setStyleSheet("background:transparent;bord-width:0;border-style:outset")
        self.pwd.setStyleSheet("background:transparent;bord-width:0;border-style:outset")
        f = QFont()
        f.setBold(True)
        self.account.setFont(f)
        self.pwd.setFont(f)
        self.pwd.setGeometry(self.width() / 2 - 2.9 * self.pwd.width(),
                             self.height() / 2 + 5.5 * self.pwd.height(),
                             280,
                             50)
        self.account.setGeometry(self.width() / 2 - 2.9 * self.account.width(),
                                 self.height() / 2 + 2.5 * self.account.height(),
                                 280,
                                 50)

        self.logupButton.clicked.connect(self.account.clear)
        self.logupButton.clicked.connect(self.pwd.clear)
        self.returnback.clicked.connect(self.account.clear)
        self.returnback.clicked.connect(self.pwd.clear)
        self.logupWin.success.connect(self.logupWin.close)
        self.logupWin.success.connect(self.show)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Return:
            self.loginbutton.clicked.emit()

    def login(self):
        self.loginButton.clicked.connect(self.verify)

    def verify(self):
        if self.account.text() == "" or self.pwd.text() == "" or len(selectAllByAccount(self.account.text())) == 0 \
                or selectTypeByAccount(self.account.text()) != "manager" \
                or self.pwd.text() != selectPwdByAccount(self.account.text()):
            self.mes = QMessageBox()
            self.mes.setWindowTitle("注意")
            self.mes.setText("密码错误或用户名不存在")
            self.account.clear()
            self.pwd.clear()
            self.mes.show()
        else:
            self.teaOperate = teaWindow(self.account.text())
            self.pwd.clear()
            self.account.clear()
            self.teaOperate.show()
            self.hide()


# 学生注册页面
class logupWindowStu(QWidget):
    success = pyqtSignal()

    def __init__(self, parent=None):
        super(logupWindowStu, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pix = QPixmap("./src/image/logupWidget.png")
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

        # 注册
        self.account = QLineEdit(self)
        self.pwd = QLineEdit(self)
        self.pwd_re = QLineEdit(self)
        self.account.setGeometry(self.width() / 2 - 1.3 * self.account.width(),
                                 self.height() / 2 - 4.4 * self.account.height(),
                                 230,
                                 50)
        self.pwd.setGeometry(self.width() / 2 - 1.3 * self.pwd.width(),
                             self.height() / 2 - 1.3 * self.pwd.height(),
                             230,
                             50)
        self.pwd_re.setGeometry(self.width() / 2 - 1.3 * self.pwd_re.width(),
                                self.height() / 2 + 1.7 * self.pwd_re.height(),
                                230,
                                50)
        self.account.setStyleSheet("background:transparent;bord-width:0;border-style:outset")
        self.pwd.setStyleSheet("background:transparent;bord-width:0;border-style:outset")
        self.pwd_re.setStyleSheet("background:transparent;bord-width:0;border-style:outset")
        self.pwd.setEchoMode(QLineEdit.Password)
        self.pwd_re.setEchoMode(QLineEdit.Password)
        f = QFont()
        f.setBold(True)
        self.account.setFont(f)

        self.submit = submitButton(self)
        self.submit.setGeometry(self.width() / 2 - 1.4 * self.submit.width(),
                                self.height() / 2 + 0.8 * self.submit.height(),
                                self.submit.width(),
                                self.submit.height())
        self.cancel = cancelButton(self)
        self.cancel.setGeometry(self.width() / 2,
                                self.height() / 2 + 0.8 * self.submit.height(),
                                self.cancel.width(),
                                self.cancel.height())
        self.account.setValidator(QIntValidator())
        self.cancel.clicked.connect(self.account.clear)
        self.cancel.clicked.connect(self.pwd.clear)
        self.cancel.clicked.connect(self.pwd_re.clear)
        self.submit_form()

    def submit_form(self):
        self.submit.clicked.connect(self.verify)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def verify(self):
        if self.account.text() == '' or self.pwd.text() == '' or self.pwd_re.text() == '' or self.pwd.text() != self.pwd_re.text() or len(
                selectAllByAccount(
                    self.account.text())) > 0:  # 验证不通过
            self.warning = QMessageBox()
            self.account.clear()
            self.pwd.clear()
            self.pwd_re.clear()
            self.warning.setWindowTitle("注意")
            self.warning.setText("两次密码输入不匹配或者用户名已存在")
            self.warning.show()

        else:  # 验证通过
            insertNewStu(self.account.text(), self.pwd.text())
            self.account.clear()
            self.pwd.clear()
            self.pwd_re.clear()
            self.success.emit()


# 老师注册界面
class logupWindowTea(QWidget):
    success = pyqtSignal()

    def __init__(self, parent=None):
        super(logupWindowTea, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pix = QPixmap("./src/image/logupWidget.png")
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.submit = submitButton(self)
        self.submit.setGeometry(self.width() / 2 - 1.4 * self.submit.width(),
                                self.height() / 2 + 0.8 * self.submit.height(),
                                self.submit.width(),
                                self.submit.height())
        self.cancel = cancelButton(self)
        self.cancel.setGeometry(self.width() / 2,
                                self.height() / 2 + 0.8 * self.submit.height(),
                                self.cancel.width(),
                                self.cancel.height())
        # 注册
        self.account = QLineEdit(self)
        self.pwd = QLineEdit(self)
        self.pwd_re = QLineEdit(self)
        self.account.setGeometry(self.width() / 2 - 1.3 * self.account.width(),
                                 self.height() / 2 - 4.4 * self.account.height(),
                                 230,
                                 50)
        self.pwd.setGeometry(self.width() / 2 - 1.3 * self.pwd.width(),
                             self.height() / 2 - 1.3 * self.pwd.height(),
                             230,
                             50)
        self.pwd_re.setGeometry(self.width() / 2 - 1.3 * self.pwd_re.width(),
                                self.height() / 2 + 1.7 * self.pwd_re.height(),
                                230,
                                50)
        self.account.setStyleSheet("background:transparent;bord-width:0;border-style:outset")
        self.pwd.setStyleSheet("background:transparent;bord-width:0;border-style:outset")
        self.pwd_re.setStyleSheet("background:transparent;bord-width:0;border-style:outset")
        self.pwd.setEchoMode(QLineEdit.Password)
        self.pwd_re.setEchoMode(QLineEdit.Password)
        f = QFont()
        f.setBold(True)
        self.account.setFont(f)

        self.account.setValidator(QIntValidator())
        self.cancel.clicked.connect(self.account.clear)
        self.cancel.clicked.connect(self.pwd.clear)
        self.cancel.clicked.connect(self.pwd_re.clear)
        self.submit_form()

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def submit_form(self):
        self.submit.clicked.connect(self.verify)

    def verify(self):
        if self.account.text() == '' or self.pwd.text() == '' or self.pwd_re.text() == '' or self.pwd.text() != self.pwd_re.text() or len(
                selectAllByAccount(
                    self.account.text())) > 0:  # 验证不通过
            self.warning = QMessageBox()
            self.warning.setWindowTitle("注意")
            self.warning.setText("两次密码输入不匹配或者用户名已存在")
            self.warning.show()
            self.account.clear
            self.pwd.clear
            self.pwd_re.clear
        else:  # 验证通过
            insertNewTea(self.account.text(), self.pwd.text())
            self.account.clear
            self.pwd.clear
            self.pwd_re.clear
            self.success.emit()
