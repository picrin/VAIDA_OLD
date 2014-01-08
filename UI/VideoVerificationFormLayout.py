# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoVerificationFormLayout.ui'
#
# Created: Wed Jan  8 00:29:53 2014
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
        VideoVerificationDialog.resize(895, 499)
        self.videoPlayerWidget = QtGui.QWidget(VideoVerificationDialog)
        self.videoPlayerWidget.setGeometry(QtCore.QRect(20, 10, 491, 431))
        self.videoPlayerWidget.setObjectName(_fromUtf8("videoPlayerWidget"))
        self.fingerprintLabel = QtGui.QLabel(VideoVerificationDialog)
        self.fingerprintLabel.setGeometry(QtCore.QRect(30, 450, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fingerprintLabel.setFont(font)
        self.fingerprintLabel.setObjectName(_fromUtf8("fingerprintLabel"))
        self.keyExpirationLabel = QtGui.QLabel(VideoVerificationDialog)
        self.keyExpirationLabel.setGeometry(QtCore.QRect(560, 450, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.keyExpirationLabel.setFont(font)
        self.keyExpirationLabel.setObjectName(_fromUtf8("keyExpirationLabel"))
        self.layoutWidget = QtGui.QWidget(VideoVerificationDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(530, 0, 351, 441))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.verticalLayout.addWidget(self.checkBox_4)

        self.retranslateUi(VideoVerificationDialog)
        QtCore.QMetaObject.connectSlotsByName(VideoVerificationDialog)

    def retranslateUi(self, VideoVerificationDialog):
        VideoVerificationDialog.setWindowTitle(_translate("VideoVerificationDialog", "VAIDA - Verify Video", None))
        self.fingerprintLabel.setText(_translate("VideoVerificationDialog", "Key fingerprint: 0C8E5995CD1770E5936D288ED98029C596F20E5D", None))
        self.keyExpirationLabel.setText(_translate("VideoVerificationDialog", "Key expiration: 27 October 2014", None))
        self.checkBox.setText(_translate("VideoVerificationDialog", "Does this look like Adam?", None))
        self.checkBox_2.setText(_translate("VideoVerificationDialog", "Does this sound like Adam?", None))
        self.checkBox_3.setText(_translate("VideoVerificationDialog", "Do the key fingerprints match?", None))
        self.checkBox_4.setText(_translate("VideoVerificationDialog", "Do the key expiration dates match?", None))

