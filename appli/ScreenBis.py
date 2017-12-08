from PyQt4 import QtGui, QtCore
import sys

res=100

class BlocPlacementWindow():
    def __init__(self, main,n, m):
        self.main = main        
        self.n=n
        self.m=m
        
        self.window = QtGui.QWidget()
        
        self.Scene = QtGui.QGraphicsScene()
        self.DrawGrid()
        
        self.Screen = QtGui.QGraphicsView(self.Scene)
        self.Screen.setGeometry(QtCore.QRect(0, 0, self.main.m*res, self.main.n*res))
        self.Screen.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.Screen.mousePressEvent = self.getPos

        self.lowerPanel = QtGui.QHBoxLayout()
        self.buttonOk = QtGui.QPushButton('Ok')
        self.buttonClear = QtGui.QPushButton('Clear')
        
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(40)
        self.label = QtGui.QLabel("Select bloc position :")
        self.label.setFont(font)
        self.lowerPanel.addWidget(self.buttonOk)
        self.lowerPanel.addWidget(self.buttonClear)

        self.mainPanel = QtGui.QVBoxLayout()
        self.mainPanel.addWidget(self.label)
        self.mainPanel.addWidget(self.Screen)
        self.mainPanel.addLayout(self.lowerPanel)

        self.window.setLayout(self.mainPanel)
        self.window.setWindowTitle('Bloc placement')
        self.window.show()

        self.buttonClear.clicked.connect(self.Clear)
        self.buttonOk.clicked.connect(self.Ok)
    
    def Ok(self):
        self.Update()
        self.window.close()
        
        
    def Clear(self):
        self.DrawGrid()
        self.main.bloc.x=3
        self.main.bloc.y=3
        
        
    def DrawGrid(self):
        col= QtGui.QColor(255,255,255)
        pen = QtGui.QPen()
        pen.setWidth(3)
        brush = QtGui.QBrush(col)
        n,m= self.n,self.m
        self.Scene.addRect( 0, 0, self.main.m*res, self.main.n*res, pen , brush )
        pen.setStyle(5)
        for i in range(1,self.main.n):
            self.Scene.addLine(0, i*res, m*res, i*res, pen)
        for j in range(1,self.main.m):
            self.Scene.addLine(j*res,0, j*res, n*res, pen)
    
    
    def getPos(self , event):
        self.DrawGrid()
        col= QtGui.QColor(255,0,0)
        pen = QtGui.QPen()
        brush = QtGui.QBrush(col)
        
        x = event.pos().x()//res
        y = event.pos().y()//res
        self.DrawCercle(x, y)
        self.main.bloc.x=x
        self.main.bloc.y=y
    
    def Update(self):
        self.main.controller.Clear()
        self.main.controller.AfficheBloc(self.main.bloc)
        self.main.ApplySizeButton.setEnabled(False)
        self.main.ResetButton.setEnabled(True)
        
    def DrawCercle(self, x, y):
        pen = QtGui.QPen()
        pen.setWidth(2)
        col = QtGui.QColor(150,150,150)
        col1= QtGui.QColor(40,40,40)
        gradient = QtGui.QRadialGradient(x*res, y*res, 1.3*res,x*res + res/2, y*res + res/2)
        gradient.setColorAt(0, col)
        gradient.setColorAt(1, col1)
        brush = QtGui.QBrush(gradient)

        self.Scene.addEllipse( res*x + res/4, res * y + res/4, res/2, res/2, pen , brush)
        
        
        
