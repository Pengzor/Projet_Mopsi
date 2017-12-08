import os
os.chdir('C:\\Users\\teovi\\Documents\\IMI\\Projet MoPSi\\code')

from Classes import *
from code.Pieces import *
from PyQt4 import QtCore, QtGui

## Définition de pièces



class piece_default(piece):
    
    def __init__(self):
        super().__init__()
        self.color=""
        self.mat=np.array([0])
        
        
#Pour le puzzle 3x3

class piece1(piece):
    
    def __init__(self):
        super().__init__()
        self.color="piece_bleu.png"
        self.name='1'
        self.mat=np.array([[1,1],[0,1]])


class piece2(piece):
    
    def __init__(self):
        super().__init__()
        self.color="piece_vert.png"
        self.name='2'
        self.mat=np.array([[1,1]])

class piece3(piece):
    
    def __init__(self):
        super().__init__()
        self.color="piece_rose.png"
        self.name='3'
        self.mat=np.array([[1]])

class piece4(piece):
    
    def __init__(self):
        super().__init__()
        self.color="piece_rouge.png"
        self.name='4'
        self.mat=np.array([[1,1],[0,1]])

#Pour le vrai puzzle (7x7)

class pieceA(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,255,0)
        self.name='A'
        self.mat=np.array([[1,0,0],[1,1,0],[0,1,1]])


class pieceB(piece): ##
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,0,0)
        self.name='B'
        self.mat=np.array([[1,1,1,1,1]])

class pieceC(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,0,255)
        self.name='C'
        self.mat=np.array([[0,1,1],[1,1,1],[0,1,1]])

class pieceD(piece): ##
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,255,255)
        self.name='D'
        self.mat=np.array([[1,0,0],[1,1,0],[1,1,1]])
        
class pieceE(piece): 
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,255,0)
        self.name='E'
        self.mat=np.array([[0,1],[1,1],[1,1],[0,1]])


class pieceF(piece): 

    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,0,255)
        self.name='F'
        self.mat=np.array([[0,1],[1,1],[0,1],[0,1]])

class pieceG(piece): 
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(50,150,100)
        self.name='G'
        self.mat=np.array([[0,1,1,0],[0,1,1,1],[1,1,1,0]])

class pieceH(piece): 
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(173,79,9)
        self.name='H'
        self.mat=np.array([[0,1],[1,1],[0,1]])

class pieceI(piece): 
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,120,0)
        self.name='I'
        self.mat=np.array([[1,1]])
        
## Le puzzle 5x5

class piece5a(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,255,0)
        self.name='C'
        self.mat=np.array([[1,1,1],[0,0,1],[0,0,1]])
        
class piece5b(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,0,0)
        self.name='H'
        self.mat=np.array([[1,1],[1,1]])
        
class piece5c(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,0,255)
        self.name='H'
        self.mat=np.array([[1,1],[1,0],[1,0]])
        
class piece5d(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,255,0)
        self.name='C'
        self.mat=np.array([[0,1,0],[0,1,1],[1,1,0]])
        
class piece5e(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,255,255)
        self.name='H'
        self.mat=np.array([[1,1],[0,1]])
        
class piece5f(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,0,255)
        self.name='C'
        self.mat=np.array([[1,1,1]])