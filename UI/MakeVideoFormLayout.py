# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MakeVideoFormLayout.ui'
#
# Created: Sun Oct 27 16:06:57 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_MakeVideoForm(object):
    def setupUi(self, MakeVideoForm):
        MakeVideoForm.setObjectName(_fromUtf8("MakeVideoForm"))
        MakeVideoForm.resize(547, 432)
        self.keyIsLabel = QtGui.QLabel(MakeVideoForm)
        self.keyIsLabel.setGeometry(QtCore.QRect(20, 30, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.keyIsLabel.setFont(font)
        self.keyIsLabel.setObjectName(_fromUtf8("keyIsLabel"))
        self.keyLabel = QtGui.QLabel(MakeVideoForm)
        self.keyLabel.setGeometry(QtCore.QRect(20, 60, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyLabel.setFont(font)
        self.keyLabel.setObjectName(_fromUtf8("keyLabel"))
        self.instructionsLabel = QtGui.QLabel(MakeVideoForm)
        self.instructionsLabel.setGeometry(QtCore.QRect(20, 270, 491, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.instructionsLabel.setFont(font)
        self.instructionsLabel.setObjectName(_fromUtf8("instructionsLabel"))
        self.importVideoButton = QtGui.QPushButton(MakeVideoForm)
        self.importVideoButton.setGeometry(QtCore.QRect(150, 380, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.importVideoButton.setFont(font)
        self.importVideoButton.setObjectName(_fromUtf8("importVideoButton"))
        self.widget = QtGui.QWidget(MakeVideoForm)
        self.widget.setGeometry(QtCore.QRect(20, 110, 491, 151))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.nameLabel = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.verticalLayout.addWidget(self.nameLabel)
        self.emailLabel = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.verticalLayout.addWidget(self.emailLabel)
        self.expiresLabel = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.expiresLabel.setFont(font)
        self.expiresLabel.setObjectName(_fromUtf8("expiresLabel"))
        self.verticalLayout.addWidget(self.expiresLabel)
        self.dateLabel = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName(_fromUtf8("dateLabel"))
        self.verticalLayout.addWidget(self.dateLabel)

        self.retranslateUi(MakeVideoForm)
        QtCore.QMetaObject.connectSlotsByName(MakeVideoForm)

    def retranslateUi(self, MakeVideoForm):
        MakeVideoForm.setWindowTitle(_translate("MakeVideoForm", "VAIDA - Your Video", None))
        self.keyIsLabel.setText(_translate("MakeVideoForm", "Your key fingerprint is:", None))
        self.keyLabel.setText(_translate("MakeVideoForm", "0a.1b.2c:3d", None))
        self.instructionsLabel.setText(_translate("MakeVideoForm", "Instructions + link", None))
        self.importVideoButton.setText(_translate("MakeVideoForm", "Import Video", None))
        self.nameLabel.setText(_translate("MakeVideoForm", "Name: Hugh McGrade", None))
        self.emailLabel.setText(_translate("MakeVideoForm", "Email Address: hugh_mcgrade@hotmail.co.uk", None))
        self.expiresLabel.setText(_translate("MakeVideoForm", "Expires: 1 October 2015", None))
        self.dateLabel.setText(_translate("MakeVideoForm", "Date: 27 October 2013", None))

