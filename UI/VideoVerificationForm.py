import sys
from PyQt4.QtGui import QApplication, QDialog, QMessageBox
#from PyQt4.phonon import MediaSource, VideoWidget
from PyQt4.phonon import Phonon
from VideoVerificationFormLayout import *
from KeySavedForm import *
from gpglib import untar_verify_vaida, add_tmp_to_keyring
from PyQt4.QtGui import QMessageBox
import os.path
import uIntToString

class VideoVerificationForm (QDialog) :
        
    def checkBoxChecked(self, x):
        if (self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked() and self.ui.checkBox_3.isChecked() and self.ui.checkBox_4.isChecked()):
            add_tmp_to_keyring()
            newForm = KeySavedForm(self.app)
            self.window.close()
            newForm._exec()
   
    def __init__(self, app, vaidaPath):
        super(QDialog, self).__init__()
        
        success, fingerprint, absoluteVideoPath, dateUInt = untar_verify_vaida(vaidaPath)
        
        expirationDate = uIntToString.uIntToString(dateUInt)
        
        if not success:
            #TODO QMessageBox
            #Delete tmp?
            return
        
        self.window = QDialog()
        self.ui = Ui_VideoVerificationDialog()
        self.ui.setupUi(self.window)
        self.app = app
        
        # Set text
        self.ui.fingerprintLabel.setText("Key fingerprint: " + fingerprint)
        self.ui.keyExpirationLabel.setText("Key expiration date: " + expirationDate)
        
        # Set media
        self.source = Phonon.MediaSource(absoluteVideoPath)
        self.media = Phonon.MediaObject()
        self.media.setCurrentSource(self.source)
        self.video = Phonon.VideoWidget(self.ui.videoPlayerWidget)
        self.video.setMinimumSize(600, 600)
        
        # Scale mode - 0 = do not scale, 1 = scale and crop
        self.video.setScaleMode(Phonon.VideoWidget.ScaleMode(0))
        
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self.ui.videoPlayerWidget)
        Phonon.createPath(self.media, self.audio)
        Phonon.createPath(self.media, self.video)
        
        self.ui.checkBox.stateChanged.connect(self.checkBoxChecked)
        self.ui.checkBox_2.stateChanged.connect(self.checkBoxChecked)
        self.ui.checkBox_3.stateChanged.connect(self.checkBoxChecked)
        self.ui.checkBox_4.stateChanged.connect(self.checkBoxChecked)
        
        self.window.show()
        
        # Add VideoVerificationForm window to openWindows list
        #app.openWindows = app.openWindows + [self]
        
        self.media.play()
			
#VAIDAApp(sys.argv)
