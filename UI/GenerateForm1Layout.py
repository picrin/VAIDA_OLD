# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GenerateForm1Layout.ui'
#
# Created: Sun Oct 27 11:00:53 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_GenerateForm1Dialog(object):
    def setupUi(self, GenerateForm1Dialog):
        GenerateForm1Dialog.setObjectName(_fromUtf8("GenerateForm1Dialog"))
        GenerateForm1Dialog.resize(611, 401)
        font = QtGui.QFont()
        font.setPointSize(12)
        GenerateForm1Dialog.setFont(font)
        self.ExistingPGPLabel = QtGui.QLabel(GenerateForm1Dialog)
        self.ExistingPGPLabel.setGeometry(QtCore.QRect(0, 10, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ExistingPGPLabel.setFont(font)
        self.ExistingPGPLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ExistingPGPLabel.setObjectName(_fromUtf8("ExistingPGPLabel"))
        self.pushButton = QtGui.QPushButton(GenerateForm1Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 60, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.ExistingPGPLabel_2 = QtGui.QLabel(GenerateForm1Dialog)
        self.ExistingPGPLabel_2.setGeometry(QtCore.QRect(0, 100, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ExistingPGPLabel_2.setFont(font)
        self.ExistingPGPLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ExistingPGPLabel_2.setObjectName(_fromUtf8("ExistingPGPLabel_2"))
        self.label = QtGui.QLabel(GenerateForm1Dialog)
        self.label.setGeometry(QtCore.QRect(10, 160, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.plainTextEdit = QtGui.QPlainTextEdit(GenerateForm1Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 150, 401, 31))
        self.plainTextEdit.setTabChangesFocus(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label_2 = QtGui.QLabel(GenerateForm1Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(GenerateForm1Dialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(190, 180, 401, 31))
        self.plainTextEdit_2.setTabChangesFocus(True)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.label_4 = QtGui.QLabel(GenerateForm1Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 320, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.plainTextEdit_4 = QtGui.QPlainTextEdit(GenerateForm1Dialog)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(190, 310, 361, 31))
        self.plainTextEdit_4.setTabChangesFocus(True)
        self.plainTextEdit_4.setObjectName(_fromUtf8("plainTextEdit_4"))
        self.label_5 = QtGui.QLabel(GenerateForm1Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 561, 81))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_2 = QtGui.QPushButton(GenerateForm1Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 360, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(GenerateForm1Dialog)
        self.label_3.setGeometry(QtCore.QRect(560, 320, 51, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(GenerateForm1Dialog)
        QtCore.QMetaObject.connectSlotsByName(GenerateForm1Dialog)

    def retranslateUi(self, GenerateForm1Dialog):
        GenerateForm1Dialog.setWindowTitle(_translate("GenerateForm1Dialog", "VAIDA - Choose Key", None))
        self.ExistingPGPLabel.setText(_translate("GenerateForm1Dialog", "Already  have a PGP Key?", None))
        self.pushButton.setText(_translate("GenerateForm1Dialog", "Load Key", None))
        self.ExistingPGPLabel_2.setText(_translate("GenerateForm1Dialog", "Otherwise, generate a new key:", None))
        self.label.setText(_translate("GenerateForm1Dialog", "Your name:", None))
        self.label_2.setText(_translate("GenerateForm1Dialog", "Your email address:", None))
        self.label_4.setText(_translate("GenerateForm1Dialog", "Passphrase", None))
        self.label_5.setText(_translate("GenerateForm1Dialog", "Your passphrase should be at least 20 characters long and should be as difficult\n"
"to guess as possible.It should contain words not found in the dictionary.\n"
"\n"
"For example: \"Dirty loondry! Boundry. Stash/\"", None))
        self.pushButton_2.setText(_translate("GenerateForm1Dialog", "Generate Key", None))
        self.label_3.setText(_translate("GenerateForm1Dialog", "<n>", None))

