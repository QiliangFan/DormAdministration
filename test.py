import sys

from PyQt5.QtWidgets import *
from MyWidgetSelf.Window import *
import MyWidgetSelf.Window

app=QApplication(sys.argv)
w=logupWindowStu()
w.show()
app.exec_()
