from PyQt4.QtGui import QApplication, QDialog
from KeySavedFormLayout import *

class KeySavedForm (QDialog):
    
    def okayClicked(self):
        self.window.close()

    def __init__(self, app):
        super(QDialog, self).__init__()
        
        #Set up window
        self.window = QDialog()
        self.ui = Ui_keySavedDialog()
        self.ui.setupUi(self.window)
        
        # Set up connections
        self.ui.okayButton.clicked.connect(self.okayClicked)
        
        self.window.show()
        
        # Add GenerateForm1 window to openWindows
        #app.openWindows = app.openWindows + [self.window]
        
app = QApplication([])
form = KeySavedForm(app)
form._exec()