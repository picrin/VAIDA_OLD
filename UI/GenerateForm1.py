import sys
from PyQt4.QtGui import QApplication, QDialog
from GenerateForm1Layout import *

def showGenerateForm1():
    print "Showing Form1"
    app = QApplication(sys.argv)
    window = QDialog()
    ui = Ui_GenerateForm1()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
