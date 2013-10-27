import sys
from PyQt4.QtGui import QApplication, QDialog
from GenerateForm1Layout import *
from PrivateKeySelector import *

class GenerateForm1 (QDialog):
    
    def passphraseChanged(self):
        self.ui.passphraseLengthLabel.setText(str(len(self.ui.passphraseTextEdit.toPlainText())))
    
    def loadKeyClicked(self):
        newForm = PrivateKeySelector(self.app)
        self.window.close()
        newForm._exec()
    
    def __init__(self, app):
        super(QDialog, self).__init__()
        self.app = app
        
        #Set up window
        self.window = QDialog()
        self.ui = Ui_GenerateForm1Dialog()
        self.ui.setupUi(self.window)
        
        # Set up connections
        self.ui.passphraseTextEdit.textChanged.connect(self.passphraseChanged)
        self.ui.loadKeyButton.clicked.connect(self.loadKeyClicked)
        
        self.window.show()
        
        # Add GenerateForm1 window to openWindows
        #app.openWindows = app.openWindows + [self.window]


