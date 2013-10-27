import sys
from PyQt4.QtGui import QApplication, QDialog
from GenerateForm1Layout import *

def showGenerateForm1(app):
    GenerateForm1(app)

class GenerateForm1 (QDialog):
    
    def passphraseChanged():
        print ("Passphrase changed signal received!")
        self.ui.passphraseLengthLabel.setText(str(len(self.ui.passphraseTextEdit.toPlainText())))
    
    def loadKeyClicked():
        print("ABC")
    
    def __init__(self, app):
        #Set up window
        self.window = QDialog()
        self.ui = Ui_GenerateForm1Dialog()
        self.ui.setupUi(self.window)
        self.app = app
        
        #self.ui.passphraseTextEdit.textChanged.connect(self.passphraseChanged)
        #self.ui.passphraseTextEdit.textChanged.emit()
        self.app.connect(self.ui.passphraseTextEdit, QtCore.SIGNAL("textChanged()"), self.passphraseChanged)
        #self.ui.passphraseTextEdit.textChanged.emit()
        
        #self.ui.loadKeyButton.clicked.connect(self.loadKeyClicked)
        
        self.window.show()
        
        # Add GenerateForm1 window to openWindows
        app.openWindows = app.openWindows + [self.window]