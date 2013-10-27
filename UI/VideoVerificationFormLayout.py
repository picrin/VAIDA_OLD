# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoVerificationFormLayout.ui'
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

class Ui_VideoVerificationDialog(object):
    def setupUi(self, VideoVerificationDialog):
        VideoVerificationDialog.setObjectName(_fromUtf8("VideoVerificationDialog"))
        VideoVerificationDialog.resize(694, 360)
        self.videoPlayerWidget = QtGui.QWidget(VideoVerificationDialog)
        self.videoPlayerWidget.setGeometry(QtCore.QRect(20, 10, 301, 261))
        self.videoPlayerWidget.setObjectName(_fromUtf8("videoPlayerWidget"))
        self.label = QtGui.QLabel(VideoVerificationDialog)
        self.label.setGeometry(QtCore.QRect(20, 280, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(VideoVerificationDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 310, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.widget = QtGui.QWidget(VideoVerificationDialog)
        self.widget.setGeometry(QtCore.QRect(330, -20, 351, 371))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox = QtGui.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.verticalLayout.addWidget(self.checkBox_4)

        self.retranslateUi(VideoVerificationDialog)
        QtCore.QMetaObject.connectSlotsByName(VideoVerificationDialog)

    def retranslateUi(self, VideoVerificationDialog):
        VideoVerificationDialog.setWindowTitle(_translate("VideoVerificationDialog", "VAIDA - Verify Video", None))
        self.label.setText(_translate("VideoVerificationDialog", "Key signature: <signature>", None))
        self.label_2.setText(_translate("VideoVerificationDialog", "Key expiration: <expiration>", None))
        self.checkBox.setText(_translate("VideoVerificationDialog", "Does this look like <name>?", None))
        self.checkBox_2.setText(_translate("VideoVerificationDialog", "Does this sound like <name>?", None))
        self.checkBox_3.setText(_translate("VideoVerificationDialog", "Do the key fingerprints match?", None))
        self.checkBox_4.setText(_translate("VideoVerificationDialog", "Do the key expiration dates match?", None))

