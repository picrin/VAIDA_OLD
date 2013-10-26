import sys
from PyQt4.QtGui import QApplication, QDialog, QMessageBox
from HomeLayout import *

def onCreateButtonClicked():
    # Create
    pass

def onVerifyButtonClicked():
    # Verify
    window.close()
    pass

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Home()
ui.setupUi(window)

app.connect(ui.createButton, QtCore.SIGNAL("clicked()"), onCreateButtonClicked)
app.connect(ui.verifyButton, QtCore.SIGNAL("clicked()"), onVerifyButtonClicked)

window.show()
sys.exit(app.exec_())
