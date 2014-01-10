import sys
from PyQt4.QtGui import QApplication, QDialog
from PrivateKeySelectorDialog import *
from PyQt4.QtGui import QListWidgetItem
from gpglib import *
from MakeVideoForm import *

def showPrivateKeySelector(app):
    PrivateKeySelector(app)

class PrivateKeySelector (QDialog):
    
    def startMakeVideo(self, passphrase, keyID):
        form = MakeVideoForm(self.app, passphrase, keyID)
        self.window.close()
        form._exec()
    
    def __init__(self, app):
        #Set up window
        self.window = QDialog()
        self.ui = Ui_PrivateKeySelectorDialog()
        self.ui.setupUi(self.window)
        
        keysDict = private_keys_users()
        
        for key in keysDict.keys():
            #item = QListWidgetItem(key)
            #self.ui.keyListWidget.insertItem(item)
            self.ui.keyListWidget.addItem(key)
        
        #self.ui.privateKeyList = private_keys_users().keys()
        
        self.ui.selectKeyButton.clicked.connect(self.selectKey)
        
        self.window.show()
        
    def selectKey(self):
        # TODO rename "lineEdit" to something descriptive
        passphrase = self.ui.lineEdit.text()
        keyID = "123"
        self.startMakeVideo(passphrase, keyID)
        
