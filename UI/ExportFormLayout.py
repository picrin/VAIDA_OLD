# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExportFormLayout.ui'
#
# Created: Wed Dec 11 19:45:36 2013
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

class Ui_exportDialog(object):
    def setupUi(self, exportDialog):
        exportDialog.setObjectName(_fromUtf8("exportDialog"))
        exportDialog.resize(400, 182)
        self.readyLabel = QtGui.QLabel(exportDialog)
        self.readyLabel.setGeometry(QtCore.QRect(10, 20, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.readyLabel.setFont(font)
        self.readyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.readyLabel.setObjectName(_fromUtf8("readyLabel"))
        self.pushButton = QtGui.QPushButton(exportDialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 120, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(exportDialog)
        QtCore.QMetaObject.connectSlotsByName(exportDialog)

    def retranslateUi(self, exportDialog):
        exportDialog.setWindowTitle(_translate("exportDialog", "Export", None))
        self.readyLabel.setText(_translate("exportDialog", "Ready to Go!", None))
        self.pushButton.setText(_translate("exportDialog", "Export VAIDA", None))

