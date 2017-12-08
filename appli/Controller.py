import os
os.chdir('C:\\Users\\teovi\\Documents\\IMI\\Projet MoPSi\\')

from appli.Screen import *
from appli.ScreenBis import *
from appli.ScreenTer import *

# from PyQt4 import QtCore, QtGui
  
class Controller:
    def __init__(self, ui, grid, bloc, pieces, n, m):
        self.ui = ui
        self.continu=True	
        
        self.grid=grid
        self.bloc=bloc
        self.pieces=pieces
        self.method= transform1

        self.T=100
        
        self.compteur=0
        

    def bind(self):
        self.ui.InitButton.clicked.connect(self.Init)
        self.ui.ResetButton.clicked.connect(self.Reset)
        self.ui.SolveButton.clicked.connect(self.Solve)
        self.ui.PauseButton.clicked.connect(self.Pause)
        self.ui.PlaceBlocButton.clicked.connect(self.PlaceBloc)
        self.ui.ApplySizeButton.clicked.connect(self.SetSize)
        self.ui.ApplyPeriodButton.clicked.connect(self.SetPeriod)
        self.ui.ApplyMethodButton.clicked.connect(self.SetMethod)
        # self.ui.ApplyMethodButton.clicked.connect(self.t)
        self.ui.InterfButton.clicked.connect(self.CreatePieces)
    
    def AffichePiece(self, piece):
        n_p,m_p=piece.mat.shape
        for i in range(n_p):
            for j in range(m_p):
                if piece.mat[i,j]==1:
                    self.ui.DrawRect(piece.x + i,piece.y + j,  piece.color)
    
    
    def AfficheBloc(self, bloc):
        self.ui.DrawCercle(bloc.x,bloc.y)
        

    def Clear(self):
        self.ui.Scene.clear()
        self.ui.SolveButton.setEnabled(False)
        self.ui.ResetButton.setEnabled(False)
        self.ui.DrawGrid()
    
    
    def Reset(self):
        self.Clear()
        self.grid.clear()
        self.ui.ResetButton.setEnabled(False)
        self.ui.ApplySizeButton.setEnabled(True)
        self.ui.PlaceBlocButton.setEnabled(True)
        self.ui.ApplySizeButton.setEnabled(True)
        self.compteur=0
        self.ui.CompteurLCD.display(0)
    
    
    def Refresh(self, pieces, bloc= False):
        self.Clear()
        if not bloc:
            pass
        else:
            self.AfficheBloc(bloc)
        for piece in pieces:
            self.AffichePiece(piece)
    
    
    def Init(self):
        self.compteur=0
        self.Clear()
        self.AfficheBloc(self.bloc)
        self.grid.clear()
        
        config_init(self.grid ,self.pieces, self.bloc)
        
        for piece in self.pieces:
            self.AffichePiece(piece)
        
        self.ui.SolveButton.setEnabled(True)
        self.ui.ResetButton.setEnabled(True)
        self.ui.PlaceBlocButton.setEnabled(True)
        self.ui.ApplySizeButton.setEnabled(False)
        self.ui.PlaceBlocButton.setEnabled(False)
        self.ui.CompteurLCD.display(0)
        
        
    def Pause(self):
        self.continu= False
        self.ui.PauseButton.setEnabled(False)
        self.ui.InitButton.setEnabled(True)
        self.ui.SolveButton.setEnabled(True)
    
    
    def Solve(self):
        self.continu = True
        self.ui.SolveButton.setEnabled(False)
        self.ui.ApplyPeriodButton.setEnabled(False)
        self.ui.ApplyMethodButton.setEnabled(False)
        self.ui.InitButton.setEnabled(False)
        self.ui.PauseButton.setEnabled(True)
        self.ui.PlaceBlocButton.setEnabled(False)
        
        Pot=self.grid.V();
        
        while (Pot > 0 and self.continu):
            self.ui.CompteurLCD.display(self.compteur)
            self.compteur+=1
            
            Pot = self.method(self.pieces,Pot, self.grid, self.bloc, self.compteur)
            
            if (self.compteur%self.T==0): 
                # time.sleep(0.1)
                self.Refresh(self.pieces, self.bloc)
                self.ui.app.processEvents()

                self.ui.Screen.resetMatrix()
                self.ui.Screen.resetTransform()
                self.ui.Screen.resetCachedContent()
         
        self.Refresh(self.pieces, self.bloc)
        self.ui.CompteurLCD.display(self.compteur)
        
        if Pot==0:
            self.ui.PauseButton.setEnabled(False)
            self.ui.InitButton.setEnabled(True)
            self.ui.PlaceBlocButton.setEnabled(True)
            self.ui.Success(self.ui.n,self.ui.m,self.compteur)
        else: 
            self.Pause()

        
        self.ui.ResetButton.setEnabled(True)
        self.ui.ApplyPeriodButton.setEnabled(True)
        self.ui.ApplyMethodButton.setEnabled(True)


    def PlaceBloc(self):
        BlocPlacementWindow(self.ui, self.ui.n, self.ui.m)


    def SetPeriod(self):
        self.T=int(self.ui.RefreshPeriod.currentText())

    
    def SetSize(self):
        self.ui.n=int(self.ui.PuzzleSize.currentText()[0])
        self.ui.m=int(self.ui.PuzzleSize.currentText()[-1])
        self.pieces= pieces_default(self.ui.n, self.ui.m)
        self.grid = grid(self.ui.n,self.ui.m)
        self.ui.res = int(900/max(self.ui.n, self.ui.m))
        self.Reset()
        
    def CreatePieces(self):
        PieceCreationWindow(self.ui, self.ui.n, self.ui.m)
        
        ##
        
    def SetMethod(self):
        if self.ui.SolveMethod.currentText()=="1":
            self.method=transform1
        if self.ui.SolveMethod.currentText()=="2":
            self.method=transform2

    
    def Test(self):

        # print(self.grid.V())
        # 
        # 
        # print(self.grid.V()+self.pieces[0].varV_permut(self.grid, self.pieces[1]))
        # self.pieces[0].permut(self.grid, self.pieces[1])
        # self.Refresh(self.pieces, self.bloc)
        # self.grid.refresh(self.pieces, self.bloc)
        # 
        # 
        # # print(np.transpose(self.grid.mat))
        # print('potentiel', self.grid.V())
        # print(' ')
        # 
        
        self.pieces[0].rotate(self.grid)
        self.Refresh(self.pieces, self.bloc)


    
        
        




