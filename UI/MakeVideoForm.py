from PyQt4.QtGui import QDialog, QFileDialog, QMessageBox
from MakeVideoFormLayout import Ui_MakeVideoForm
from gpglib import public_keys_details, create_vaida
import re
from uIntToString import uIntToString
from os.path import expanduser

class MakeVideoForm (QDialog):
    
    def showMessage(self, text):
        message = QMessageBox()
        message.setText(text)
        message.exec()

    def importVideo(self):
        homeDir = expanduser("~")
        fname = str(QFileDialog.getOpenFileName(caption="Import a video", directory=homeDir))
        try:
            vaida_path = create_vaida(fname, self.passphrase, self.keyID)
        except GPGException as e:
            self.showMessage(str(e))
            return
        self.showMessage("VAIDA created at " + vaida_path)
        exit()
    
    def extract_name_and_email(self, uid):
        result = re.search('(.*?)<(.*?)>', uid, flags=0)
        if not result:
            # Name and email not found
            return '', ''
        return result.groups()

    def __init__(self, app, passphrase, keyID):
        super(QDialog, self).__init__()
        self.app = app
        self.passphrase = passphrase
        self.keyID = keyID
        
        #Set up window
        self.ui = Ui_MakeVideoForm()
        self.ui.setupUi(self)
        
        print (keyID)
        print (public_keys_details())
        
        # Handle key error here?
        key = public_keys_details()[keyID]
        if not key:
            # Key not found
            self.window.show()
            return
        
        print (key['uid'])
        
        name, email = self.extract_name_and_email(key['uid'])
        
        keyExpiry = key['expires']
        if keyExpiry == '':
            expiry = "None"
        else:
            expiry = uIntToString(keyExpiry)
        
        date = uIntToString(key['date'])
        fingerprint = key['fingerprint']
        
        print (name)
        print (email)
        
        self.ui.nameLabel.setText("Name: " + name)
        self.ui.emailLabel.setText("Email: " + email)
        self.ui.expiresLabel.setText("Expiry: " + expiry)
        self.ui.dateLabel.setText("Date: " + date)
        self.ui.fingerprintTextEdit.setText(fingerprint)
        
        self.ui.importVideoButton.clicked.connect(self.importVideo)
        # Set up connections
        #self.ui.passphraseTextEdit.textChanged.connect(self.passphraseChanged)
        #self.ui.loadKeyButton.clicked.connect(self.loadKeyClicked)
        
        self.show()
        
        # Add GenerateForm1 window to openWindows
        #app.openWindows = app.openWindows + [self.window]


