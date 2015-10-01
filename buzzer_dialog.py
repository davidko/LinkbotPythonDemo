# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buzzer_dialog.ui'
#
# Created: Thu Oct  1 16:17:45 2015
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
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_serialId = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_serialId.setObjectName(_fromUtf8("lineEdit_serialId"))
        self.gridLayout.addWidget(self.lineEdit_serialId, 0, 1, 1, 1)
        self.spinBox_frequency = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_frequency.setMinimum(20)
        self.spinBox_frequency.setMaximum(20000)
        self.spinBox_frequency.setProperty("value", 440)
        self.spinBox_frequency.setObjectName(_fromUtf8("spinBox_frequency"))
        self.gridLayout.addWidget(self.spinBox_frequency, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
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
        self.label_2.setText(_translate("Dialog", "Beep the Buzzer on a Linkbot!", None))
        self.groupBox.setTitle(_translate("Dialog", "Instructions", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>This small demo program allows you to control the buzzer on a Linkbot.</p><p>Sound waves are actually vibrations travelling through the air, very similar to waves travelling across the surface of water. The percieved pitch of a sound is determined by the &quot;frequency&quot; of the sound, or how close together the waves peaks are. The higher the frequency of sound, the higher the pitch.</p><p>Linkbots can create sound by vibrating a small device at precise frequencies. Try making the Linkbot play some different frequencies to see what they sound like! Most humans can hear frequencies from about 40 Hz to about 20000 Hz.</p></body></html>", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Settings", None))
        self.label.setText(_translate("Dialog", "Robot Serial ID:", None))
        self.label_4.setText(_translate("Dialog", "Frequency (Hz):", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Code:", None))
        self.pushButton_run.setText(_translate("Dialog", "Run", None))
        self.pushButton_close.setText(_translate("Dialog", "Close", None))

