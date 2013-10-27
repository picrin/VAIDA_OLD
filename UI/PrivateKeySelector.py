import sys
from PyQt4.QtGui import QApplication, QDialog
from PrivateKeySelectorDialog import *
#from gpglib import *

def showPrivateKeySelector(app):
    PrivateKeySelector(app)

class PrivateKeySelector (QDialog):
    
    def __init__(self, app):
        #Set up window
        self.window = QDialog()
        self.ui = Ui_PrivateKeySelectorDialog()
        self.ui.setupUi(self.window)
        
        #self.ui.privateKeyList = private_keys_users().keys()
        
        #self.ui.passphraseTextEdit.textChanged.connect(self.passphraseChanged)
        #self.ui.passphraseTextEdit.textChanged.emit()
        #self.app.connect(self.ui.passphraseTextEdit, QtCore.SIGNAL("textChanged()"), self.passphraseChanged)
        #self.ui.passphraseTextEdit.textChanged.emit()
        
        #self.ui.loadKeyButton.clicked.connect(self.loadKeyClicked)
        
        self.window.show()
        
        # Add GenerateForm1 window to openWindows
        app.openWindows = app.openWindows + [self.window]