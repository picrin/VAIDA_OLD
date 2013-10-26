# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GenerateForm1Layout.ui'
#
# Created: Sat Oct 26 20:31:04 2013
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

class Ui_GenerateForm1(object):
    def setupUi(self, GenerateForm1):
        GenerateForm1.setObjectName(_fromUtf8("GenerateForm1"))
        GenerateForm1.resize(412, 306)
        self.ExistingPGPLabel = QtGui.QLabel(GenerateForm1)
        self.ExistingPGPLabel.setGeometry(QtCore.QRect(90, 0, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ExistingPGPLabel.setFont(font)
        self.ExistingPGPLabel.setObjectName(_fromUtf8("ExistingPGPLabel"))

        self.retranslateUi(GenerateForm1)
        QtCore.QMetaObject.connectSlotsByName(GenerateForm1)

    def retranslateUi(self, GenerateForm1):
        GenerateForm1.setWindowTitle(_translate("GenerateForm1", "Dialog", None))
        self.ExistingPGPLabel.setText(_translate("GenerateForm1", "Already  have a PGP Key?", None))

