import os
os.chdir('C:\\Users\\teovi\\Documents\\IMI\\Projet MoPSi\\')
from code.Classes import *
from code.Fonctions import *
from code.Pieces import *
from appli.Controller import *
from appli.ScreenBis import *

##

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    
    def __init__(self, Dialog, appli, bloc):
        self.n = 3
        self.m = 3
        self.res = int(900/max(self.n, self.m))
        self.grid = grid(self.n,self.m)
        self.app = appli
        self.pieces=pieces_default(self.n, self.m)

        self.bloc = bloc
        self.setupUi(Dialog)
        self.controller = Controller(self, self.grid, bloc, self.pieces, self.n, self.m)
        self.controller.bind()

        
    def setupUi(self, Dialog):
          
        app_icon = QtGui.QIcon()
        app_icon.addFile('logo.png', QtCore.QSize(238,238))
        self.app.setWindowIcon(app_icon)
        Dialog.setObjectName(_fromUtf8("Résolution de Puzzle"))
        Dialog.setEnabled(True)
        Dialog.resize(1600, 1100)
        
        
        ## Fenêtre d'affichage
        
        self.Scene = QtGui.QGraphicsScene(Dialog)
        self.DrawGrid()
        
        self.Screen = QtGui.QGraphicsView(self.Scene,Dialog)
        self.Screen.setGeometry(QtCore.QRect(50, 50, 1000, 1000))
        self.Screen.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.Screen.setObjectName(_fromUtf8("graphicsView"))
        
        self.Screen.setViewportUpdateMode(QtGui.QGraphicsView.FullViewportUpdate)
        
        
        ## Polices d'écriture
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        font2 = QtGui.QFont()
        font2.setFamily(_fromUtf8("Calibri"))
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        
        font3 = QtGui.QFont()
        font3.setPointSize(12)
        
        
        ## Texte Réglage
        
        self.label = QtGui.QLabel()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        
        
        ## PuzzleSize
        
        self.label_8 = QtGui.QLabel()
        self.label_8.setFont(font2)
        self.label_8.setAlignment(QtCore.Qt.AlignRight)
        self.label_8.setObjectName(_fromUtf8("label_8"))
  
        self.PuzzleSize = QtGui.QComboBox()
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PuzzleSize.sizePolicy().hasHeightForWidth())
        self.PuzzleSize.setSizePolicy(sizePolicy)
        self.PuzzleSize.setObjectName(_fromUtf8("PuzzleSize"))
        self.PuzzleSize.addItem(_fromUtf8(""))
        self.PuzzleSize.addItem(_fromUtf8(""))
        self.PuzzleSize.addItem(_fromUtf8(""))
        self.PuzzleSize.addItem(_fromUtf8(""))
        self.PuzzleSize.addItem(_fromUtf8(""))
        self.PuzzleSize.setMaximumWidth(90)
        
        self.ApplySizeButton = QtGui.QPushButton("Apply")
        self.ApplySizeButton.setMaximumHeight(35)
        self.ApplySizeButton.setMaximumWidth(150)
        
    
        ## RefreshPeriod
        
        self.label_9 = QtGui.QLabel()
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font2)
        self.label_9.setAlignment(QtCore.Qt.AlignRight)
        self.label_9.setObjectName(_fromUtf8("label_9"))        
    
        self.RefreshPeriod = QtGui.QComboBox()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RefreshPeriod.sizePolicy().hasHeightForWidth())
        self.RefreshPeriod.setSizePolicy(sizePolicy)
        self.RefreshPeriod.setObjectName(_fromUtf8("RefreshPeriod"))
        self.RefreshPeriod.addItem(_fromUtf8(""))
        self.RefreshPeriod.addItem(_fromUtf8(""))
        self.RefreshPeriod.addItem(_fromUtf8(""))
        self.RefreshPeriod.addItem(_fromUtf8(""))
        self.RefreshPeriod.addItem(_fromUtf8(""))
        self.RefreshPeriod.setMinimumWidth(90)
        
        self.ApplyPeriodButton = QtGui.QPushButton("Apply")
        self.ApplyPeriodButton.setMaximumHeight(35)
        self.ApplyPeriodButton.setMaximumWidth(150)

        
        
        ## SolveMethod
        
        self.label_10 = QtGui.QLabel()
        self.label_10.setFont(font2)
        self.label_10.setAlignment(QtCore.Qt.AlignRight)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        
        self.SolveMethod = QtGui.QComboBox()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SolveMethod.sizePolicy().hasHeightForWidth())
        self.SolveMethod.setSizePolicy(sizePolicy)
        self.SolveMethod.setObjectName(_fromUtf8("SolveMethod"))
        self.SolveMethod.addItem(_fromUtf8(""))
        self.SolveMethod.addItem(_fromUtf8(""))
        self.SolveMethod.addItem(_fromUtf8(""))
        self.SolveMethod.addItem(_fromUtf8(""))
        self.SolveMethod.setMinimumWidth(90)
        
        self.ApplyMethodButton = QtGui.QPushButton("Apply")
        self.ApplyMethodButton.setMaximumHeight(35)
        self.ApplyMethodButton.setMaximumWidth(150)
        
        
        ## UseMode
        
        self.label_2 = QtGui.QLabel()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.UseMode = QtGui.QComboBox()
        font = QtGui.QFont()
        font.setPointSize(11)
        self.UseMode.setFont(font)
        self.UseMode.setObjectName(_fromUtf8("UseMode"))
        self.UseMode.addItem(_fromUtf8(""))
        self.UseMode.addItem(_fromUtf8(""))
        self.UseMode.addItem(_fromUtf8(""))
        
        self.ApplyModeButton = QtGui.QPushButton("Apply")
        # self.ApplyModeButton.setMaximumHeight(35)
        # self.ApplyModeButton.setMaximumWidth(150)
        
        
        ## Boutons
        
        #SaveButton
        # self.SaveButton = QtGui.QPushButton('Save')
        # self.SaveButton.setFont(font3)

        
        #InterfButton
        self.InterfButton = QtGui.QPushButton("Open user Window")
        self.InterfButton.setFont(font3)
 
        
        #ResetButton
        self.ResetButton = QtGui.QPushButton("Reset") 
        self.ResetButton.setFont(font3)
        
        
        #InitButton
        self.InitButton = QtGui.QPushButton("Initialize")
        self.InitButton.setFont(font3)


        #SolveButton
        self.SolveButton = QtGui.QPushButton("Solve")
        self.SolveButton.setFont(font3)
        
        
        #PauseButton
        self.PauseButton = QtGui.QPushButton("Pause")
        self.PauseButton.setFont(font3)
     
     
        #PlaceBlocButton
        self.PlaceBlocButton = QtGui.QPushButton("Bloc Placement")
        self.PlaceBlocButton.setFont(font3)
        
        ##Compteur
        self.label_c = QtGui.QLabel("Number of tries :")
        self.label_c.setFont(font)
        self.label_c.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c.setObjectName(_fromUtf8("label_10"))
   
        self.CompteurLayout = QtGui.QHBoxLayout()
        self.CompteurLCD = QtGui.QLCDNumber()
        
        self.CompteurLayout.addWidget(self.label_c)
        self.CompteurLayout.addWidget(self.CompteurLCD)
        self.CompteurLCD.setDigitCount(8)
        self.CompteurLCD.setMaximumHeight(50)


        ## Mise en page 
        
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1080, 50, 468, 1021))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_2.addWidget(self.label_8)              
        self.horizontalLayout_2.addWidget(self.PuzzleSize)
        self.horizontalLayout_2.addWidget(self.ApplySizeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))        
        self.horizontalLayout_3.addWidget(self.label_9)
        self.horizontalLayout_3.addWidget(self.RefreshPeriod)
        self.horizontalLayout_3.addWidget(self.ApplyPeriodButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))        
        self.horizontalLayout_4.addWidget(self.label_10)
        self.horizontalLayout_4.addWidget(self.SolveMethod)
        self.horizontalLayout_4.addWidget(self.ApplyMethodButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)        
        # self.verticalLayout.addWidget(self.SaveButton)
        spacerItem = QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)        
        self.verticalLayout.addWidget(self.label_2)
        
        self.horizontalLayout_usemode = QtGui.QHBoxLayout()
        self.horizontalLayout_usemode.addWidget(self.UseMode)
        self.horizontalLayout_usemode.addWidget(self.ApplyModeButton)
        
        
        self.verticalLayout.addLayout(self.horizontalLayout_usemode)
              
        self.verticalLayout.addWidget(self.InterfButton)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)   
        self.verticalLayout.addWidget(self.PlaceBlocButton)
        self.verticalLayout.addItem(spacerItem)        
        self.verticalLayout.addWidget(self.ResetButton)
        self.verticalLayout.addWidget(self.InitButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))        
        self.horizontalLayout.addWidget(self.SolveButton)
        self.horizontalLayout.addWidget(self.PauseButton)        
        self.verticalLayout.addLayout(self.horizontalLayout)   
        self.verticalLayout.addLayout(self.CompteurLayout)
        
             
        self.Screen.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.PauseButton.setEnabled(False)
        self.SolveButton.setEnabled(False)
        self.ResetButton.setEnabled(False)
    

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Puzzle Solver", None))
        self.label.setText(_translate("Dialog", "Settings", None))
        self.label_8.setText(_translate("Dialog", "Puzzle Size ", None))
        self.PuzzleSize.setItemText(0, _translate("Dialog", "3x3", None))
        self.PuzzleSize.setItemText(1, _translate("Dialog", "4x4", None))
        self.PuzzleSize.setItemText(2, _translate("Dialog", "5x5", None))
        self.PuzzleSize.setItemText(3, _translate("Dialog", "6x6", None))
        self.PuzzleSize.setItemText(4, _translate("Dialog", "7x7", None))
        self.label_9.setText(_translate("Dialog", "Refresh Period ", None))
        self.RefreshPeriod.setItemText(0, _translate("Dialog", "10", None))
        self.RefreshPeriod.setItemText(1, _translate("Dialog", "100", None))
        self.RefreshPeriod.setItemText(2, _translate("Dialog", "300", None))
        self.RefreshPeriod.setItemText(3, _translate("Dialog", "500", None))
        self.RefreshPeriod.setItemText(4, _translate("Dialog", "1000", None))
        self.label_10.setText(_translate("Dialog", "Solve Method ", None))
        self.SolveMethod.setItemText(0, _translate("Dialog", "1", None))
        self.SolveMethod.setItemText(1, _translate("Dialog", "2", None))
        # self.SolveMethod.setItemText(2, _translate("Dialog", "3", None))
        # self.SolveMethod.setItemText(3, _translate("Dialog", "4", None))
        self.label_2.setText(_translate("Dialog", "Use Mode", None))
        self.UseMode.setItemText(0, _translate("Dialog", "Default", None))
        self.UseMode.setItemText(1, _translate("Dialog", "Place puzzle pieces", None))
        self.UseMode.setItemText(2, _translate("Dialog", "Create own puzzle", None))

    
    def Success(self, n, m, compteur):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        
        text = "Puzzle " + str(n) + "x" + str(m) + " solved in " + str(compteur) + " tries !"
        msg.setText(text)
        msg.setWindowTitle("Success")
        msg.exec_()


    def DrawGrid(self):
        col= QtGui.QColor(255,255,255)
        pen = QtGui.QPen()
        pen.setWidth(3)
        brush = QtGui.QBrush(col)
        e=3
        self.Scene.addRect(-e, -e, self.m*self.res + 2*e, self.n*self.res + 2*e, pen , brush )
    
    
    def DrawRect(self,x ,y, col):
        pen = QtGui.QPen()
        col1= QtGui.QColor(40,40,40)
        gradient = QtGui.QRadialGradient(x*self.res + self.res/2,y*self.res + self.res/2, 1.3*self.res,x*self.res + self.res/2, y*self.res + self.res/2)
        gradient.setColorAt(0, col)
        gradient.setColorAt(1, col1)
        brush = QtGui.QBrush(gradient)
        self.Scene.addRect(x*self.res, y*self.res, self.res, self.res, pen , brush )
    
    def DrawCercle(self, x, y):
        pen = QtGui.QPen()
        pen.setWidth(2)
        col = QtGui.QColor(150,150,150)
        col1= QtGui.QColor(40,40,40)
        gradient = QtGui.QRadialGradient(x*self.res, y*self.res, 1.3*self.res,x*self.res + self.res/2, y*self.res + self.res/2)
        gradient.setColorAt(0, col)
        gradient.setColorAt(1, col1)
        brush = QtGui.QBrush(gradient)

        self.Scene.addEllipse( self.res*x + self.res/4, self.res * y + self.res/4, self.res/2, self.res/2, pen , brush)
        
