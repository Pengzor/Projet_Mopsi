import os
import inspect
path = os.path.dirname(inspect.getfile(inspect.currentframe()))
os.chdir(path)

from appli.Screen import *
from appli.ScreenBis import *
from appli.ScreenTer import *
from appli.ScreenQuad import *

  
class Controller:
    def __init__(self, ui):
        #to link with the screen
        self.ui = ui
        #For pausing
        self.continu=True	 
        #grid       
        self.grid=self.ui.grid
        #Solving method
        self.method= transform1
        #Refresh period
        self.T=1000
        #Counter
        self.compteur=0
        
        #Variables of state
        self.blocPlaced = True
        self.puzzleInitialized = False
        self.piecesAlreadyPlaced = False
        self.UpdateState()

    def bind(self):     #Assigns each widget to the correspinding function
        self.ui.InitButton.clicked.connect(self.Init)
        self.ui.ResetButton.clicked.connect(self.Reset)
        self.ui.SolveButton.clicked.connect(self.Solve)
        self.ui.PauseButton.clicked.connect(self.Pause)
        self.ui.PlaceBlocButton.clicked.connect(self.PlaceBloc)
        self.ui.ApplySizeButton.clicked.connect(self.SetSize)
        self.ui.ApplyPeriodButton.clicked.connect(self.SetPeriod)
        self.ui.ApplyMethodButton.clicked.connect(self.SetMethod)
        self.ui.ApplyModeButton.clicked.connect(self.SetUse)
        self.ui.InterfButton.clicked.connect(self.UserWindow)
        self.SetUse()
    
    
    def AffichePiece(self, piece):      #Displays a given piece on the screen
        n_p,m_p=piece.mat.shape
        for i in range(n_p):
            for j in range(m_p):
                if piece.mat[i,j]==1:
                    self.ui.DrawRect(piece.x + i,piece.y + j,  piece.color)
    
    
    def AfficheBloc(self, bloc):        #Displays the bloc
        self.ui.DrawCercle(bloc.x,bloc.y)
        

    def Clear(self):        #Clears the grid
        self.ui.Scene.clear()
        self.ui.DrawGrid()
        
        #Buttons management
        self.ui.SolveButton.setEnabled(False)
        self.ui.ResetButton.setEnabled(False)
        
    
    def Reset(self):        #Resets the interface
        self.Clear()
        self.grid.clear()
        self.compteur=0
        self.ui.CompteurLCD.display(0)
        self.ui.pieces = pieces_default(self.ui.n, self.ui.m)
        self.ui.fixedpieces=[]
        
        #Buttons management
        self.ui.ResetButton.setEnabled(False)
        self.ui.ApplySizeButton.setEnabled(True)
        self.ui.ApplyPeriodButton.setEnabled(True)
        self.ui.ApplyMethodButton.setEnabled(True)
        self.ui.PlaceBlocButton.setEnabled(True)
        self.ui.ApplyModeButton.setEnabled(False)
        self.ui.InterfButton.setEnabled(False)
        
        #State variables
        self.blocPlaced = True
        self.puzzleInitialized = False
        self.piecesAlreadyPlaced = False
        self.UpdateState()
        self.ui.app.processEvents()
    
    
    def Refresh(self, pieces, bloc= False):     #Refreshes the position of the pieces on the screen
        self.Clear()
        if not bloc:
            pass
        else:
            self.AfficheBloc(bloc)
        for piece in pieces:
            self.AffichePiece(piece)
    
    
    def Init(self):     #Randomly places pieces on the screen
        self.compteur=0
        self.Clear()
        self.AfficheBloc(self.ui.bloc)
        self.grid.clear()
        config_init(self.grid ,self.ui.pieces, self.ui.fixedpieces, self.ui.bloc)
        
        for piece in self.ui.pieces:
            self.AffichePiece(piece)
        for piece in self.ui.fixedpieces:
            self.AffichePiece(piece)
            
        #Buttons management
        self.ui.SolveButton.setEnabled(True)
        self.ui.ResetButton.setEnabled(True)
        self.ui.PlaceBlocButton.setEnabled(True)
        self.ui.ApplySizeButton.setEnabled(False)
        self.ui.PlaceBlocButton.setEnabled(False)
        self.ui.ApplyModeButton.setEnabled(False)
        self.ui.CompteurLCD.display(0)
        
        self.puzzleInitialized = True
        self.UpdateState()


    def Pause(self):        #Pauses the resolution
        self.continu= False
        
        #Buttons management
        self.ui.PauseButton.setEnabled(False)
        self.ui.InitButton.setEnabled(True)
        self.ui.SolveButton.setEnabled(True)

    
    
    def Solve(self):        #Launches the resolution 
        self.continu = True
        
        #Buttons management
        self.ui.SolveButton.setEnabled(False)
        self.ui.ApplyPeriodButton.setEnabled(False)
        self.ui.ApplyMethodButton.setEnabled(False)
        self.ui.InitButton.setEnabled(False)
        self.ui.PauseButton.setEnabled(True)
        self.ui.PlaceBlocButton.setEnabled(False)
        
        # ---Simulated annealing---
        if (self.method==transform1 or self.method==transform2):
            Pot=self.grid.V();
        
            while (Pot > 0 and self.continu):
                self.ui.CompteurLCD.display(self.compteur)
                self.compteur+=1
                
                Pot = self.method(self.ui.pieces, Pot, self.grid, self.ui.bloc, self.compteur, self.ui.fixedpieces)
            
                if (self.compteur%self.T==0):   #Refreshing the screen every T iterations
                    self.Refresh(self.ui.pieces+self.ui.fixedpieces, self.ui.bloc)
                    
                    #Magical functions preventing overflow
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
                
            #Buttons management
            self.ui.ResetButton.setEnabled(True)
            self.ui.ApplyPeriodButton.setEnabled(True)
            self.ui.ApplyMethodButton.setEnabled(True)
        
        #---Exhaustive Algorithm---
        elif (self.method==transformExhaustive):
            
            #momentarily disable buttons
            self.ui.DisableAll()
            
            # #indicate the solving operation
            # solving = QtGui.QMessageBox()
            # solving.setIcon(QtGui.QMessageBox.Information)
            # 
            # text = "Calculation in progress..."
            # msg.setText(text)
            # msg.setWindowTitle("Solving")
            # msg.exec_()
            
            #solutions to display
            #--Rq : always 1 single fixed square
            numFixedSquares = []
            for fixedPiece in self.ui.fixedpieces:
                fixedMat = fixedPiece.mat
                fixedN, fixedM = fixedMat.shape
                xf, yf = fixedPiece.x, fixedPiece.y
                for iFix in range(0, fixedN):
                    for jFix in range(0, fixedM):
                        if fixedMat[iFix][jFix] == 1:
                            numFixedSquares.append((yf + jFix)*self.grid.n + xf + iFix + 1)
            numFixedSquares.append(self.ui.bloc.y * self.grid.n + self.ui.bloc.x + 1)
            setSolutions = self.method(self.grid.n, numFixedSquares, self.ui.pieces)
            
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

    def PlaceBloc(self):        #Opens the bloc placement interface
        BlocPlacementWindow(self.ui)


    def SetPeriod(self):        #To modify the refresh Period
        self.T=int(self.ui.RefreshPeriod.currentText())

    
    def SetSize(self):      #To change the size of the puzzle
        self.ui.n=int(self.ui.PuzzleSize.currentText()[0])
        self.ui.m=int(self.ui.PuzzleSize.currentText()[-1])
        self.ui.pieces= pieces_default(self.ui.n, self.ui.m)
        self.ui.bloc=bloc_default(self.ui.n, self.ui.m)
        self.grid = grid(self.ui.n,self.ui.m)
        self.ui.res = int(700/max(self.ui.n, self.ui.m))
        self.Reset()
        
    def CreatePieces(self):     #Opens the piece creation interface
        PieceCreationWindow(self.ui)
    
    def PlacePieces(self):      #Opens the piece placement interface
        PiecePlacementWindow(self.ui)
        
    def SetMethod(self):        #To set the solving method
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


    def SetUse(self):       #Links the InterButton to the corresponding use
        if self.ui.UseMode.currentText()=="Default":
            self.ui.InterfButton.setEnabled(False)
        elif self.ui.UseMode.currentText()=="Create own puzzle":
            self.ui.InterfButton.setEnabled(True)
        
        elif self.ui.UseMode.currentText()=="Place puzzle pieces":
            self.ui.InterfButton.setEnabled(True)

    def UserWindow(self):
        if self.ui.UseMode.currentText()=="Create own puzzle":
            self.CreatePieces()
        elif self.ui.UseMode.currentText()=="Place puzzle pieces":
            self.PlacePieces()
    
    def AffichePlaced(self):        #Display only pieces fixed in the interface
        self.Clear()
        for piece in self.ui.fixedpieces:
            self.AffichePiece(piece)
        self.AfficheBloc(self.ui.bloc)
        self.ui.InterfButton.setEnabled(False)
        
        self.ui.ApplyModeButton.setEnabled(False)


    def UpdateState(self):      #Basically an easier way to manage button status
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
        
        if (self.piecesAlreadyPlaced):
            self.ui.ApplyModeButton.setEnabled(False)
            self.ui.PlaceBlocButton.setEnabled(False)
        elif (self.puzzleInitialized):
            self.ui.ApplyModeButton.setEnabled(False)
            self.ui.PlaceBlocButton.setEnabled(False)
        elif (self.blocPlaced):
            self.ui.ApplyModeButton.setEnabled(True)
            self.ui.PlaceBlocButton.setEnabled(True)
        else:
            self.ui.ApplyModeButton.setEnabled(False)
            self.ui.PlaceBlocButton.setEnabled(True)
        
        self.ui.ResetButton.setEnabled(True)
        
        self.ui.app.processEvents()