import os
os.chdir('C:\\Users\\teovi\\Documents\\IMI\\Projet MoPSi\\')


from PyQt4 import QtGui, QtCore
# import sys
# import random
# import numpy as np
from code.Classes import *

from code.Pieces import *

class PieceCreationWindow():        
    def __init__(self, main, n, m):
        self.res= 700/n
        self.main = main        
        self.n=n
        self.m=m
        self.compt= self.n*self.m-1
        self.clics=0
        self.SetNewCol()
        self.pieces=[]
        self.mat=[]
        
        self.window = QtGui.QWidget()
        self.Scene = QtGui.QGraphicsScene()
        self.DrawGrid()
        
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(40)
        
        self.Screen = QtGui.QGraphicsView(self.Scene)
        self.Screen.setGeometry(QtCore.QRect(0, 0, m*self.res, n*self.res))
        self.Screen.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.Screen.mousePressEvent = self.getPos

        self.lowerPanel = QtGui.QHBoxLayout()
        self.buttonClear = QtGui.QPushButton('Clear')
        self.buttonAddpiece = QtGui.QPushButton('Add Piece')
        self.buttonOk = QtGui.QPushButton('Ok')
        
        self.upperPanel = QtGui.QHBoxLayout()
        self.label_c = QtGui.QLabel("Number of slots left :")
        self.label_c.setFont(font)
        self.label_c.setAlignment(QtCore.Qt.AlignCenter)
        self.buttonReset = QtGui.QPushButton('Reset')
   
        self.CompteurLayout = QtGui.QHBoxLayout()
        self.Compteur = QtGui.QLCDNumber()
        self.Compteur.display(self.compt)
        self.Compteur.setMinimumHeight(50)
        
        self.upperPanel.addWidget(self.label_c)
        self.upperPanel.addWidget(self.Compteur)
        self.upperPanel.addWidget(self.buttonReset)
        self.Compteur.setDigitCount(2)    
        self.Compteur.setDigitCount(8)
        self.Compteur.setMaximumHeight(50)
        
        self.label = QtGui.QLabel("Select bloc position :")
        self.label.setFont(font)
        self.lowerPanel.addWidget(self.buttonClear)
        self.lowerPanel.addWidget(self.buttonAddpiece)
        self.lowerPanel.addWidget(self.buttonOk)

        self.mainPanel = QtGui.QVBoxLayout()
        self.mainPanel.addLayout(self.upperPanel)
        self.mainPanel.addWidget(self.label)
        self.mainPanel.addWidget(self.Screen)
        self.mainPanel.addLayout(self.lowerPanel)

        self.window.setLayout(self.mainPanel)
        self.window.setWindowTitle('Place Creation')
        self.window.show()

        self.buttonClear.clicked.connect(self.Clear)
        self.buttonOk.clicked.connect(self.Ok)
        self.buttonAddpiece.clicked.connect(self.AddPiece)
        self.buttonReset.clicked.connect(self.Reset)
        
        self.Compteur.setEnabled(True)
        self.buttonOk.setEnabled(False)
        self.buttonAddpiece.setEnabled(False)
        self.buttonClear.setEnabled(False)
        
        
    def RefreshCompt(self, int):
        self.Compteur.display(int)
    
    
    def Ok(self):
        self.Update()
        self.main.pieces = self.pieces
        self.ui.InterfButton.setEnabled(True)
        self.window.close()
        
        
    def Clear(self):
        self.DrawGrid()
        self.clics =0
        self.mat=[]
        self.buttonClear.setEnabled(False)
        self.buttonAddpiece.setEnabled(False)
        
        
    def DrawGrid(self):
        col= QtGui.QColor(255,255,255)
        pen = QtGui.QPen()
        pen.setWidth(2)
        brush = QtGui.QBrush(col)
        n,m= self.n,self.m
        self.Scene.addRect( 0, 0, m*self.res, n*self.res, pen , brush )
        pen.setStyle(4)
        for i in range(1,self.main.n):
            self.Scene.addLine(0, i*self.res, m*self.res, i*self.res, pen)
        for j in range(1,self.main.m):
            self.Scene.addLine(j*self.res,0, j*self.res, n*self.res, pen)
    
    
    def SetNewCol(self):
        a = random.randint(50,255)
        b = random.randint(50,255)
        c = random.randint(50,255)
        self.col = QtGui.QColor(a,b,c)
        
        
    def getPos(self, event):
        x = int(event.pos().x()//self.res)
        y = int(event.pos().y()//self.res)
        
        if [x,y] not in self.mat:
            self.DrawRect(x, y, self.col)
            self.mat.append([x,y])
            self.clics +=1

        self.buttonAddpiece.setEnabled(True)
        self.buttonClear.setEnabled(True)
    
    
    def Update(self):
        self.compt -= self.clics
        self.clics =0
        self.RefreshCompt(self.compt)
        self.SetNewCol()
        self.DrawGrid()
        self.mat=[]
        self.buttonClear.setEnabled(False)
        
        if self.compt==0:
            self.buttonOk.setEnabled(True)
            self.buttonAddpiece.setEnabled(False)
    
    
    def Reset(self):
        self.Clear()
        self.compt=self.n*self.m-1
        self.RefreshCompt(self.compt)
        self.pieces=[]
        self.buttonAddpiece.setEnabled(False)
    
    
    def connexe(self,mat):
        if len(mat)==1:
            return True
        for i in mat:
            a=[i[0]+1,i[1]]
            b=[i[0]-1,i[1]]
            c=[i[0],i[1]+1]
            d=[i[0],i[1]-1]
            if(a in mat or b in mat or c in mat or d in mat):
                pass
            else:
                return False
        return True

        
    def MatToPiece(self):
        minx = self.n
        miny = self.m
        maxx= 0
        maxy= 0
    
        for i in range(len(self.mat)):
            if self.mat[i][0] > maxx:
                maxx = self.mat[i][0]
            if self.mat[i][1] > maxy:
                maxy = self.mat[i][1]                
            if self.mat[i][0] <= minx:
                minx = self.mat[i][0]            
            if self.mat[i][1] <= miny:
                miny = self.mat[i][1]
        piece = np.zeros((maxy-miny+1,maxx-minx+1))
        
        for i in range(minx,maxx+1):
            for j in range(miny,maxy+1):
                if [i,j] in self.mat:
                    piece[j-miny,i-minx]+=1
        
        P = piece_default()
        P.mat= piece
        P.color = self.col
        self.pieces.append(P)
        
        
    def AddPiece(self):
        if (self.compt- self.clics)<0:
            self.Error(1)
            self.Clear()
        else:
            if self.connexe(self.mat):
                self.MatToPiece()
                self.Update()
            else: 
                self.Error(0)
                self.Clear()
        self.buttonAddpiece.setEnabled(False)
        self.buttonClear.setEnabled(False)
        
        
    def DrawRect(self,x ,y, col):
        pen = QtGui.QPen()
        col1= QtGui.QColor(40,40,40)
        gradient = QtGui.QRadialGradient(x*self.res + self.res/2,y*self.res + self.res/2, 1.3*self.res,x*self.res + self.res/2, y*self.res + self.res/2)
        gradient.setColorAt(0, col)
        gradient.setColorAt(1, col1)
        brush = QtGui.QBrush(gradient)
        self.Scene.addRect(x*self.res, y*self.res, self.res, self.res, pen , brush )


    def Error(self, type):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Critical)
        
        if type==0:
            text = "Please draw a piece of a possible shape"
        if type==1:
            text = "Not enough space left for this piece"
    
        msg.setText(text)
        msg.setWindowTitle("Error")
        msg.exec_()
