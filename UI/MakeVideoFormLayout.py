# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MakeVideoFormLayout.ui'
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

class Ui_MakeVideoForm(object):
    def setupUi(self, MakeVideoForm):
        MakeVideoForm.setObjectName(_fromUtf8("MakeVideoForm"))
        MakeVideoForm.resize(539, 525)
        self.keyIsLabel = QtGui.QLabel(MakeVideoForm)
        self.keyIsLabel.setGeometry(QtCore.QRect(20, 30, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.keyIsLabel.setFont(font)
        self.keyIsLabel.setObjectName(_fromUtf8("keyIsLabel"))
        self.instructionsLabel = QtGui.QLabel(MakeVideoForm)
        self.instructionsLabel.setGeometry(QtCore.QRect(10, 340, 511, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.instructionsLabel.setFont(font)
        self.instructionsLabel.setObjectName(_fromUtf8("instructionsLabel"))
        self.importVideoButton = QtGui.QPushButton(MakeVideoForm)
        self.importVideoButton.setGeometry(QtCore.QRect(150, 450, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.importVideoButton.setFont(font)
        self.importVideoButton.setObjectName(_fromUtf8("importVideoButton"))
        self.layoutWidget = QtGui.QWidget(MakeVideoForm)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 190, 511, 151))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.nameLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.verticalLayout.addWidget(self.nameLabel)
        self.emailLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.verticalLayout.addWidget(self.emailLabel)
        self.expiresLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.expiresLabel.setFont(font)
        self.expiresLabel.setObjectName(_fromUtf8("expiresLabel"))
        self.verticalLayout.addWidget(self.expiresLabel)
        self.dateLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName(_fromUtf8("dateLabel"))
        self.verticalLayout.addWidget(self.dateLabel)
        self.fingerprintTextEdit = QtGui.QTextEdit(MakeVideoForm)
        self.fingerprintTextEdit.setGeometry(QtCore.QRect(10, 70, 521, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fingerprintTextEdit.setFont(font)
        self.fingerprintTextEdit.setObjectName(_fromUtf8("fingerprintTextEdit"))

        self.retranslateUi(MakeVideoForm)
        QtCore.QMetaObject.connectSlotsByName(MakeVideoForm)

    def retranslateUi(self, MakeVideoForm):
        MakeVideoForm.setWindowTitle(_translate("MakeVideoForm", "VAIDA - Your Video", None))
        self.keyIsLabel.setText(_translate("MakeVideoForm", "Your key fingerprint is:", None))
        self.instructionsLabel.setText(_translate("MakeVideoForm", "Instructions + link", None))
        self.importVideoButton.setText(_translate("MakeVideoForm", "Import Video", None))
        self.nameLabel.setText(_translate("MakeVideoForm", "Name:", None))
        self.emailLabel.setText(_translate("MakeVideoForm", "Email Address:", None))
        self.expiresLabel.setText(_translate("MakeVideoForm", "Expires:", None))
        self.dateLabel.setText(_translate("MakeVideoForm", "Date:", None))
        self.fingerprintTextEdit.setHtml(_translate("MakeVideoForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fingerprint Goes Here</p></body></html>", None))

