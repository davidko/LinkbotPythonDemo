#!/usr/bin/env python3

import sys
import util
from PyQt4 import QtCore, QtGui

from mainwindow import Ui_MainWindow
import led_demo
import buzzer_demo
import move_demo

class MyMainWindow(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_led.clicked.connect(self.run_led_demo)
        self.ui.pushButton_buzzer.clicked.connect(self.run_buzzer_demo)
        self.ui.pushButton_move.clicked.connect(self.run_move_demo)

    def run_led_demo(self):
        dialog = led_demo.LedDemo(self.ui.lineEdit_serialId.text())
        dialog.exec()

    def run_buzzer_demo(self):
        dialog = buzzer_demo.BuzzerDemo(self.ui.lineEdit_serialId.text())
        dialog.exec()

    def run_move_demo(self):
        dialog = move_demo.MoveDemo(self.ui.lineEdit_serialId.text())
        dialog.exec()


def main():
    app = QtGui.QApplication(sys.argv)
    myapp = MyMainWindow()
    myapp.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
