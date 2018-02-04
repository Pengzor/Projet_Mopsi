from PyQt4 import QtGui, QtCore
import numpy as np

class PiecePlacementWindow():        
    def __init__(self, main):
        self.main = main  
        #Size
        self.n = main.n
        self.m = main.m
        n=self.n
        m=self.m
        #Resolutions
        self.res= 500/n
        self.resp=250/n

        #Pieces
        self.pieces=np.copy(main.pieces)
        #Placed pieces
        self.occupied=[[main.bloc.x,main.bloc.y]]
        self.placedpieces=[]
        #Window
        self.window = QtGui.QWidget()

        
        #Font
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(40)
        
        #Spacers
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        spacerItem3 = QtGui.QSpacerItem(40, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        
        #Display Screen
        self.Scene = QtGui.QGraphicsScene()
        self.DrawGrid()
        self.Screen = QtGui.QGraphicsView(self.Scene)
        self.Screen.setGeometry(QtCore.QRect(0, 0, m*self.res, n*self.res))
        self.Screen.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        
        #Preview Screen
        self.Scene2 = QtGui.QGraphicsScene()
        self.Preview =  QtGui.QGraphicsView(self.Scene2)
        self.Preview.setGeometry(QtCore.QRect(0, 0, m*self.resp, n*self.resp))
        self.Preview.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.Preview.setMaximumHeight(m*self.resp)
        self.Preview.setMaximumWidth(n*self.resp)
        self.Preview.setMinimumHeight(m*self.resp)
        self.Preview.setMinimumWidth(n*self.resp)
        
        #Bottom of screen buttons
        self.lowerPanel = QtGui.QHBoxLayout()
        self.buttonReset = QtGui.QPushButton('Reset')
        self.buttonAddpiece = QtGui.QPushButton('Confirm Placement')
        self.buttonOk = QtGui.QPushButton('Ok')
        self.lowerPanel.addWidget(self.buttonReset)
        self.lowerPanel.addWidget(self.buttonAddpiece)
        self.lowerPanel.addWidget(self.buttonOk)
        
        #Labels
        self.label = QtGui.QLabel("Place top left corner of the piece:")
        self.label.setFont(font)
        self.label2 = QtGui.QLabel("Select piece :")
        self.label2.setFont(font)
        
        #Display pannel
        self.leftPanel = QtGui.QVBoxLayout()
        self.leftPanel.addWidget(self.Screen)
        
        #Piece list
        self.PiecePanel=QtGui.QHBoxLayout()
        self.PieceList = QtGui.QComboBox()
        self.PieceList.setMinimumHeight(43)
        i = 0
        for piece in self.main.pieces:
            i+=1;
            self.PieceList.addItem(str(i))
        
        #Piece selection & rotation panel
        self.SelectPieceButton = QtGui.QPushButton("Apply")
        self.RotateButton = QtGui.QPushButton("Rotate")
        self.PiecePanel.addWidget(self.PieceList)
        self.PiecePanel.addWidget(self.SelectPieceButton)
        
        #Preview pannel
        self.rightPanel = QtGui.QVBoxLayout()
        self.rightPanel.addItem(spacerItem3)
        self.rightPanel.addWidget(self.label2)
        self.rightPanel.addLayout(self.PiecePanel)
        self.rightPanel.addWidget(self.Preview)
        self.rightPanel.addWidget(self.RotateButton)
        self.rightPanel.addItem(spacerItem3)
        
        #Display both screens
        self.midPanel=QtGui.QHBoxLayout()
        self.midPanel.addLayout(self.leftPanel)
        self.midPanel.addItem(spacerItem2)
        self.midPanel.addLayout(self.rightPanel)
        
        #Overall layout
        self.mainPanel = QtGui.QVBoxLayout()
        self.mainPanel.addWidget(self.label)
        self.mainPanel.addLayout(self.midPanel)
        self.mainPanel.addItem(spacerItem)
        self.mainPanel.addLayout(self.lowerPanel)
        self.window.setLayout(self.mainPanel)
        self.window.setWindowTitle('Piece Placement')
        self.window.show()

        # Binds
        self.Screen.mousePressEvent = self.getPos
        self.SelectPieceButton.clicked.connect(self.PreviewPiece)
        self.RotateButton.clicked.connect(self.RotatePiece)
        self.buttonReset.clicked.connect(self.Reset)
        self.buttonAddpiece.clicked.connect(self.ConfirmPlacement)
        self.buttonOk.clicked.connect(self.Ok)
        
        #Buttons management
        self.Screen.setEnabled(False)
        self.RotateButton.setEnabled(False)
        self.buttonAddpiece.setEnabled(False)
        self.PieceList.setEnabled(True)
        self.index = int(self.PieceList.currentText())-1
        self.DrawBloc(main.bloc.x,main.bloc.y)
        
    
    def PreviewPiece(self):     #Preview a piece
        if len(self.placedpieces)<len(self.pieces):
            self.index = int(self.PieceList.currentText())-1
            piece=self.pieces[self.index]
            self.AffichePiecePreview(piece)
        
        self.Screen.setEnabled(True)
        self.RotateButton.setEnabled(True)
        self.currentIndex = self.PieceList.currentIndex()
    
    
    def AffichePiecePreview(self, piece):       #To display the piece on the preview screen
        self.Scene2.clear()
        n_p,m_p=piece.mat.shape
        for i in range(n_p):
            for j in range(m_p):
                if piece.mat[i,j]==1:
                    self.DrawRect(i, j,  piece.color, self.Scene2, self.resp)
        pen = QtGui.QPen()
        pen.setWidth(1)
        col = QtGui.QColor(255,0,0)
        brush = QtGui.QBrush(col)
        size = self.resp/8
        self.Scene2.addEllipse( self.resp/2 - size/2, self.resp/2-size/2, size, size, pen , brush)
        self.buttonAddpiece.setEnabled(False)


    def RotatePiece(self):      #Rotate preview
        self.pieces[self.index].rotate_()
        self.AffichePiecePreview(self.pieces[self.index])
        self.buttonAddpiece.setEnabled(False)
        
        
    def DrawGrid(self):     #Draw display grid
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
            
        
    def getPos(self, event):        #Acquire clicked case
        x = int(event.pos().x()//self.res)
        y = int(event.pos().y()//self.res)
        self.Placepiece(x,y)
        
        
    def Placepiece(self,x,y):          # Place the piece here
        piece =  self.pieces[self.index]
        if self.Placable(piece, x, y):
            self.Refresh()
            piece.x = x
            piece.y = y
            self.AffichePiece(piece)
            n,m= piece.mat.shape
            self.buttonAddpiece.setEnabled(True)

            
    def Placable(self,piece, x, y):      #Make sure you can put the piece here
        G= self.main.grid
        n,m= piece.mat.shape
        for i in range(n):
            for j in range(m):
                if piece.mat[i,j] ==1:
                    if [x+i,y+j] in self.occupied :
                        self.Error(0)
                        return False
        if n+x>self.n or m+y>self.m:
            self.Error(1)
            return False
        return True
    
    
    def ConfirmPlacement(self):     #Confirm the choice of position
        piece= self.pieces[self.index]  
        x, y=piece.x, piece.y
        n,m= piece.mat.shape
        for i in range(n):
            for j in range(m):
                if piece.mat[i,j] ==1:
                    self.occupied.append([x+i,y+j])
        self.placedpieces.append(piece)
        self.PieceList.removeItem(self.currentIndex)
        self.PreviewPiece()
        
        #Buttons management
        self.PieceList.setEnabled(True)
        self.buttonAddpiece.setEnabled(False)
        if len(self.placedpieces)==len(self.pieces):
            self.buttonAddpiece.setEnabled(False)
            self.Screen.setEnabled(False)
            self.RotateButton.setEnabled(False)
            self.SelectPieceButton.setEnabled(False)
            
    
    def Reset(self):        #Reset
        self.placedpieces=[]
        self.occupied=[[self.main.bloc.x,self.main.bloc.y]]
        self.Refresh()
        self.PieceList.clear()
        i = 0
        for piece in self.main.pieces:
            i+=1;
            self.PieceList.addItem(str(i))
        self.Scene2.clear()
        
        #Buttons management
        self.Screen.setEnabled(False)
        self.RotateButton.setEnabled(False)
        self.buttonAddpiece.setEnabled(False)
        self.SelectPieceButton.setEnabled(True)

    def Refresh(self):      #Display changes
        self.DrawGrid()
        for piece in self.placedpieces:
            self.AffichePiece(piece)
        self.DrawBloc(self.main.bloc.x, self.main.bloc.y)
    
    
    def AffichePiece(self, piece):      #Display a piece
        n_p,m_p=piece.mat.shape
        for i in range(n_p):
            for j in range(m_p):
                if piece.mat[i,j]==1:
                    self.DrawRect(piece.x + i,piece.y + j,  piece.color, self.Scene, self.res)
      
        
    def DrawRect(self,x ,y, col, scene, res):       #Draw a rectangle
        pen = QtGui.QPen()
        col1= QtGui.QColor(100,100,100)
        gradient = QtGui.QRadialGradient(x*res + res/2,y*res + res/2, 1.3*res,x*res + res/2, y*res + res/2)
        gradient.setColorAt(0, col)
        gradient.setColorAt(1, col1)
        brush = QtGui.QBrush(gradient)
        scene.addRect(x*res, y*res, res, res, pen , brush )


    def Error(self, type):      #Error message
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Critical)
        
        if type==0:
            text = "There is already a piece"
        if type==1:
            text = "Piece out of bounds"
    
        msg.setText(text)
        msg.setWindowTitle("Cannot place piece here")
        msg.exec_()
        
        
    def Ok(self):       #Apply changes
        self.main.fixedpieces= self.placedpieces
        for piece in self.placedpieces:
            if piece in self.main.pieces:
                self.main.pieces.remove(piece)
        self.main.controller.AffichePlaced()
        self.main.controller.piecesAlreadyPlaced = True
        self.main.controller.UpdateState()
        self.window.close()
        
        
    def DrawBloc(self, x, y):       #Draws the bloc
        pen = QtGui.QPen()
        pen.setWidth(2)
        col = QtGui.QColor(150,150,150)
        col1= QtGui.QColor(40,40,40)
        gradient = QtGui.QRadialGradient(x*self.res, y*self.res, 1.3*self.res,x*self.res + self.res/2, y*self.res + self.res/2)
        gradient.setColorAt(0, col)
        gradient.setColorAt(1, col1)
        brush = QtGui.QBrush(gradient)
        self.Scene.addEllipse( self.res*x + self.res/4, self.res * y + self.res/4, self.res/2, self.res/2, pen , brush)