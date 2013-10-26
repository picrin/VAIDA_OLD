import sys
from PyQt4.QtGui import QApplication, QDialog, QMessageBox
from HomeLayout import *
from GenerateForm1 import *

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Home()
ui.setupUi(window)

def onCreateButtonClicked():
    print "hello"
    # Create
    window.close()
    #showGenerateForm1()
    pass

def onVerifyButtonClicked():
    # Verify
    window.close()
    showGenerateForm1()

app.connect(ui.createButton, QtCore.SIGNAL("clicked()"), onCreateButtonClicked)
app.connect(ui.verifyButton, QtCore.SIGNAL("clicked()"), onVerifyButtonClicked)

window.show()
sys.exit(app.exec_())
