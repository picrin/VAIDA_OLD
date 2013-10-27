import sys
from PyQt4.QtGui import QApplication, QDialog, QMessageBox
from HomeLayout import *
from GenerateForm1 import *
from os.path import expanduser
from VideoVerificationForm import *

class VAIDAApp (QApplication) :

    # List of open windows to keep reference in app
    global openWindows
    
    def onCreateButtonClicked(self):
        # Create
        showGenerateForm1(self)
        self.window.close()

    def onVerifyButtonClicked(self):
        # Verify
        homeDir = expanduser("~")
        fname = QtGui.QFileDialog.getOpenFileName(caption="Choose a VAIDA file", directory=homeDir)
        showVideoVerificationForm(self, videoPath=fname)
        self.window.close()

    def closeApp(self):
        # Kill the app
        self.exit(0)
        
    def __init__(self, argv):
        super(VAIDAApp, self).__init__(argv)
        self.window = QDialog()
        self.ui = Ui_HomeDialog()
        self.ui.setupUi(self.window)
        
        # Add button connections and last window closed kills app
        self.connect(self.ui.createButton, QtCore.SIGNAL("clicked()"), self.onCreateButtonClicked)
        self.connect(self.ui.verifyButton, QtCore.SIGNAL("clicked()"), self.onVerifyButtonClicked)
        self.connect(self, QtCore.SIGNAL("lastWindowClosed()"), self.closeApp)
        
        self.window.show()
        
        # Add HomeForm window to openWindows list
        self.openWindows = [self.window]
        
        # Start QApplication loop
        sys.exit(self.exec_())
			
VAIDAApp(sys.argv)