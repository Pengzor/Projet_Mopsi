import os
import sys
import inspect


path = os.path.dirname(inspect.getfile(inspect.currentframe()))
os.chdir(path)
# print(os.getcwd())

from codes.Fonctions import *
from appli.Screen import *
   
QtGui.QApplication.setGraphicsSystem("raster")


    
app = QtGui.QApplication(sys.argv)

Dialog = QtGui.QDialog()
ui = Ui_Dialog(Dialog, app)
Dialog.show()
sys.exit(app.exec_())


