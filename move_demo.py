#!/usr/bin/env python3

import sys
import util
from PyQt4 import QtCore, QtGui

from move_dialog import Ui_Dialog

class MoveDemo(QtGui.QDialog):
    demo_finished_signal = QtCore.pyqtSignal()
    def __init__(self, robot_id):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.robot_id = robot_id
        self.ui.lineEdit_serialId.setText(robot_id)

        # Connect signals
        self.ui.pushButton_run.clicked.connect(self.run)
        self.ui.pushButton_close.clicked.connect(self.done)
        self.ui.lineEdit_serialId.textChanged.connect(self.update_code_box)
        self.ui.doubleSpinBox_radius.valueChanged.connect(self.update_code_box)
        self.ui.doubleSpinBox_distance.valueChanged.connect(self.update_code_box)
        self.ui.doubleSpinBox_speed.valueChanged.connect(self.update_code_box)
        self.demo_finished_signal.connect(self.run_finished)

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

    def update_code_box(self, *args, **kwargs):
        mapping = {'SERIAL_ID': self.ui.lineEdit_serialId.text(),
                   'distance':self.ui.doubleSpinBox_distance.value(),
                   'diameter':self.ui.doubleSpinBox_radius.value(),
                   'speed':self.ui.doubleSpinBox_speed.value(),
                   }
        code = util.translate_file('move_demo.template.py', mapping)
        self.ui.textEdit.setText(code)

def main():
    app = QtGui.QApplication(sys.argv)
    myapp = MoveDemo('ABCD')
    myapp.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
