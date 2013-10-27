import sys
from PyQt4.QtGui import QApplication, QDialog, QMessageBox
#from PyQt4.phonon import MediaSource, VideoWidget
from PyQt4.phonon import Phonon
from VideoVerificationFormLayout import *

class VideoVerificationForm (QDialog) :
        
    def __init__(self, app, videoPath):
        super(QDialog, self).__init__()
        self.window = QDialog()
        self.ui = Ui_VideoVerificationDialog()
        self.ui.setupUi(self.window)
        
        # Set media
        self.source = Phonon.MediaSource(videoPath)
        self.media = Phonon.MediaObject()
        self.media.setCurrentSource(self.source)
        self.video = Phonon.VideoWidget(self.ui.videoPlayerWidget)
        self.video.setMinimumSize(400, 400)
        
        # Scale mode - 0 = do not scale, 1 = scale and crop
        self.video.setScaleMode(Phonon.VideoWidget.ScaleMode(1))
        
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self.ui.videoPlayerWidget)
        Phonon.createPath(self.media, self.audio)
        Phonon.createPath(self.media, self.video)
        
        self.window.show()
        
        # Add VideoVerificationForm window to openWindows list
        #app.openWindows = app.openWindows + [self]
        
        self.media.play()
			
#VAIDAApp(sys.argv)