# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PrivateKeySelectorDialog.ui'
#
# Created: Sun Oct 27 14:36:15 2013
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

class Ui_PrivateKeySelectorDialog(object):
    def setupUi(self, PrivateKeySelectorDialog):
        PrivateKeySelectorDialog.setObjectName(_fromUtf8("PrivateKeySelectorDialog"))
        PrivateKeySelectorDialog.resize(400, 321)
        self.keyListWidget = QtGui.QListWidget(PrivateKeySelectorDialog)
        self.keyListWidget.setGeometry(QtCore.QRect(10, 10, 381, 221))
        self.keyListWidget.setObjectName(_fromUtf8("keyListWidget"))
        self.passphraseLabel = QtGui.QLabel(PrivateKeySelectorDialog)
        self.passphraseLabel.setGeometry(QtCore.QRect(20, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passphraseLabel.setFont(font)
        self.passphraseLabel.setObjectName(_fromUtf8("passphraseLabel"))
        self.selectKeyButton = QtGui.QPushButton(PrivateKeySelectorDialog)
        self.selectKeyButton.setGeometry(QtCore.QRect(120, 280, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.selectKeyButton.setFont(font)
        self.selectKeyButton.setObjectName(_fromUtf8("selectKeyButton"))
        self.lineEdit = QtGui.QLineEdit(PrivateKeySelectorDialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 239, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(PrivateKeySelectorDialog)
        QtCore.QMetaObject.connectSlotsByName(PrivateKeySelectorDialog)

    def retranslateUi(self, PrivateKeySelectorDialog):
        PrivateKeySelectorDialog.setWindowTitle(_translate("PrivateKeySelectorDialog", "Choose an Existing Private Key", None))
        self.passphraseLabel.setText(_translate("PrivateKeySelectorDialog", "Passphrase:", None))
        self.selectKeyButton.setText(_translate("PrivateKeySelectorDialog", "Select Key", None))

