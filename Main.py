from PyQt5.QtWidgets import *
import MainWindow
import sys
from DDL.account import *

def main():
    app = QApplication(sys.argv)
    win=MainWindow.chooseWindow()
    win.show()
    return app.exec_()


if __name__ == '__main__':
    main()
    db.close()
