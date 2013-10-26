import sys
from PyQt4.QtGui import QApplication, QDialog, QMessageBox
from HomeLayout import *
from GenerateForm1 import *

class HomeForm (object) :

    def onCreateButtonClicked(self):
        # Create
        self.window.close()

    def onVerifyButtonClicked(self):
        # Verify
        self.latestWindow = showGenerateForm1()
        self.window.close()

    def closeApp(self):
        self.app.exit(0)
        
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QDialog()
        self.ui = Ui_Home()
        self.ui.setupUi(self.window)
        self.app.connect(self.ui.createButton, QtCore.SIGNAL("clicked()"), self.onCreateButtonClicked)
        self.app.connect(self.ui.verifyButton, QtCore.SIGNAL("clicked()"), self.onVerifyButtonClicked)
        self.app.connect(self.app, QtCore.SIGNAL("lastWindowClosed()"), self.closeApp)
        self.window.show()
        sys.exit(self.app.exec_())
			
HomeForm()