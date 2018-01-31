import os
os.chdir('D:\\Documents\\Ponts ParisTech\\Projet MOPSI\\Projet2')

from appli.Screen import *
from appli.ScreenBis import *
from appli.ScreenTer import *
from appli.ScreenQuad import *

# from PyQt4 import QtCore, QtGui
  
class Controller:
    def __init__(self, ui):
        self.ui = ui
        self.continu=True	
        
        self.grid=self.ui.grid
        self.method= transform1

        self.T=100
        
        self.compteur=0
        
        #variables of state
        self.blocPlaced = False
        self.puzzleInitialized = False
        

    def bind(self):
        self.ui.InitButton.clicked.connect(self.Init)
        self.ui.ResetButton.clicked.connect(self.Reset)
        self.ui.SolveButton.clicked.connect(self.Solve)
        self.ui.PauseButton.clicked.connect(self.Pause)
        self.ui.PlaceBlocButton.clicked.connect(self.PlaceBloc)
        self.ui.ApplySizeButton.clicked.connect(self.SetSize)
        self.ui.ApplyPeriodButton.clicked.connect(self.SetPeriod)
        self.ui.ApplyMethodButton.clicked.connect(self.SetMethod)
        self.ui.ApplyModeButton.clicked.connect(self.SetUse)
        # self.ui.ApplyMethodButton.clicked.connect(self.t)
        self.SetUse()
    
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
        self.ui.ApplyPeriodButton.setEnabled(True)
        self.ui.ApplyMethodButton.setEnabled(True)
        self.ui.PlaceBlocButton.setEnabled(True)
        self.ui.ApplyModeButton.setEnabled(True)

        self.compteur=0
        self.ui.CompteurLCD.display(0)
        
        self.ui.pieces= self.ui.pieces+self.ui.fixedpieces
        self.ui.fixedpieces=[]
        
        #state variables
        self.blocPlaced = False
        self.puzzleInitialized = False
        self.UpdateState()
        
        self.ui.app.processEvents()
    
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
        self.AfficheBloc(self.ui.bloc)
        self.grid.clear()
        
        config_init(self.grid ,self.ui.pieces, self.ui.fixedpieces, self.ui.bloc)
        
        for piece in self.ui.pieces:
            self.AffichePiece(piece)
        for piece in self.ui.fixedpieces:
            self.AffichePiece(piece)
        
        self.ui.SolveButton.setEnabled(True)
        self.ui.ResetButton.setEnabled(True)
        self.ui.PlaceBlocButton.setEnabled(True)
        self.ui.ApplySizeButton.setEnabled(False)
        self.ui.PlaceBlocButton.setEnabled(False)
        self.ui.ApplyModeButton.setEnabled(False)
        self.ui.CompteurLCD.display(0)
        
        self.puzzleInitialized = True
        self.UpdateState()

    def Pause(self):
        self.continu= False
        self.ui.PauseButton.setEnabled(False)
        self.ui.InitButton.setEnabled(True)
        self.ui.SolveButton.setEnabled(True)
        print('Pause')
    
    
    def Solve(self):
        self.continu = True
        self.ui.SolveButton.setEnabled(False)
        self.ui.ApplyPeriodButton.setEnabled(False)
        self.ui.ApplyMethodButton.setEnabled(False)
        self.ui.InitButton.setEnabled(False)
        self.ui.PauseButton.setEnabled(True)
        self.ui.PlaceBlocButton.setEnabled(False)
        
        #---Recuit simule---
        if (self.method==transform1 or self.method==transform2):
            Pot=self.grid.V();
        
            while (Pot > 0 and self.continu):
                self.ui.CompteurLCD.display(self.compteur)
                self.compteur+=1
                
                Pot = self.method(self.ui.pieces, Pot, self.grid, self.ui.bloc, self.compteur, self.ui.fixedpieces)
            
                if (self.compteur%self.T==0): 
                    # time.sleep(0.1)
                    self.Refresh(self.ui.pieces+self.ui.fixedpieces, self.ui.bloc)
                    self.ui.app.processEvents()

                    self.ui.Screen.resetMatrix()
                    self.ui.Screen.resetTransform()
                    self.ui.Screen.resetCachedContent()
         
            self.Refresh(self.ui.pieces+self.ui.fixedpieces, self.ui.bloc)
            self.ui.CompteurLCD.display(self.compteur)
            
            #if success
            if Pot==0:
                self.ui.PauseButton.setEnabled(False)
                self.ui.InitButton.setEnabled(True)
                self.ui.PlaceBlocButton.setEnabled(True)
                self.ui.ApplyModeButton.setEnabled(True)
                self.ui.Success(self.ui.n,self.ui.m,self.compteur)
            else: 
                self.Pause()
        
            self.ui.ResetButton.setEnabled(True)
            self.ui.ApplyPeriodButton.setEnabled(True)
            self.ui.ApplyMethodButton.setEnabled(True)
        
        #---Algorithme exhaustif---
        elif (self.method==transformExhaustive):
            
            #momentarily disable buttons
            self.ui.DisableAll()
            
            #solutions to display
            #--Rq : always 1 single fixed square
            numFixedPieces = []
            for i in range(0, len(self.ui.fixedpieces)):
                numFixedPieces.append(self.ui.fixedpieces[i].y * self.grid.n + self.ui.fixedpieces[i].x + 1)
            numFixedPieces.append(self.ui.bloc.y * self.grid.n + self.ui.bloc.x + 1)
            setSolutions = self.method(self.grid.n, numFixedPieces, self.ui.pieces)
            
            #if success
            if len(setSolutions) > 0:
                self.ui.SuccessExhaustive(len(setSolutions), self.ui.n, self.ui.m)
                #display all solutions
                for i in range(0, len(setSolutions)):
                    self.compteur += 1
                    self.Refresh(setSolutions[i]+self.ui.fixedpieces, self.ui.bloc)
                    self.ui.CompteurLCD.display(self.compteur)
                    self.ui.app.processEvents()
                    self.ui.Screen.resetMatrix()
                    self.ui.Screen.resetTransform()
                    self.ui.Screen.resetCachedContent()
                    time.sleep(1)
                #re-enable buttons
                self.ui.ReEnableAll()
            else: 
                self.Reset()
                self.ui.FailureExhaustive()

    def PlaceBloc(self):
        BlocPlacementWindow(self)
        self.Reset()
        #self.UpdateState()   -> in the 'BlocPlacementWindow' function


    def SetPeriod(self):
        self.T=int(self.ui.RefreshPeriod.currentText())

    
    def SetSize(self):
        self.ui.n=int(self.ui.PuzzleSize.currentText()[0])
        self.ui.m=int(self.ui.PuzzleSize.currentText()[-1])
        self.ui.pieces= pieces_default(self.ui.n, self.ui.m)
        self.ui.bloc=bloc_default(self.ui.n, self.ui.m)
        self.grid = grid(self.ui.n,self.ui.m)
        self.ui.res = int(900/max(self.ui.n, self.ui.m))
        self.Reset()
        
    def CreatePieces(self):
        PieceCreationWindow(self.ui, self.ui.n, self.ui.m)
    
    def PlacePieces(self):
        self.Reset()
        PiecePlacementWindow(self.ui, self.ui.n, self.ui.m)
        
        
        
        ##
        
    def SetMethod(self):
        if self.ui.SolveMethod.currentText()=="1":
            self.method=transform1
            self.ui.ApplyPeriodButton.setEnabled(True)
        elif self.ui.SolveMethod.currentText()=="2":
            self.method=transform2
            self.ui.ApplyPeriodButton.setEnabled(True)
        elif self.ui.SolveMethod.currentText()=="Exhaustive":
            self.method=transformExhaustive
            self.ui.ApplyPeriodButton.setEnabled(False)
        self.UpdateState()

    def SetUse(self):
        if self.ui.UseMode.currentText()=="Default":
            self.ui.InterfButton.setEnabled(False)
        elif self.ui.UseMode.currentText()=="Create own puzzle":
            self.ui.InterfButton.setEnabled(True)
            self.ui.InterfButton.clicked.connect(self.CreatePieces)
        
        elif self.ui.UseMode.currentText()=="Place puzzle pieces":
            self.ui.InterfButton.setEnabled(True)
            self.ui.InterfButton.clicked.connect(self.PlacePieces)
            
    
    def AffichePlaced(self):
        self.Clear()
        for piece in self.ui.fixedpieces:
            self.AffichePiece(piece)
        self.AfficheBloc(self.ui.bloc)
        # self.ui.PlaceBlocButton.setEnabled(False)
        self.ui.InterfButton.setEnabled(False)
        
        self.ui.ApplyModeButton.setEnabled(False)

    def UpdateState(self):
        if (self.blocPlaced and self.puzzleInitialized):
            self.ui.SolveButton.setEnabled(True)
            self.ui.ApplySizeButton.setEnabled(False)
        elif (self.blocPlaced and self.method == transformExhaustive):
            self.ui.SolveButton.setEnabled(True)
            self.ui.InitButton.setEnabled(False)
            self.ui.ApplyPeriodButton.setEnabled(False)
            self.ui.ApplySizeButton.setEnabled(False)
        elif (self.method == transformExhaustive):
            self.ui.SolveButton.setEnabled(False)
            self.ui.InitButton.setEnabled(False)
            self.ui.ApplyPeriodButton.setEnabled(False)
        else:
            self.ui.SolveButton.setEnabled(False)
            self.ui.InitButton.setEnabled(True)
        
        self.ui.app.processEvents()



