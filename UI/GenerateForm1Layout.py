# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GenerateForm1Layout.ui'
#
# Created: Sun Oct 27 12:37:32 2013
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
        self.existingPGPLabel = QtGui.QLabel(GenerateForm1Dialog)
        self.existingPGPLabel.setGeometry(QtCore.QRect(0, 10, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.existingPGPLabel.setFont(font)
        self.existingPGPLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.existingPGPLabel.setObjectName(_fromUtf8("existingPGPLabel"))
        self.loadKeyButton = QtGui.QPushButton(GenerateForm1Dialog)
        self.loadKeyButton.setGeometry(QtCore.QRect(180, 60, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loadKeyButton.setFont(font)
        self.loadKeyButton.setObjectName(_fromUtf8("loadKeyButton"))
        self.newPGPLabel = QtGui.QLabel(GenerateForm1Dialog)
        self.newPGPLabel.setGeometry(QtCore.QRect(0, 100, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.newPGPLabel.setFont(font)
        self.newPGPLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newPGPLabel.setObjectName(_fromUtf8("newPGPLabel"))
        self.nameLabel = QtGui.QLabel(GenerateForm1Dialog)
        self.nameLabel.setGeometry(QtCore.QRect(10, 160, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.nameTextEdit = QtGui.QPlainTextEdit(GenerateForm1Dialog)
        self.nameTextEdit.setGeometry(QtCore.QRect(190, 150, 401, 31))
        self.nameTextEdit.setTabChangesFocus(True)
        self.nameTextEdit.setObjectName(_fromUtf8("nameTextEdit"))
        self.emailLabel = QtGui.QLabel(GenerateForm1Dialog)
        self.emailLabel.setGeometry(QtCore.QRect(10, 190, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.emailTextEdit = QtGui.QPlainTextEdit(GenerateForm1Dialog)
        self.emailTextEdit.setGeometry(QtCore.QRect(190, 180, 401, 31))
        self.emailTextEdit.setTabChangesFocus(True)
        self.emailTextEdit.setObjectName(_fromUtf8("emailTextEdit"))
        self.passphraseLabel = QtGui.QLabel(GenerateForm1Dialog)
        self.passphraseLabel.setGeometry(QtCore.QRect(10, 320, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passphraseLabel.setFont(font)
        self.passphraseLabel.setObjectName(_fromUtf8("passphraseLabel"))
        self.passphraseTextEdit = QtGui.QPlainTextEdit(GenerateForm1Dialog)
        self.passphraseTextEdit.setGeometry(QtCore.QRect(190, 310, 361, 31))
        self.passphraseTextEdit.setTabChangesFocus(True)
        self.passphraseTextEdit.setObjectName(_fromUtf8("passphraseTextEdit"))
        self.passphraseTipsTextEdit = QtGui.QLabel(GenerateForm1Dialog)
        self.passphraseTipsTextEdit.setGeometry(QtCore.QRect(20, 220, 561, 81))
        font = QtGui.QFont()
        font.setItalic(True)
        self.passphraseTipsTextEdit.setFont(font)
        self.passphraseTipsTextEdit.setObjectName(_fromUtf8("passphraseTipsTextEdit"))
        self.pushButton_2 = QtGui.QPushButton(GenerateForm1Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 360, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.passphraseLengthLabel = QtGui.QLabel(GenerateForm1Dialog)
        self.passphraseLengthLabel.setGeometry(QtCore.QRect(560, 320, 51, 20))
        self.passphraseLengthLabel.setObjectName(_fromUtf8("passphraseLengthLabel"))

        self.retranslateUi(GenerateForm1Dialog)
        QtCore.QMetaObject.connectSlotsByName(GenerateForm1Dialog)

    def retranslateUi(self, GenerateForm1Dialog):
        GenerateForm1Dialog.setWindowTitle(_translate("GenerateForm1Dialog", "VAIDA - Choose Key", None))
        self.existingPGPLabel.setText(_translate("GenerateForm1Dialog", "Already  have a PGP Key?", None))
        self.loadKeyButton.setText(_translate("GenerateForm1Dialog", "Load Key", None))
        self.newPGPLabel.setText(_translate("GenerateForm1Dialog", "Otherwise, generate a new key:", None))
        self.nameLabel.setText(_translate("GenerateForm1Dialog", "Your name:", None))
        self.emailLabel.setText(_translate("GenerateForm1Dialog", "Your email address:", None))
        self.passphraseLabel.setText(_translate("GenerateForm1Dialog", "Passphrase", None))
        self.passphraseTipsTextEdit.setText(_translate("GenerateForm1Dialog", "Your passphrase should be at least 20 characters long and should be as difficult\n"
"to guess as possible.It should contain words not found in the dictionary.\n"
"\n"
"For example: \"Dirty loondry! Boundry. Stash/\"", None))
        self.pushButton_2.setText(_translate("GenerateForm1Dialog", "Generate Key", None))
        self.passphraseLengthLabel.setText(_translate("GenerateForm1Dialog", "<n>", None))

