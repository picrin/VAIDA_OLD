#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create a simple
window in PyQt4.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui


def main():
    
    app = QtGui.QApplication(sys.argv)



    w = QtGui.QWidget()
    w.resize(800, 600)
    w.move(400, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    isBiometrics = QtGui.QCheckBox("biometrics OK", parent = w)
    isKeyProperties = QtGui.QCheckBox("the fingerprint is letter by letter identical with the ")
    layout = QtGui.QVBoxLayout()
    
    layout.addWidget(isBiometrics)
    layout.addWidget(isKeyProperties)
    
    w.setLayout(layout)
    w.show()
    #isBiometrics.show()
    #isKeyProperties.show()
    print layout.__dict__
    sys.exit(app.exec_())
    


if __name__ == '__main__':
    main()
