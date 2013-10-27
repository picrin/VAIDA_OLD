import sys
from PyQt4.QtGui import QApplication, QDialog, QMessageBox
#from PyQt4.phonon import MediaSource, VideoWidget
from PyQt4.phonon import Phonon
from VideoVerificationFormLayout import *
from KeySavedForm import *

class VideoVerificationForm (QDialog) :
        
    def checkBoxChecked(self, x):
        if (self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked() and self.ui.checkBox_3.isChecked() and self.ui.checkBox_4.isChecked()):
            newForm = KeySavedForm(self.app)
            self.window.close()
            newForm._exec()
   
    def __init__(self, app, videoPath):
        super(QDialog, self).__init__()
        self.window = QDialog()
        self.ui = Ui_VideoVerificationDialog()
        self.ui.setupUi(self.window)
        self.app = app
        
        # Set media
        self.source = Phonon.MediaSource(videoPath)
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
