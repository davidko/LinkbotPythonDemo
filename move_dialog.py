# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'move_dialog.ui'
#
# Created: Thu Oct  1 16:39:06 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(627, 652)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.groupBox = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.doubleSpinBox_distance = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_distance.setMaximum(20.0)
        self.doubleSpinBox_distance.setSingleStep(0.1)
        self.doubleSpinBox_distance.setProperty("value", 6.0)
        self.doubleSpinBox_distance.setObjectName(_fromUtf8("doubleSpinBox_distance"))
        self.gridLayout.addWidget(self.doubleSpinBox_distance, 2, 2, 1, 1)
        self.doubleSpinBox_radius = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_radius.setDecimals(1)
        self.doubleSpinBox_radius.setMaximum(5.0)
        self.doubleSpinBox_radius.setSingleStep(0.1)
        self.doubleSpinBox_radius.setProperty("value", 3.5)
        self.doubleSpinBox_radius.setObjectName(_fromUtf8("doubleSpinBox_radius"))
        self.gridLayout.addWidget(self.doubleSpinBox_radius, 1, 2, 1, 1)
        self.lineEdit_serialId = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_serialId.setObjectName(_fromUtf8("lineEdit_serialId"))
        self.gridLayout.addWidget(self.lineEdit_serialId, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.doubleSpinBox_speed = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_speed.setMinimum(0.5)
        self.doubleSpinBox_speed.setMaximum(5.0)
        self.doubleSpinBox_speed.setSingleStep(0.1)
        self.doubleSpinBox_speed.setProperty("value", 2.0)
        self.doubleSpinBox_speed.setObjectName(_fromUtf8("doubleSpinBox_speed"))
        self.gridLayout.addWidget(self.doubleSpinBox_speed, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.textEdit = QtGui.QTextEdit(self.groupBox_3)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_3.addWidget(self.textEdit)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_run = QtGui.QPushButton(Dialog)
        self.pushButton_run.setObjectName(_fromUtf8("pushButton_run"))
        self.horizontalLayout.addWidget(self.pushButton_run)
        self.pushButton_close = QtGui.QPushButton(Dialog)
        self.pushButton_close.setObjectName(_fromUtf8("pushButton_close"))
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "Move a 2-wheeled Linkbot a precise distance!", None))
        self.groupBox.setTitle(_translate("Dialog", "Instructions", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>This small demo program moves the motors on a Linkbot.</p><p>The Linkbot\'s motors are very precise. They can rotate to within 0.3 degrees of a desired angle at a constant velocity from 0 to 200 degrees per second. This means that you can make Linkbots move and turn very precise distances at precise speeds.</p><p>For this demo program, make sure the Linkbot has two wheels attached. Type in the distance you want the Linkbot to go, the radius of the wheels, and the speed you want the Linkbot to travel at and the Python script will calculate the necessary rotational speed and angle to turn the motors to achieve the desired result.</p></body></html>", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Settings", None))
        self.label_5.setText(_translate("Dialog", "Distance (inches)", None))
        self.label.setText(_translate("Dialog", "Robot Serial ID:", None))
        self.label_4.setText(_translate("Dialog", "Wheel Radius (inches)", None))
        self.label_6.setText(_translate("Dialog", "Speed (inches/second)", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Code:", None))
        self.pushButton_run.setText(_translate("Dialog", "Run", None))
        self.pushButton_close.setText(_translate("Dialog", "Close", None))

