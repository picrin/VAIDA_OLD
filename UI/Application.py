import sys
from PyQt4.QtGui import QApplication, QDialog, QMessageBox
from HomeLayout import *
from GenerateForm1 import *
from os.path import expanduser
from VideoVerificationForm import *

class VAIDAApp (QApplication) :
    
    def onCreateButtonClicked(self):
        # Create
        form = GenerateForm1(self)
        self.window.close()
        form.exec()

    def onVerifyButtonClicked(self):
        # Verify
        homeDir = expanduser("~")
        fname = str(QtGui.QFileDialog.getOpenFileName(caption="Choose a VAIDA file", directory=homeDir))
        if len(fname) == 0:
            # No file selected (dialog cancelled)
            return
        form = VideoVerificationForm(self, vaidaPath=fname)
        self.window.close()
        form.exec()

    def closeApp(self):
        # Kill the app
        self.exit(0)
        
    def __init__(self, argv):
        super(VAIDAApp, self).__init__(argv)
        self.window = QDialog()
        self.ui = Ui_HomeDialog()
        self.ui.setupUi(self.window)
        
        # Add button connections and last window closed kills app
        self.ui.createButton.clicked.connect(self.onCreateButtonClicked)
        self.ui.verifyButton.clicked.connect(self.onVerifyButtonClicked)
        self.lastWindowClosed.connect(self.closeApp)
        
        self.window.show()
        
        # Start QApplication loop
        sys.exit(self.exec_())

VAIDAApp(sys.argv)
