from PyQt4.QtGui import QDialog
from GenerateForm1Layout import Ui_GenerateForm1Dialog
from PrivateKeySelector import PrivateKeySelector
from MakeVideoForm import MakeVideoForm
from gpglib import generate_gpg_key

class GenerateForm1 (QDialog):
    
    def passphraseChanged(self):
        self.ui.passphraseLengthLabel.setText(str(len(self.ui.passphraseTextEdit.toPlainText())))
    
    def startKeySelector(self):
        newForm = PrivateKeySelector(self.app)
        self.close()
        newForm.exec()
    
    def startMakeVideo(self):
        form = MakeVideoForm(self.app)
        self.close()
        form.exec()
    
    def generateKeyClicked(self):
        realName = self.ui.nameTextEdit.toPlainText()
        # TODO Ask for nickname?
        nickname = ""
        email = self.ui.emailTextEdit.toPlainText()
        passphrase = self.ui.passphraseTextEdit.toPlainText()
        # TODO Loading message. Ask for entropy.
        print ("App will now hang. Please provide entropy.")
        generate_gpg_key(realName, nickname, email, passphrase) 
        print ("Complete")
        self.startKeySelector()

    
    def __init__(self, app):
        super(QDialog, self).__init__()
        self.app = app
        
        #Set up window
        #self.window = QDialog()
        self.ui = Ui_GenerateForm1Dialog()
        self.ui.setupUi(self)
        
        # Set up connections
        self.ui.passphraseTextEdit.textChanged.connect(self.passphraseChanged)
        self.ui.loadKeyButton.clicked.connect(self.startKeySelector)
        self.ui.generateKeyButton.clicked.connect(self.generateKeyClicked)
        
        self.show()
        #self.window.show()
        
        # Add GenerateForm1 window to openWindows
        #app.openWindows = app.openWindows + [self.window]


