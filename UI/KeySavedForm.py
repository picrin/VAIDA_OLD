from PyQt4.QtGui import QDialog, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QPixmap
from KeySavedFormLayout import Ui_keySavedDialog

class KeySavedForm (QDialog):
    
    def okayClicked(self):
        self.close()

    def __init__(self, app):
        super(QDialog, self).__init__()
        
        #Set up window
        self.ui = Ui_keySavedDialog()
        self.ui.setupUi(self)
        
        # Set up connections
        self.ui.okayButton.clicked.connect(self.okayClicked)

        # Set checkmark image
        scene = QGraphicsScene()
        item = QGraphicsPixmapItem(QPixmap("checkmark.png"))
        scene.addItem(item)
        self.ui.checkMarkGraphicsView.setScene(scene)
        
        self.show()
