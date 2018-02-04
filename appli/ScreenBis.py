from PyQt4 import QtGui, QtCore
import sys
import os
import numpy as np


class BlocPlacementWindow():
    def __init__(self, main):
        self.main = main
        #Display resolution
        self.res = 100     
        #Size
        self.n = main.n
        self.m = main.m
        
        #Window & Screen
        self.window = QtGui.QWidget()
        self.Scene = QtGui.QGraphicsScene()
        self.DrawGrid()
        
        self.Screen = QtGui.QGraphicsView(self.Scene)
        self.Screen.setGeometry(QtCore.QRect(0, 0, self.main.m*self.res, self.main.n*self.res))
        self.Screen.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.Screen.mousePself.ressEvent = self.getPos

        #Bottom of screen buttons
        self.lowerPanel = QtGui.QHBoxLayout()
        self.buttonOk = QtGui.QPushButton('Ok')
        self.buttonClear = QtGui.QPushButton('Clear')
        
        #Label
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(40)
        self.label = QtGui.QLabel("Select bloc position :")
        self.label.setFont(font)
        self.lowerPanel.addWidget(self.buttonOk)
        self.lowerPanel.addWidget(self.buttonClear)
        
        #Display
        self.mainPanel = QtGui.QVBoxLayout()
        self.mainPanel.addWidget(self.label)
        self.mainPanel.addWidget(self.Screen)
        self.mainPanel.addLayout(self.lowerPanel)
        self.window.setLayout(self.mainPanel)
        self.window.setWindowTitle('Bloc placement')
        self.window.show()
        
        #Binding
        self.buttonClear.clicked.connect(self.Clear)
        self.buttonOk.clicked.connect(self.Ok)
    
    
    def Ok(self):       #To apply changes
        self.Update()
        self.window.close()
        
        
    def Clear(self):        #To clear the grid
        self.DrawGrid()
        self.main.bloc.x=3
        self.main.bloc.y=3
        
        
    def DrawGrid(self):     #Draws the grid
        col= QtGui.QColor(255,255,255)
        pen = QtGui.QPen()
        pen.setWidth(3)
        brush = QtGui.QBrush(col)
        n,m= self.n,self.m
        self.Scene.addRect( 0, 0, self.main.m*self.res, self.main.n*self.res, pen , brush )
        pen.setStyle(5)
        for i in range(1,self.main.n):
            self.Scene.addLine(0, i*self.res, m*self.res, i*self.res, pen)
        for j in range(1,self.main.m):
            self.Scene.addLine(j*self.res,0, j*self.res, n*self.res, pen)
    
    
    def getPos(self , event):       #Acquires the square clicked
        self.DrawGrid()
        col= QtGui.QColor(255,0,0)
        pen = QtGui.QPen()
        brush = QtGui.QBrush(col)
        
        x = event.pos().x()//self.res
        y = event.pos().y()//self.res
        self.DrawCercle(x, y)
        self.main.bloc.x=x
        self.main.bloc.y=y
    
    def Update(self):       #Applies changes
        self.main.controller.Clear()
        self.main.controller.AfficheBloc(self.main.bloc)
        self.main.ApplySizeButton.setEnabled(False)
        self.main.self.resetButton.setEnabled(True)
        #bloc placed
        self.main.controller.blocPlaced = True
        self.main.controlller.UpdateState()
        
    def DrawCercle(self, x, y):     #Drawing the bloc
        pen = QtGui.QPen()
        pen.setWidth(2)
        col = QtGui.QColor(150,150,150)
        col1= QtGui.QColor(40,40,40)
        gradient = QtGui.QRadialGradient(x*self.res, y*self.res, 1.3*self.res,x*self.res + self.res/2, y*self.res + self.res/2)
        gradient.setColorAt(0, col)
        gradient.setColorAt(1, col1)
        brush = QtGui.QBrush(gradient)

        self.Scene.addEllipse( self.res*x + self.res/4, self.res * y + self.res/4, self.res/2, self.res/2, pen , brush)
        
        
        
