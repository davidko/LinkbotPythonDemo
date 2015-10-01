#!/usr/bin/env python3

import sys
import util
from PyQt4 import QtCore, QtGui

from led_dialog import Ui_Dialog

class LedDemo(QtGui.QDialog):
    demo_finished_signal = QtCore.pyqtSignal()
    def __init__(self, robot_id):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.robot_id = robot_id
        self.ui.lineEdit_serialId.setText(robot_id)

        # Connect signals
        self.ui.pushButton_run.clicked.connect(self.run)
        self.ui.pushButton_selectColor.clicked.connect(self.set_color)
        self.ui.lineEdit_serialId.textChanged.connect(self.update_code_box)
        self.demo_finished_signal.connect(self.run_finished)

        self.rgb = QtGui.QColor(255, 0, 255)
        self.update_code_box()
        
    def run(self):
        # Run button clicked
        # Disable Run and Close buttons
        self.ui.pushButton_run.setEnabled(False)
        self.ui.pushButton_close.setEnabled(False)
        util.run_string_async(self.ui.textEdit.toPlainText().encode(), self.run_finished_cb)

    def run_finished_cb(self):
        self.demo_finished_signal.emit()
        
    def run_finished(self):
        # Re-enable buttons
        self.ui.pushButton_run.setEnabled(True)
        self.ui.pushButton_close.setEnabled(True)

    def update_code_box(self):
        mapping = {'SERIAL_ID': self.ui.lineEdit_serialId.text(),
                   'R':self.rgb.red(),
                   'G':self.rgb.green(),
                   'B':self.rgb.blue(),
                   }
        code = util.translate_file('led_demo.template.py', mapping)
        self.ui.textEdit.setText(code)

    def set_color(self):
        self.rgb = QtGui.QColorDialog.getColor()
        self.update_code_box()
        self.ui.widget_color.setStyleSheet(
                'background-color:rgb({}, {}, {})'.format(
                    self.rgb.red(),
                    self.rgb.green(),
                    self.rgb.blue()
                    )
                )

def main():
    app = QtGui.QApplication(sys.argv)
    myapp = LedDemo('ABCD')
    myapp.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
