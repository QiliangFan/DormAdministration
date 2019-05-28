from DDL.insert import *
from DDL.delete import *
from DDL.query import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# 学生端显示宿舍总体情况
class firstWindow(QWidget):
    def __init__(self, account, parent=None):
        super(firstWindow, self).__init__(parent)
        self.pix = QPixmap("./src/image/1.png")
        self.setWindow()
        self.account = account

        self.student_number = QLabel(self)
        self.teacher_number = QLabel(self)
        self.dorm_number = QLabel(self)
        self.room_number = QLabel(self)
        self.student_in = QLabel(self)
        self.student_canIn = QLabel(self)

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, a0: QPaintEvent) -> None:
        self.iniLabel()
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def getAccount(self, account):
        self.account = account

    def iniLabel(self):
        self.student_number.setText(str(selectNumByType("student")))
        self.student_number.setGeometry(180, 80, 200, 50)
        self.teacher_number.setText(str(selectNumByType("maanger")))
        self.teacher_number.setGeometry(680, 80, 200, 50)
        data = selectRoomBuildingByAccount(self.account)
        if len(data) > 0:
            self.dorm_number.setText(str(selectRoomBuildingByAccount(self.account)))
        else:
            self.dorm_number.setText("++")
        self.dorm_number.setGeometry(140, 290, 200, 50)
        data = selectRoomByAccount(self.account)
        if len(data) > 0:
            self.room_number.setText(str(selectRoomByAccount(self.account)))
        else:
            self.room_number.setText("++")
        self.room_number.setGeometry(420, 290, 200, 50)
        self.student_in.setText(str(selectStudentNumberHasInByAccount(self.account)))
        self.student_in.setGeometry(690, 290, 200, 50)


# 学生端同宿舍人员查询
class secondWindow(QWidget):
    def __init__(self, account, parent=None):
        super(secondWindow, self).__init__(parent)
        self.accouont = account
        self.pix = QPixmap("./src/image/2.png")
        self.building = QLineEdit(self)
        self.room = QLineEdit(self)
        self.status = QLabel(self)
        self.submit = QPushButton(self)
        self.result = QTableWidget(self)
        self.setWindow()
        self.iniWidget()
        self.iniSignalSlot()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def iniWidget(self):
        self.building.setGeometry(90, 70, 160, 30)
        self.room.setGeometry(330, 70, 160, 30)
        self.status.setGeometry(580, 70, 160, 30)
        self.status.setText("状态良好")
        self.submit.setGeometry(680, 70, 160, 30)
        self.submit.setText("查询")
        self.submit.setCursor(Qt.PointingHandCursor)
        self.result.setGeometry(20, 120, 815, 600)
        self.result.horizontalHeader().setDefaultSectionSize(100)
        self.result.verticalHeader().setDefaultSectionSize(30)
        self.result.setColumnCount(8)
        # self.result.setRowCount(20)
        list = [u'学号', u'姓名', u'学院', u'年级', u'出生日期', u'个人电话', u'父母电话', u'床号']
        self.result.setHorizontalHeaderLabels(list)

    def iniSignalSlot(self):
        building = self.building.text()
        room = self.room.text()


# 学生端查询本楼成员
class thirdWindow(QWidget):
    def __init__(self, account, parent=None):
        super(thirdWindow, self).__init__(parent)
        self.account = account
        self.accouont = account
        self.pix = QPixmap("./src/image/3.png")
        self.building = QLineEdit(self)
        self.name = QLineEdit(self)
        self.status = QLabel(self)
        self.submit = QPushButton(self)
        self.result = QTableWidget(self)
        self.setWindow()
        self.iniWidget()
        self.iniSignalSlot()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def iniWidget(self):
        self.building.setGeometry(90, 70, 160, 30)
        self.name.setGeometry(340, 70, 160, 30)
        self.status.setGeometry(580, 70, 160, 30)
        self.status.setText("状态良好")
        self.submit.setGeometry(680, 70, 160, 30)
        self.submit.setText("查询")
        self.submit.setCursor(Qt.PointingHandCursor)
        self.result.setGeometry(20, 120, 810, 600)
        self.result.horizontalHeader().setDefaultSectionSize(160)
        self.result.verticalHeader().setDefaultSectionSize(30)
        self.result.setColumnCount(5)
        # self.result.setRowCount(20)
        list = [u'学号', u'姓名', u'学院', u'年级', u'房间号']
        self.result.setHorizontalHeaderLabels(list)

    def iniSignalSlot(self):
        building = self.building.text()
        name = self.name.text()


# 学生端个人资料面板
class forthWindow(QWidget):
    def __init__(self, account, parent=None):
        super(forthWindow, self).__init__(parent)
        self.account = account
        self.pix = QPixmap("./src/image/4.png")
        self.submit = QPushButton(self)
        self.setWindow()
        self.iniLineEdit()
        self.iniButton()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def iniLineEdit(self):
        self.id = QLineEdit(self)
        self.name = QLineEdit(self)
        self.department_name = QLineEdit(self)
        self.grade = QLineEdit(self)
        self.phoneparent = QLineEdit(self)
        self.phoneself = QLineEdit(self)
        self.gender = QLineEdit(self)
        self.bed_id = QLineEdit(self)
        self.admition_date = QLineEdit(self)
        self.birthday = QLineEdit(self)
        self.id.setGeometry(190, 153, 360, 30)
        self.name.setGeometry(190, 203, 360, 30)
        self.department_name.setGeometry(190, 253, 360, 30)
        self.grade.setGeometry(190, 303, 360, 30)
        self.phoneparent.setGeometry(190, 350, 360, 30)
        self.phoneself.setGeometry(190, 393, 360, 30)
        self.gender.setGeometry(190, 435, 360, 30)
        self.bed_id.setGeometry(190, 490, 360, 30)
        self.admition_date.setGeometry(190, 540, 360, 30)
        self.birthday.setGeometry(190, 600, 360, 30)
        self.id.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.name.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.department_name.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.grade.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.phoneparent.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.phoneself.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.gender.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.bed_id.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.admition_date.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.birthday.setStyleSheet("background:transparent;border-width:0;border-style:outset")

    def iniButton(self):
        self.submit.setGeometry(370, 630, 80, 50)
        self.submit.setCursor(Qt.PointingHandCursor)
        self.submit.setStyleSheet("background:transparent;")


# 管理员端显示宿舍整体情况
class managerfirstWindow(QWidget):
    def __init__(self, account, parent=None):
        super(managerfirstWindow, self).__init__(parent)
        self.pix = QPixmap("./src/image/1.png")
        self.setWindow()
        self.account = account

        self.student_number = QLabel(self)
        self.teacher_number = QLabel(self)
        self.dorm_number = QLabel(self)
        self.room_number = QLabel(self)
        self.student_in = QLabel(self)
        self.student_canIn = QLabel(self)

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, a0: QPaintEvent) -> None:
        self.iniLabel()
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def getAccount(self, account):
        self.account = account

    def iniLabel(self):
        self.student_number.setText(str(selectNumByType("student")))
        self.student_number.setGeometry(180, 80, 200, 50)
        self.teacher_number.setText(str(selectNumByType("maanger")))
        self.teacher_number.setGeometry(680, 80, 200, 50)
        data = selectRoomBuildingByAccount(self.account)
        if len(data) > 0:
            self.dorm_number.setText(str(selectRoomBuildingByAccount(self.account)))
        else:
            self.dorm_number.setText("++")
        self.dorm_number.setGeometry(140, 290, 200, 50)
        data = selectRoomByAccount(self.account)
        if len(data) > 0:
            self.room_number.setText(str(selectRoomByAccount(self.account)))
        else:
            self.room_number.setText("++")
        self.room_number.setGeometry(420, 290, 200, 50)
        self.student_in.setText(str(selectStudentNumberHasInByAccount(self.account)))
        self.student_in.setGeometry(690, 290, 200, 50)


# 同楼管理员信息
class managersecondWindow(QWidget):
    def __init__(self, account, parent=None):
        super(managersecondWindow, self).__init__(parent)
        self.account = account
        self.pix = QPixmap("./src/image/m2.png")
        self.setWindow()
        self.iniTable()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def iniTable(self):
        self.table = QTableWidget(self)
        self.table.setGeometry(20, 120, 810, 600)
        self.table.horizontalHeader().setDefaultSectionSize(160)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['工号', '姓名', '性别', '出生日期', '个人电话'])


# 同楼全部学生信息
class managerthirdWindow(QWidget):
    def __init__(self, account, parent=None):
        super(managerthirdWindow, self).__init__(parent)
        self.pix = QPixmap("./src/image/m3.png")
        self.setWindow()
        self.iniTable()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def iniTable(self):
        self.table = QTableWidget(self)
        self.table.setGeometry(20, 120, 820, 600)
        self.table.horizontalHeader().setDefaultSectionSize(90)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(['学号', '姓名', '性别', '学院', '房间号', '床号', '出生日期', '本人电话', '父母电话'])


# 同楼的某间的学生信息
class managerforthWindow(QWidget):
    def __init__(self, account, parent=None):
        super(managerforthWindow, self).__init__(parent)
        self.pix = QPixmap("./src/image/m4.png")
        self.account = account
        self.setWindow()
        self.iniTable()
        self.iniLineEdit()
        self.iniButton()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def iniTable(self):
        self.table = QTableWidget(self)
        self.table.setGeometry(20, 120, 820, 600)
        self.table.horizontalHeader().setDefaultSectionSize(90)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(['学号', '姓名', '性别', '学院', '房间号', '床号', '出生日期', '本人电话', '父母电话'])

    def iniLineEdit(self):
        self.room = QLineEdit(self)
        self.room.setGeometry(270, 50, 200, 40)

    def iniButton(self):
        self.submit = QPushButton(self)
        self.submit.setGeometry(550, 50, 160, 40)
        self.submit.setText("搜索")
        self.setCursor(Qt.PointingHandCursor)


# 同楼的某学生的信息
class managerfifthWindow(QWidget):
    def __init__(self, account, parent=None):
        super(managerfifthWindow, self).__init__(parent)
        self.pix = QPixmap("./src/image/m5.png")
        self.account = account
        self.setWindow()
        self.iniTable()
        self.iniLineEdit()
        self.iniButton()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def iniTable(self):
        self.table = QTableWidget(self)
        self.table.setGeometry(20, 120, 820, 600)
        self.table.horizontalHeader().setDefaultSectionSize(90)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(['学号', '姓名', '性别', '学院', '房间号', '床号', '出生日期', '本人电话', '父母电话'])

    def iniLineEdit(self):
        self.room = QLineEdit(self)
        self.room.setGeometry(270, 50, 200, 40)

    def iniButton(self):
        self.submit = QPushButton(self)
        self.submit.setGeometry(550, 50, 160, 40)
        self.submit.setText("搜索")
        self.setCursor(Qt.PointingHandCursor)


# 所属楼的可用房间情况
class managersixthWindow(QWidget):
    def __init__(self, account, parent=None):
        super(managersixthWindow, self).__init__(parent)
        self.account = account
        self.pix = QPixmap('./src/image/m6.png')
        self.setWindow()
        self.iniTable()

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def iniTable(self):
        self.table = QTableWidget(self)
        self.table.setGeometry(20, 120, 810, 600)
        self.table.horizontalHeader().setDefaultSectionSize(400)
        self.table.setColumnCount(2)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setHorizontalHeaderLabels(['未满房间号', '剩余床位'])


# 所属楼的某间房间剩余
class managerseventhWindow(QWidget):
    def __init__(self, account, parent=None):
        super(managerseventhWindow, self).__init__(parent)
        self.pix = QPixmap("./src/image/m7.png")
        self.account = account
        self.setWindow()
        self.iniTable()
        self.iniLineEdit()
        self.iniButton()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def iniTable(self):
        self.table = QTableWidget(self)
        self.table.setGeometry(20, 120, 820, 600)
        self.table.horizontalHeader().setDefaultSectionSize(400)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['房间号', '剩余床位'])

    def iniLineEdit(self):
        self.room = QLineEdit(self)
        self.room.setGeometry(270, 50, 200, 40)

    def iniButton(self):
        self.submit = QPushButton(self)
        self.submit.setGeometry(550, 50, 160, 40)
        self.submit.setText("搜索")
        self.setCursor(Qt.PointingHandCursor)


# 安排无床位学生的宿舍
class managereightWindow(QWidget):
    def __init__(self, account, parent=None):
        super(managereightWindow, self).__init__(parent)
        self.pix = QPixmap("./src/image/m8.png")
        self.account = account
        self.setWindow()
        self.iniButton()
        self.iniLineEdit()
        self.iniTable()
        self.iniSignalSlot()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def iniButton(self):
        self.submit = QPushButton(self)
        self.submit.setGeometry(620,100,100,30)
        self.submit.setText("添加")
        self.submit.setCursor(Qt.PointingHandCursor)

    def iniSignalSlot(self):
        pass

    def iniLineEdit(self):
        self.stuid = QLineEdit(self)
        self.room = QLineEdit(self)
        self.stuid.setGeometry(200,100,100,30)
        self.room.setGeometry(420,100,100,30)

    def iniTable(self):
        self.table=QTableWidget(self)
        self.table.setGeometry(20, 220, 815, 400)
        self.table.horizontalHeader().setDefaultSectionSize(90)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(['学号', '姓名', '性别', '学院', '房间号', '床号', '出生日期', '本人电话', '父母电话'])


# 删除离校中学生的宿舍信息
class managerninthWindow(QWidget):
    def __init__(self, account, parent=None):
        super(managerninthWindow, self).__init__(parent)
        self.pix = QPixmap('./src/image/m9.png')
        self.account = account
        self.setWindow()
        self.iniLineEdit()
        self.iniTable()
        self.iniButton()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def iniButton(self):
        self.delete = QPushButton(self)
        self.delete.setGeometry(400,105,100,30)
        self.delete.setText("删除")
        self.delete.setCursor(Qt.PointingHandCursor)

    def iniLineEdit(self):
        self.stuid = QLineEdit(self)
        self.stuid.setGeometry(200,105,100,30)

    def iniTable(self):
        self.table=QTableWidget(self)
        self.table.setGeometry(20, 220, 815, 400)
        self.table.horizontalHeader().setDefaultSectionSize(90)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(['学号', '姓名', '性别', '学院', '房间号', '床号', '出生日期', '本人电话', '父母电话'])


# 学生寝室调整
class managertenthWindow(QWidget):
    def __init__(self, account, parent=None):
        super(managertenthWindow, self).__init__(parent)
        self.account = account
        self.pix = QPixmap("./src/image/m10.png")
        self.setWindow()
        self.iniTable()
        self.iniLineEdit()
        self.iniButton()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def iniButton(self):
        self.submit = QPushButton(self)
        self.submit.setGeometry(600,105,100,30)
        self.submit.setText("调整")
        self.submit.setCursor(Qt.PointingHandCursor)


    def paintEvent(self, QPaintEvent):
        p=QPainter(self)
        p.drawPixmap(0,0,self.pix.width(),self.pix.height(),self.pix)


    def iniLineEdit(self):
        self.stuid = QLineEdit(self)
        self.room = QLineEdit(self)
        self.stuid.setGeometry(200,105,100,30)
        self.room.setGeometry(420,105,100,30)

    def iniTable(self):
        self.table=QTableWidget(self)
        self.table.setGeometry(20, 220, 815, 400)
        self.table.horizontalHeader().setDefaultSectionSize(90)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(['学号', '姓名', '性别', '学院', '房间号', '床号', '出生日期', '本人电话', '父母电话'])


# 个人资料
class managereleventhWindow(QWidget):
    def __init__(self, account, parent=None):
        super(managereleventhWindow, self).__init__(parent)
        self.account = account
        self.pix = QPixmap("./src/image/m11.png")
        self.setWindow()
        self.iniLinEdit()
        self.iniButton()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, QPaintEvent):
        p = QPainter(self)
        p.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def iniLinEdit(self):
        self.tea_id = QLineEdit(self)
        self.name = QLineEdit(self)
        self.building = QLineEdit(self)
        self.phone = QLineEdit(self)

        self.tea_id.setGeometry(120,160,400,50)
        self.name.setGeometry(120,220,400,50)
        self.building.setGeometry(120,290,400,50)
        self.phone.setGeometry(120,360,400,50)
        self.tea_id.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.name.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.building.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.phone.setStyleSheet("background:transparent;border-width:0;border-style:outset")


    def iniButton(self):
        self.submit = QPushButton(self)
        self.submit.setGeometry(370,480,100,50)
        self.submit.setCursor(Qt.PointingHandCursor)
        self.submit.setStyleSheet("background:transparent;")
