# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KeySavedFormLayout.ui'
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

class Ui_keySavedDialog(object):
    def setupUi(self, keySavedDialog):
        keySavedDialog.setObjectName(_fromUtf8("keySavedDialog"))
        keySavedDialog.resize(315, 304)
        self.checkMarkGraphicsView = QtGui.QGraphicsView(keySavedDialog)
        self.checkMarkGraphicsView.setGeometry(QtCore.QRect(30, 10, 256, 192))
        self.checkMarkGraphicsView.setObjectName(_fromUtf8("checkMarkGraphicsView"))
        self.keyIsLabel = QtGui.QLabel(keySavedDialog)
        self.keyIsLabel.setGeometry(QtCore.QRect(-20, 210, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.keyIsLabel.setFont(font)
        self.keyIsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.keyIsLabel.setObjectName(_fromUtf8("keyIsLabel"))
        self.okayButton = QtGui.QPushButton(keySavedDialog)
        self.okayButton.setGeometry(QtCore.QRect(80, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okayButton.setFont(font)
        self.okayButton.setObjectName(_fromUtf8("okayButton"))

        self.retranslateUi(keySavedDialog)
        QtCore.QMetaObject.connectSlotsByName(keySavedDialog)

    def retranslateUi(self, keySavedDialog):
        keySavedDialog.setWindowTitle(_translate("keySavedDialog", "VAIDA - Key Saved", None))
        self.keyIsLabel.setText(_translate("keySavedDialog", "The new key has been saved", None))
        self.okayButton.setText(_translate("keySavedDialog", "Okay", None))

