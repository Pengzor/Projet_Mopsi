import os
import inspect
path = os.path.dirname(os.path.dirname(inspect.getfile(inspect.currentframe())))
os.chdir(path)
print(os.getcwd())


from codes.Classes import *
from codes.Pieces import *
from PyQt4 import QtCore, QtGui

## Définition de pièces



class piece_default(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,255,255)
        self.mat=np.array([0])
        
        
        
##Pour le puzzle 3x3


class piece3a(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,255,0)
        self.mat=np.array([[1,1],[0,1]])


class piece3b(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,255,0)
        self.mat=np.array([[1,1]])


class piece3c(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,0,255)
        self.mat=np.array([[1,1],[0,1]])



##Pour le puzzle 4x4


class piece4a(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,255,0)
        self.mat=np.array([[1,1,1],[0,0,1],[0,0,1]])

        
class piece4b(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,255,0)
        self.mat=np.array([[1,0],[1,1],[1,0]])
        
        
class piece4c(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,255,255)
        self.mat=np.array([[1,1],[0,1]])

class piece4d(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,0,255)
        self.mat=np.array([[1,1],[0,1]])
    
        
        
## Le puzzle 5x5


class piece5a(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,255,0)
        self.mat=np.array([[1,1,1],[0,0,1],[0,0,1]])
        
class piece5b(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,0,0)
        self.mat=np.array([[1,1],[1,1]])
        
class piece5c(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,0,255)
        self.mat=np.array([[1,1],[1,0],[1,0]])
        
class piece5d(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,255,0)
        self.mat=np.array([[0,1,0],[0,1,1],[1,1,0]])
        
class piece5e(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,255,255)
        self.mat=np.array([[1,1],[0,1]])
        
class piece5f(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,0,255)
        self.mat=np.array([[1,1,1]])
        
        
        
##Pour le puzzle 6x6


class piece6a(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,255,0)
        self.mat=np.array([[1,0,0],[1,1,0],[0,1,1]])


class piece6c(piece):
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,0,255)
        self.mat=np.array([[0,1],[1,1],[0,1]])
        

class piece6d(piece): 
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(0,255,255)
        self.mat=np.array([[1,0,0],[1,1,0],[1,1,1]])
        
class piece6e(piece): 
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,255,0)
        self.mat=np.array([[1,1]])


class piece6f(piece): 

    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,0,255)
        self.mat=np.array([[1,1],[0,1],[0,1]])

class piece6g(piece): 
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(50,150,100)
        self.mat=np.array([[0,1,1,0],[0,1,1,1],[1,1,1,0]])

class piece6h(piece): 
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(173,79,9)
        self.mat=np.array([[0,1],[1,1]])

class piece6i(piece): 
    
    def __init__(self):
        super().__init__()
        self.color=QtGui.QColor(255,120,0)
        self.mat=np.array([[1,1]])
        
    
    
##Pour le puzzle 7x7


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