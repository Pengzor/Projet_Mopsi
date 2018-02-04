from PyQt4.QtGui import *

class WindowWait(QWidget):
    def __init__(self, largeur = 400, hauteur = 100):
        
        #--------Geometry of the window--------
        super().__init__()
        self.nom = "Solving in progress"
        self.largeur = largeur
        self.hauteur = hauteur
        
        self.setWindowTitle(self.nom)
        self.setGeometry(300, 300, self.largeur, self.hauteur)
        #self.setWindowIcon(QIcon("icone.jpg"))
        
        self.show()