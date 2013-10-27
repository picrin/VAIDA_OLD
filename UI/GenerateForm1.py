import sys
from PyQt4.QtGui import QApplication, QDialog
from GenerateForm1Layout import *

def showGenerateForm1(app):
    #Set up window
    window = QDialog()
    ui = Ui_GenerateForm1Dialog()
    ui.setupUi(window)
    window.show()
    
    # Add GenerateForm1 window to openWindows
    app.openWindows = app.openWindows + [window]
