import os
import sys

<<<<<<< HEAD
os.chdir('D:\\Documents\\Ponts ParisTech\\Projet MOPSI\\Projet')

from codes.Fonctions import *
=======
os.chdir('C:\\Users\\teovi\\Documents\\IMI\\Projet MoPSi\\')

from code.Fonctions import *
>>>>>>> 2eb49d4a97e65232c76b141790c3b43804b711b7
from appli.Screen import *
   
QtGui.QApplication.setGraphicsSystem("raster")


    
app = QtGui.QApplication(sys.argv)

Dialog = QtGui.QDialog()
ui = Ui_Dialog(Dialog, app)
Dialog.show()
sys.exit(app.exec_())


