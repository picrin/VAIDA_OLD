from PyQt4.QtGui import QDialog, QLineEdit, QMessageBox
from GenerateForm1Layout import Ui_GenerateForm1Dialog
from PrivateKeySelector import PrivateKeySelector
from MakeVideoForm import MakeVideoForm
from gpglib import generate_gpg_key

class GenerateForm1 (QDialog):
    
    def passphraseChanged(self):
        self.ui.passphraseLengthLabel.setText(str(len(self.ui.passphraseLineEdit.text())))

    def showMessage(self, text):
        message = QMessageBox()
        message.setText(text)
        message.exec()
    
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
        if len(realName) == 0:
            self.showMessage("Please enter your name")
        nickname = self.ui.nicknameTextEdit.toPlainText()
        email = self.ui.emailTextEdit.toPlainText()
        if len(email) == 0:
            self.showMessage("Please enter your email address")
        passphrase = self.ui.passphraseLineEdit.text()
        if len(passphrase) == 0:
            self.showMessage("Please enter a passphrase")
        if passphrase != self.ui.repeatPassphraseLineEdit.text:
            self.showMessage("Passphrases do not match. Please try again")
        self.showMessage("When this message is dismissed app will hang. Please provide entropy.")
        print ("App will now hang. Please provide entropy.")
        generate_gpg_key(realName, nickname, email, passphrase) 
        print ("Complete")
        self.showMessage("Key generated")
        self.startKeySelector()

    
    def __init__(self, app):
        super(QDialog, self).__init__()
        self.app = app
        
        self.ui = Ui_GenerateForm1Dialog()
        self.ui.setupUi(self)
        
        # Set up connections
        self.ui.passphraseLineEdit.textChanged.connect(self.passphraseChanged)
        self.ui.loadKeyButton.clicked.connect(self.startKeySelector)
        self.ui.generateKeyButton.clicked.connect(self.generateKeyClicked)

        self.show()
