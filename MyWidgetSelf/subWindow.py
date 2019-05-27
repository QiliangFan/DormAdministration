from DDL.insert import *
from DDL.delete import *
from DDL.query import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


#学生端显示宿舍总体情况
class firstWindow(QWidget):
    def __init__(self,account,parent=None):
        super(firstWindow,self).__init__(parent)
        self.pix=QPixmap("./src/image/1.png")
        self.setWindow()
        self.account=account

        self.student_number=QLabel(self)
        self.teacher_number=QLabel(self)
        self.dorm_number=QLabel(self)
        self.room_number=QLabel(self)
        self.student_in=QLabel(self)
        self.student_canIn=QLabel(self)


    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, a0: QPaintEvent) -> None:
        self.iniLabel()
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),self.pix)
    def getAccount(self,account):
        self.account=account

    def iniLabel(self):
        self.student_number.setText(str(selectNumByType("student")))
        self.student_number.setGeometry(180,80,200,50)
        self.teacher_number.setText(str(selectNumByType("maanger")))
        self.teacher_number.setGeometry(680,80,200,50)
        data=selectRoomBuildingByAccount(self.account)
        if len(data)>0:
            self.dorm_number.setText(str(selectRoomBuildingByAccount(self.account)))
        else:
            self.dorm_number.setText("++")
        self.dorm_number.setGeometry(140,290,200,50)
        data=selectRoomByAccount(self.account)
        if len(data)>0:
            self.room_number.setText(str(selectRoomByAccount(self.account)))
        else:
            self.room_number.setText("++")
        self.room_number.setGeometry(420,290,200,50)
        self.student_in.setText(str(selectStudentNumberHasInByAccount(self.account)))
        self.student_in.setGeometry(690,290,200,50)


#学生端同宿舍人员查询
class secondWindow(QWidget):
    def __init__(self,account,parent=None):
        super(secondWindow,self).__init__(parent)
        self.accouont=account
        self.pix=QPixmap("./src/image/2.png")
        self.building=QLineEdit(self)
        self.room=QLineEdit(self)
        self.status=QLabel(self)
        self.submit=QPushButton(self)
        self.result=QTableWidget(self)
        self.setWindow()
        self.iniWidget()
        self.iniSignalSlot()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())


    def paintEvent(self, a0: QPaintEvent) -> None:
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),self.pix)

    def iniWidget(self):
        self.building.setGeometry(90,70,160,30)
        self.room.setGeometry(330,70,160,30)
        self.status.setGeometry(580,70,160,30)
        self.status.setText("状态良好")
        self.submit.setGeometry(680,70,160,30)
        self.submit.setText("查询")
        self.submit.setCursor(Qt.PointingHandCursor)
        self.result.setGeometry(20,120,815,600)
        self.result.horizontalHeader().setDefaultSectionSize(100)
        self.result.verticalHeader().setDefaultSectionSize(30)
        self.result.setColumnCount(8)
        # self.result.setRowCount(20)
        list=[u'学号',u'姓名',u'学院',u'年级',u'出生日期',u'个人电话',u'父母电话',u'床号']
        self.result.setHorizontalHeaderLabels(list)

    def iniSignalSlot(self):
        building=self.building.text()
        room=self.room.text()



#学生端查询本楼成员
class thirdWindow(QWidget):
    def __init__(self,account,parent=None):
        super(thirdWindow,self).__init__(parent)
        self.account=account
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
        list = [u'学号', u'姓名', u'学院', u'年级',u'房间号']
        self.result.setHorizontalHeaderLabels(list)

    def iniSignalSlot(self):
        building = self.building.text()
        name = self.name.text()

#学生端个人资料面板
class forthWindow(QWidget):
    def __init__(self,account,parent=None):
        super(forthWindow,self).__init__(parent)
        self.account=account
        self.pix=QPixmap("./src/image/4.png")
        self.setWindow()
        self.iniLineEdit()


    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),self.pix)

    def iniLineEdit(self):
        self.id=QLineEdit(self)
        self.name = QLineEdit(self)
        self.department_name = QLineEdit(self)
        self.grade = QLineEdit(self)
        self.phoneparent = QLineEdit(self)
        self.phoneself = QLineEdit(self)
        self.gender = QLineEdit(self)
        self.bed_id = QLineEdit(self)
        self.admition_date = QLineEdit(self)
        self.birthday = QLineEdit(self)
        self.id.setGeometry(190,153,360,30)
        self.name.setGeometry(190,203,360,30)
        self.department_name.setGeometry(190,253,360,30)
        self.grade.setGeometry(190,303,360,30)
        self.phoneparent.setGeometry(190,350,360,30)
        self.phoneself.setGeometry(190,393,360,30)
        self.gender.setGeometry(190,435,360,30)
        self.bed_id.setGeometry(190,490,360,30)
        self.admition_date.setGeometry(190,540,360,30)
        self.birthday.setGeometry(190,600,360,30)
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



