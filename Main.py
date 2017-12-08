import os
import sys

os.chdir('C:\\Users\\teovi\\Documents\\IMI\\Projet MoPSi\\')

from code.Fonctions import *
from appli.Screen import *
   
QtGui.QApplication.setGraphicsSystem("raster")


    
app = QtGui.QApplication(sys.argv)

Dialog = QtGui.QDialog()
ui = Ui_Dialog(Dialog, app)
Dialog.show()
sys.exit(app.exec_())


