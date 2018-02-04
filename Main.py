import os
import sys
import inspect

path = os.path.dirname(inspect.getfile(inspect.currentframe()))
os.chdir(path)

from codes.Fonctions import *
from appli.Screen import *

QtGui.QApplication.setGraphicsSystem("raster")    
app = QtGui.QApplication(sys.argv)

Dialog = QtGui.QDialog()
ui = Interface(Dialog, app)
Dialog.show()
sys.exit(app.exec_())