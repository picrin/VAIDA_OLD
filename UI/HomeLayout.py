# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeLayout.ui'
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

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName(_fromUtf8("Home"))
        Home.resize(544, 202)
        self.horizontalLayoutWidget = QtGui.QWidget(Home)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 2, 2))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.createLabel = QtGui.QLabel(Home)
        self.createLabel.setGeometry(QtCore.QRect(20, 20, 201, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.createLabel.setFont(font)
        self.createLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.createLabel.setObjectName(_fromUtf8("createLabel"))
        self.createButton = QtGui.QPushButton(Home)
        self.createButton.setGeometry(QtCore.QRect(30, 140, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.createButton.setFont(font)
        self.createButton.setObjectName(_fromUtf8("createButton"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Home)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(269, -1, 2, 2))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verifyButton = QtGui.QPushButton(Home)
        self.verifyButton.setGeometry(QtCore.QRect(310, 140, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.verifyButton.setFont(font)
        self.verifyButton.setObjectName(_fromUtf8("verifyButton"))
        self.verifyLabel = QtGui.QLabel(Home)
        self.verifyLabel.setGeometry(QtCore.QRect(290, 20, 201, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.verifyLabel.setFont(font)
        self.verifyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.verifyLabel.setObjectName(_fromUtf8("verifyLabel"))
        self.line = QtGui.QFrame(Home)
        self.line.setGeometry(QtCore.QRect(250, 20, 20, 161))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        Home.setWindowTitle(_translate("Home", "Dialog", None))
        self.createLabel.setText(_translate("Home", "I want to create\n"
" a VAIDA", None))
        self.createButton.setText(_translate("Home", "Create", None))
        self.verifyButton.setText(_translate("Home", "Verify", None))
        self.verifyLabel.setText(_translate("Home", "I want to verify\n"
" a VAIDA", None))

