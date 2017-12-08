import os
import sys

os.chdir('C:\\Users\\teovi\\Documents\\IMI\\Projet MoPSi\\')

from code.Fonctions import *
from appli.Screen import *
   

B=bloc(2,1)


QtGui.QApplication.setGraphicsSystem("raster")


    
app = QtGui.QApplication(sys.argv)

Dialog = QtGui.QDialog()
ui = Ui_Dialog(Dialog, app, B)
Dialog.show()
sys.exit(app.exec_())


