from DDL.insert import *
from DDL.delete import *
from DDL.Stu_query2 import *
from DDL.Stu_query3 import *
from DDL.Stu_query4 import *
from DDL.Stu_query5 import *
from DDL.query import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from DDL.Tea_query2 import *
from DDL.Tea_query3 import *
from DDL.Tea_query4 import *
from DDL.Tea_query5 import *
from DDL.Tea_query6 import *
from DDL.Tea_query7 import *
from DDL.Tea_query8 import *
from DDL.Tea_query11 import *
from DDL.Tea_query10 import *
from DDL.Tea_query9 import *
from DDL.Stuu_query6 import *
from DDL.Tea_query12 import *
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
        self.iniLabel()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def getAccount(self, account):
        self.account = account

    def iniLabel(self):
        self.student_number.setText(str(selectNumByType("student")))
        self.student_number.setGeometry(180, 80, 200, 50)
        self.teacher_number.setText(str(selectNumByType("manager")))
        self.teacher_number.setGeometry(680, 80, 200, 50)
        data = selectRoomBuilding()
        if len(data) > 0:
            self.dorm_number.setText(selectRoomBuilding() + '栋')
        else:
            self.dorm_number.setText("未知")
        self.dorm_number.setGeometry(140, 290, 200, 50)
        data = selectRoom()
        if len(data) > 0:
            self.room_number.setText(selectRoom() + '间')
        else:
            self.room_number.setText("未知")
        self.room_number.setGeometry(420, 290, 200, 50)
        self.student_in.setText(str(selectStudentNumberHasIn()))
        self.student_in.setGeometry(690, 290, 200, 50)
        self.student_canIn.setText(countMaxStudentCanIn())
        self.student_canIn.setGeometry(420, 460, 200, 50)


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
        self.result.setGeometry(20, 120, 830, 600)
        self.result.horizontalHeader().setDefaultSectionSize(100)
        self.result.verticalHeader().setDefaultSectionSize(30)

        self.result.setColumnCount(8)
        self.result.setColumnWidth(6, 130)
        self.result.setColumnWidth(7,70)
        # self.result.setRowCount(20)
        list = [u'学号', u'姓名', u'学院', u'年级', u'出生日期', u'个人电话', u'父母电话', u'床号']
        self.result.setHorizontalHeaderLabels(list)

    def iniSignalSlot(self):
        self.submit.clicked.connect(self.query)

    def query(self):
        if self.building.text()=="":
            building=" "
        else:
            building = self.building.text()
        if self.room.text()=="":
            room=" "
        else:
            room = self.room.text()


        print(room)
        print(building)
        data = getStuInfro(building, room)
        length = len(data)
        self.result.setRowCount(length)

        for i in range(0, length):
            for j in range(0, 8):
                if data[i][j] is None:
                    self.result.setItem(i, j, QTableWidgetItem(str("")))
                else:
                    self.result.setItem(i, j, QTableWidgetItem(str(data[i][j])))


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
        self.result.setGeometry(20, 120, 830, 600)
        self.result.horizontalHeader().setDefaultSectionSize(160)
        self.result.verticalHeader().setDefaultSectionSize(30)
        self.result.setColumnCount(5)
        # self.result.setRowCount(20)
        list = [u'学号', u'姓名', u'学院', u'年级', u'房间号']
        self.result.setHorizontalHeaderLabels(list)

    def iniSignalSlot(self):
        self.submit.clicked.connect(self.query)

    def query(self):
        building = self.building.text()
        name = self.name.text()
        data = getStuByBuildAndName(building, name)
        length = len(data)
        self.result.setRowCount(length)

        print(data)
        print(data[0][1])
        for i in range(0, length):
            for j in range(0, 5):
                print(j)
                if data[i][j] is None:
                    print(data[i][j])
                    self.result.setItem(i, j, QTableWidgetItem(str("")))
                    print("?????")
                else:
                    print(data[i][j])
                    self.result.setItem(i, j, QTableWidgetItem(str(data[i][j])))
                    print("+++++")


# 学生端个人资料面板
class forthWindow(QWidget):
    def __init__(self, account, parent=None):
        super(forthWindow, self).__init__(parent)
        self.account = account
        self.pix = QPixmap("./src/image/4.png")
        self.submit = QPushButton(self)
        self.setWindow()
        self.iniLineEdit()
        self.iniSignalSlot()
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

        data=getinfo(self.account)
        if len(data)>0:
            self.id.setText(str(data[0][0]))
            self.name.setText(str(data[0][1]))
            self.department_name.setText(str(data[0][2]))
            self.grade.setText(str(data[0][3]))
            self.phoneparent.setText(str(data[0][4]))
            self.phoneself.setText(str(data[0][5]))
            self.gender.setText(str(data[0][6]))
            self.bed_id.setText(str(data[0][7]))
            self.admition_date.setText(str(data[0][8]))
            self.birthday.setText(str(data[0][9]))

    def iniButton(self):
        self.submit.setGeometry(370, 630, 80, 50)
        self.submit.setCursor(Qt.PointingHandCursor)
        self.submit.setStyleSheet("background:transparent;")

    def iniSignalSlot(self):
        self.submit.clicked.connect(self.query)
        self.submit.clicked.connect(self.showMessageBox)

    def query(self):
        stu_id = self.id.text()
        name = self.name.text()
        dept_name = self.department_name.text()
        grade = self.grade.text()
        phoneParent = self.phoneparent.text()
        phoneOwn = self.phoneself.text()
        gender = self.gender.text()
        bed_id = self.bed_id.text()
        admisstion_date = self.admition_date.text()
        birthday = self.birthday.text()
        modify(self.account, stu_id, name, dept_name, grade, phoneParent,
               phoneOwn, gender, bed_id, admisstion_date, birthday)

    def showMessageBox(self):
        self.m = QMessageBox()
        self.m.setWindowTitle("注意")
        self.m.setText("修改成功")
        self.m.show()

#申请提交
class fifthWindow(QWidget):
    def __init__(self,account,parent=None):
        super(fifthWindow, self).__init__(parent)
        self.account = account
        self.pix = QPixmap("./src/image/5.png")
        self.submit = QPushButton(self)
        self.setWindow()
        self.iniLineEdit()
        self.iniSignalSlot()
        self.iniButton()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.mask())

    def iniLineEdit(self):
        self.stuid=QLineEdit(self)
        self.name=QLineEdit(self)
        self.build=QLineEdit(self)
        self.room=QLineEdit(self)
        self.toRoom=QLineEdit(self)
        self.stuid.setGeometry(180,140,450,30)
        self.name.setGeometry(180,190,450,30)
        self.build.setGeometry(180,240,450,30)
        self.room.setGeometry(180,300,450,30)
        self.toRoom.setGeometry(180,355,450,30)
        self.stuid.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.name.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.build.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.room.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.toRoom.setStyleSheet("background:transparent;border-width:0;border-style:outset")


    def iniSignalSlot(self):
        self.submit.clicked.connect(self.query)

    def iniButton(self):
        self.submit.setGeometry(370,460,80,50)
        self.submit.setCursor(Qt.PointingHandCursor)
        self.submit.setStyleSheet("background:transparent;")

    def query(self):
        if self.stuid.text()=="" or self.name.text()=="" or self.build.text()=="" or self.room.text()=="" or self.toRoom.text()=="":
            self.m=QMessageBox()
            self.m.setWindowTitle("注意")
            self.m.setText("请输入完整信息！")
            self.m.show()
        else:
            data=apply(self.account,self.stuid.text(),self.name.text(),self.build.text(),self.room.text(),self.toRoom.text())
            if data==0:
                self.mm=QMessageBox()
                self.mm.setWindowTitle("注意")
                self.mm.setText("提交成功！")
                self.mm.show()

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),self.pix)

class historyWindow(QWidget):
    def __init__(self,account,parent=None):
        super(historyWindow,self).__init__(parent)
        self.account=account
        self.pix=QPixmap("./src/image/history.png")

        self.setWindow()
        self.iniTable()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),self.pix)

    def iniTable(self):
        self.table=QTableWidget(self)
        self.table.setGeometry(10,10,850,600)
        self.table.setColumnCount(6)
        self.table.horizontalHeader().setDefaultSectionSize(140)
        self.table.setHorizontalHeaderLabels(['申请人学号','申请人姓名','所属楼','原房间号','申请房间号','申请时间'])
        self.showTable()

    def showTable(self):
        data=showAllStu(self.account)
        print(data)
        print(len(data))
        if len(data)>0:
            self.table.setRowCount(len(data))
            for i in range(0,len(data)):
                for j in range(0,6):
                    
                    self.table.setItem(i,j,QTableWidgetItem(str(data[i][j])))




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
        self.iniLabel()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def getAccount(self, account):
        self.account = account

    def iniLabel(self):
        self.student_number.setText(str(selectNumByType("student")))
        self.student_number.setGeometry(180, 80, 200, 50)
        self.teacher_number.setText(str(selectNumByType("manager")))
        self.teacher_number.setGeometry(680, 80, 200, 50)
        data = selectRoomBuilding()
        self.dorm_number.setText(str(selectRoomBuilding()) + "栋")
        self.dorm_number.setGeometry(140, 290, 200, 50)
        data = selectRoom()
        self.room_number.setText(str(selectRoom()) + "间")
        self.room_number.setGeometry(420, 290, 200, 50)
        self.student_in.setText(str(selectStudentNumberHasIn()))
        self.student_in.setGeometry(690, 290, 200, 50)
        self.student_canIn.setText(str(countMaxStudentCanIn()))
        self.student_canIn.setGeometry(420, 460, 200, 50)


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
        data = GetManagerInfoSameBuilding(self.account)
        length = len(data)
        self.table.setRowCount(length)

        for i in range(0, length):
            for j in range(0, 5):
                if data[i][j] is None:
                    self.table.setItem(i, j, QTableWidgetItem(str("")))
                else:
                    self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))


# 同楼全部学生信息
class managerthirdWindow(QWidget):
    def __init__(self, account, parent=None):
        super(managerthirdWindow, self).__init__(parent)
        self.account = account
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
        data = getStuInfoSameBuilding(self.account)
        length = len(data)

        self.table.setRowCount(length)
        for i in range(0, length):
            for j in range(0, 9):
                if data[i][j] is None:
                    self.table.setItem(i, j, QTableWidgetItem(str("")))
                else:
                    self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))


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
        self.submit.setCursor(Qt.PointingHandCursor)
        self.submit.clicked.connect(self.query)

    def query(self):
        room = self.room.text()
        data = getStuInfo(room, self.account)
        length = len(data)
        self.table.setRowCount(length)
        for i in range(0, length):
            for j in range(0, 9):
                if data[i][j] is None:
                    self.table.setItem(i, j, QTableWidgetItem(str("")))
                else:
                    self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))


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
        self.stuid = QLineEdit(self)
        self.stuid.setGeometry(270, 50, 200, 40)

    def iniButton(self):
        self.submit = QPushButton(self)
        self.submit.setGeometry(550, 50, 160, 40)
        self.submit.setText("搜索")
        self.submit.setCursor(Qt.PointingHandCursor)
        self.submit.clicked.connect(self.query)

    def query(self):
        stuid = self.stuid.text()
        data = getStuInfoById(stuid, self.account)
        length = len(data)
        self.table.setRowCount(length)
        for i in range(0, length):
            for j in range(0, 9):
                if data[i][j] is None:
                    self.table.setItem(i, j, QTableWidgetItem(str("")))
                else:
                    self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))


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
        self.table.setGeometry(20, 120, 825, 600)
        self.table.horizontalHeader().setDefaultSectionSize(400)
        self.table.setColumnCount(2)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setHorizontalHeaderLabels(['未满房间号', '剩余床位'])


        data=getRoomAvaliable(self.account)
        length=len(data)

        self.table.setRowCount(length)

        for i in range(0,length):
            for j in range(0,2):
                if data[i][j] is None:
                    self.table.setItem(i, j, QTableWidgetItem(str("")))
                else:
                    self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))

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
        self.table.setGeometry(20, 120, 830, 600)
        self.table.horizontalHeader().setDefaultSectionSize(400)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['房间号', '剩余床位'])
        self.table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        ##不可修改


    def iniLineEdit(self):
        self.room = QLineEdit(self)
        self.room.setGeometry(270, 50, 200, 40)

    def iniButton(self):
        self.submit = QPushButton(self)
        self.submit.setGeometry(550, 50, 160, 40)
        self.submit.setText("搜索")
        self.submit.setCursor(Qt.PointingHandCursor)
        self.submit.clicked.connect(self.query)

    def query(self):
        room=self.room.text()
        data=getNumOfBed(room,self.account)
        print(data)
        length=len(data)
        self.table.setRowCount(length)
        for i in range(0,length):
            for j in range(0,2):
                if data[i][j] is None:
                    self.table.setItem(i, j, QTableWidgetItem(str("")))
                else:
                    self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))

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
        self.submit.setGeometry(620, 100, 100, 30)
        self.submit.setText("添加")
        self.submit.setCursor(Qt.PointingHandCursor)

    def iniSignalSlot(self):
        self.submit.clicked.connect(self.query)

    def iniLineEdit(self):
        self.stuid = QLineEdit(self)
        self.room = QLineEdit(self)
        self.stuid.setGeometry(200, 100, 100, 30)
        self.room.setGeometry(420, 100, 100, 30)

    def iniTable(self):
        self.table = QTableWidget(self)
        self.table.setGeometry(20, 220, 845, 400)
        self.table.horizontalHeader().setDefaultSectionSize(90)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setColumnCount(9)
        self.table.setColumnWidth(4,50)
        self.table.setColumnWidth(5,50)
        self.table.setColumnWidth(7,125)
        self.table.setColumnWidth(8,125)
        self.table.setColumnWidth(2,50)
        self.table.setHorizontalHeaderLabels(['学号', '姓名', '性别', '学院', '房间号', '床号', '出生日期', '本人电话', '父母电话'])

    def query(self):
        stuid=self.stuid.text()
        room=self.room.text()
        data=arrangeStuWithoutBed(stuid,room,self.account)
        if data==-1:
            self.m=QMessageBox()
            self.m.setWindowTitle("注意")
            self.m.setText("此学生已有床位或目标宿舍房间已满！")
            self.m.show()
        else:
            length=len(data)
            self.table.setRowCount(length)
            for i in range(0,length):
                for j in range(0,9):
                    if data[i][j] is None:
                        self.table.setItem(i, j, QTableWidgetItem(str("")))
                    else:
                        self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))

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
        self.delete.setGeometry(400, 105, 100, 30)
        self.delete.setText("删除")
        self.delete.setCursor(Qt.PointingHandCursor)
        self.delete.clicked.connect(self.query)

    def iniLineEdit(self):
        self.stuid = QLineEdit(self)
        self.stuid.setGeometry(200, 105, 100, 30)

    def iniTable(self):
        self.table = QTableWidget(self)
        self.table.setGeometry(20, 220, 815, 400)
        self.table.horizontalHeader().setDefaultSectionSize(90)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setColumnCount(9)
        self.table.setColumnWidth(2, 50)
        self.table.setColumnWidth(4, 60)
        self.table.setColumnWidth(5, 45)
        self.table.setColumnWidth(6, 100)
        self.table.setColumnWidth(7, 120)
        self.table.setColumnWidth(8, 120)
        self.table.setHorizontalHeaderLabels(['学号', '姓名', '性别', '学院', '房间号', '床号', '出生日期', '本人电话', '父母电话'])

    def query(self):
        data=delete(self.account,self.stuid.text())
        if data==-1:
            self.em=QMessageBox()
            self.em.setWindowTitle("注意")
            self.em.setText("该学生没有住宿信息！")
        else:
            
            length = len(data)
            self.table.setRowCount(length)
            for i in range(0, length):
                for j in range(0, 9):
                    if data[i][j] is None:
                        self.table.setItem(i, j, QTableWidgetItem(str("")))
                    else:
                        self.table.setItem(i,j,QTableWidgetItem(str(data[i][j])))
            self.suc = QMessageBox()
            self.suc.setWindowTitle("注意")
            self.suc.setText("修改成功")
            self.suc.show()


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
        self.submit.setGeometry(600, 105, 100, 30)
        self.submit.setText("调整")
        self.submit.setCursor(Qt.PointingHandCursor)
        self.submit.clicked.connect(self.query)

    def paintEvent(self, QPaintEvent):
        p = QPainter(self)
        p.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def iniLineEdit(self):
        self.stuid = QLineEdit(self)
        self.room = QLineEdit(self)
        self.stuid.setGeometry(200, 105, 100, 30)
        self.room.setGeometry(420, 105, 100, 30)

    def iniTable(self):
        self.table = QTableWidget(self)
        self.table.setGeometry(20, 220, 815, 400)
        self.table.horizontalHeader().setDefaultSectionSize(90)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.setColumnCount(9)
        self.table.setColumnWidth(2,50)
        self.table.setColumnWidth(4,60)
        self.table.setColumnWidth(5,45)
        self.table.setColumnWidth(6,100)
        self.table.setColumnWidth(7,120)
        self.table.setColumnWidth(8,120)
        self.table.setHorizontalHeaderLabels(['学号', '姓名', '性别', '学院', '房间号', '床号', '出生日期', '本人电话', '父母电话'])

    def query(self):
        if self.stuid.text() =="" or self.room.text()=="":
            self.q=QMessageBox()
            self.q.setWindowTitle("注意")
            self.q.setText("请输入有效信息！")
        else:
            data=adjust(self.stuid.text(),self.room.text(),self.account)
            if data==-1:
                self.mm=QMessageBox()
                self.mm.setWindowTitle("注意")
                self.mm.setText("目标宿舍已经满人！")
                self.mm.show()
            else:
                length=len(data)
                self.table.setRowCount(length)
                for i in range(0,length):
                    for j in range(0,9):
                        if data[i][j] is None:
                            self.table.setItem(i, j, QTableWidgetItem(str("")))
                        else:
                            self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))
                self.suc=QMessageBox()
                self.suc.setWindowTitle("注意")
                self.suc.setText("修改成功")
                self.suc.show()

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
        self.gender=QLineEdit(self)
        self.birthday=QLineEdit(self)



        self.tea_id.setGeometry(155, 165, 400, 50)
        self.name.setGeometry(155, 220, 400, 50)
        self.gender.setGeometry(155,270,400,50)
        self.building.setGeometry(155,315,400,50)
        self.phone.setGeometry(155,360,400,50)
        self.birthday.setGeometry(155,415,400,50)


        self.tea_id.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.name.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.building.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.phone.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.gender.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.birthday.setStyleSheet("background:transparent;border-width:0;border-style:outset")

        data=getTeaInfo(self.account)
        if len(data)>0:
            self.tea_id.setText(str(data[0][0]))
            self.name.setText(str(data[0][1]))
            self.building.setText(str(data[0][2]))
            self.phone.setText(str(data[0][3]))
            self.gender.setText(str(data[0][4]))
            self.birthday.setText(str(data[0][5]))

    def iniButton(self):
        self.submit = QPushButton(self)
        self.submit.setGeometry(360, 470, 100, 50)
        self.submit.setCursor(Qt.PointingHandCursor)
        self.submit.setStyleSheet("background:transparent;")
        self.submit.clicked.connect(self.query)

    def query(self):
        if self.building.text()=="":
            self.m1=QMessageBox()
            self.m1.setWindowTitle("注意")
            self.m1.setText("宿舍楼不能为空")
            self.m1.show()
        elif self.tea_id.text()=="":
            self.m2=QMessageBox()
            self.m2.setWindowTitle("注意")
            self.m2.setText("工号不能为空")
            self.m2.show()
        else:
            a=Teamodify(self.account,self.tea_id.text(),self.name.text(),self.gender.text(),self.building.text(),self.phone.text(),self.birthday.text())
            if a==-1:
                self.m3=QMessageBox()
                self.m3.setWindowTitle("注意")
                self.m3.setText("楼号不存在！")
                self.m3.show()
            else:
                self.m = QMessageBox()
                self.m.setWindowTitle("注意")
                self.m.setText("修改成功！")
                self.m.show()


class managertwelevthWindow(QWidget):
    def __init__(self,account,parent=None):
        super(managertwelevthWindow,self).__init__(parent)
        self.account=account
        self.pix=QPixmap("./src/image/m12.png")

        self.setWindow()
        self.iniTable()
        self.iniButton()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),self.pix)

    def iniTable(self):
        self.table=QTableWidget(self)
        self.table.setGeometry(10,10,850,600)
        self.table.setColumnCount(6)
        self.table.horizontalHeader().setDefaultSectionSize(140)
        self.table.setHorizontalHeaderLabels(['申请人学号','申请人姓名','所属楼','原房间号','申请房间号','申请时间'])
        self.showTable()
    def iniButton(self):
        self.submit=QPushButton(self)
        self.submit.setCursor(Qt.PointingHandCursor)
        self.submit.setGeometry(360,660,180,40)
        self.submit.setStyleSheet("background:transparent;")
        self.submit.clicked.connect(self.deleteAll)

    def showTable(self):
        data=teaShowAll(self.account)
        if len(data)>0:
            self.table.setRowCount(len(data))
            for i in range(0,len(data)):
                for j in range(0,6):
                    self.table.setItem(i,j,QTableWidgetItem(str(data[i][j])))


    def deleteAll(self):
        teaDelete(self.account)
        self.showTable()
