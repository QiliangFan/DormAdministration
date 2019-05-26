from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MyWidgetSelf.Button import *
import MyWidgetSelf.Button
from DDL.query import *

#主界面
class MainWindow(QWidget):
    pass

# 学生登陆界面
class stulogWindow(QWidget):
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
        self.initSignalSlot()

    def submit_login(self):
        pass

    def initSignalSlot(self):
        self.logupbutton.clicked.connect(self.account.clear)
        self.ReturnFromLog.clicked.connect(self.account.clear)
        self.logupbutton.clicked.connect(self.pwd.clear)
        self.ReturnFromLog.clicked.connect(self.pwd.clear)

        ##########
        self.loginbutton.clicked.connect(self.account.clear)
        self.loginbutton.clicked.connect(self.pwd.clear)

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

        self.loginButton.clicked.connect(self.account.clear)
        self.loginButton.clicked.connect(self.pwd.clear)
        self.logupButton.clicked.connect(self.account.clear)
        self.logupButton.clicked.connect(self.pwd.clear)
        self.returnback.clicked.connect(self.account.clear)
        self.returnback.clicked.connect(self.pwd.clear)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Return:
            self.loginbutton.clicked.emit()


# 学生注册页面
class logupWindowStu(QWidget):
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
        self.submit_form()


    def submit_form(self):
        self.submit.clicked.connect(self.verify)
        self.submit.clicked.connect(self.account.clear)
        self.submit.clicked.connect(self.pwd.clear)
        self.submit.clicked.connect(self.pwd_re.clear)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def verify(self):
        if self.pwd.text() != self.pwd_re.text() or len(selectAllByAccount(self.account.text()) ) >0:#验证不通过
            self.warning=QMessageBox()
            self.warning.setWindowTitle("注意")
            self.warning.setText("两次密码输入不匹配或者用户名已存在")
            self.warning.show()
        else:  #验证通过
            pass

# 老师注册界面
class logupWindowTea(QWidget):
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
        self.submit_form()


    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def submit_form(self):
        self.submit.clicked.connect(self.verify)
        self.submit.clicked.connect(self.account.clear)
        self.submit.clicked.connect(self.pwd.clear)
        self.submit.clicked.connect(self.pwd_re.clear)

    def verify(self):

        if self.pwd.text() != self.pwd_re.text() or len(selectAllByAccount(self.account.text()) ) >0:#验证不通过
            self.warning=QMessageBox()
            self.warning.setWindowTitle("注意")
            self.warning.setText("两次密码输入不匹配或者用户名已存在")
            self.warning.show()
        else:  #验证通过
            pass

