import numpy as np
import matplotlib.pyplot as plt
import random
import pygame 
from pygame.locals import *
import os
import time
from math import *

## Constantes

beta= 1

# r=200



## Classes

class grid:
    def __init__(self,n,m):
        self.mat=np.zeros((n,m))
        self.n = n
        self.m = m
    
    def clear(self):
        self.mat=np.zeros((self.n,self.m))
    
    
    def affiche(self):
        im1 = plt.matshow(self.mat.transpose())
        plt.colorbar(im1)
        # Grille:
        plt.gca().set_xticks([x - 0.5 for x in plt.gca().get_xticks()][1:], minor='true')
        plt.gca().set_yticks([y - 0.5 for y in plt.gca().get_yticks()][1:], minor='true')
        plt.grid(which='minor')
        plt.show()
    
    
    def add_piece(self, piece):   #x et y sont les coordonnées du coin supérieur gauche de la pièce
        n_p,m_p=piece.mat.shape
        x,y=piece.x, piece.y
        for i in range(n_p):
            for j in range(m_p):
                self.mat[x+i,y+j]+=piece.mat[i,j]
    
    
    def add_bloc(self, bloc):
        self.mat[bloc.x,bloc.y]+=1


    # def clear(self):
        # self.mat=np.zeros(self.mat.shape)


    def V(self):
        v=0
        for i in range(self.n):
            for j in range(self.m):
                if self.mat[i,j]>1:
                    v+=self.mat[i,j]-1;
        return int(v)


    def refresh(self, pieces, bloc=False):
        self.mat=np.zeros((self.n,self.m))
        if not bloc:
            pass
        else:
            self.add_bloc(bloc)
            
        for piece in pieces:
            self.add_piece(piece)



class piece:
    
    def __init__(self):
        pass
    

    def __str__(self):
        return self.name
        
    def permut_possible(self, grid, piece):
        i1,j1=self.mat.shape   
        i2,j2=piece.mat.shape

        
        if (self.x + i2 <= grid.n and self.y+j2 <= grid.m and piece.x+i1 <= grid.n and piece.y +j1 <= grid.m):
            return True
    
    def permut(self,grid,piece):
        if self.permut_possible(grid,piece):
            piece.x,self.x=self.x,piece.x
            piece.y,self.y=self.y,piece.y
            
            
    def	varV_permut(self, grid, piece):
        dV=0
        N=np.copy(grid.mat)
        i1,j1=self.mat.shape   
        i2,j2=piece.mat.shape
        
        for i in range(i1):  #On enlève la pièce 1
            for j in range(j1):
                if N[self.x + i, self.y + j]>1:
                    dV-=self.mat[i,j]
                N[self.x + i, self.y + j]-=self.mat[i,j]
        
        for i in range(i2): #On enlève la pièce 2
            for j in range(j2):
                if N[piece.x + i, piece.y + j]>1:
                    dV-=piece.mat[i,j]
                N[piece.x + i, piece.y + j]-=piece.mat[i,j]
                
        for i in range(i1): #On replace la pièce 1
            for j in range(j1):
                if N[piece.x + i, piece.y + j]>0:
                    dV+=self.mat[i,j]
                N[piece.x + i, piece.y + j]+=self.mat[i,j]
                
        for i in range(i2): #On replace la pièce 2
            for j in range(j2):
                if N[self.x + i, self.y + j]>0:
                    dV+=piece.mat[i,j]
                N[self.x + i, self.y + j]+=piece.mat[i,j]

        return dV
        
          
     
    def rotate_possible(self, grid):
        x,y=self.mat.shape   
        return (self.x+y <=grid.n and self.y+x <= grid.m)
        
    def rotate(self, grid): #Tourne la pièce d'un quart dans le sens horaire
        x,y=self.mat.shape
        newM= np.zeros((y,x))
        if self.rotate_possible(grid):
            for i in range(y):
                for j in range(x):
                    newM[i,j]=self.mat[-(j+1),i]
            self.mat=newM
        return True
    
    def rotate_(self): #Tourne la pièce d'un quart dans le sens horaire
        x,y=self.mat.shape
        newM= np.zeros((y,x))
        for i in range(y):
            for j in range(x):
                newM[i,j]=self.mat[-(j+1),i]
        self.mat=newM
        return True
    
    
    def move_possible(self, dir, grid):
        if (dir=='droite' and self.y+self.mat.shape[1]< grid.m):
            return True
        elif (dir=='gauche' and self.y>0):
            return True
        elif (dir=='haut' and self.x>0):
            return True
        elif (dir=='bas' and self.x+self.mat.shape[0]< grid.n):
            return True
        else: 
            return False
    
    def move(self, dir, grid):
        if self.move_possible(dir, grid):
            if dir=='droite':
                self.y+=1;
            elif dir=='gauche':
                self.y-=1;
            elif dir=='haut':
                self.x-=1;
            else:
                self.x+=1;
        else: 
            return False
        return True


    def varV_move(self,dir,Grid):
        M=Grid.mat
        if dir=='haut':
            dirx=-1
            diry=0
        if dir=='bas':
            dirx=1
            diry=0
        if dir=='gauche':
            dirx=0
            diry=-1
        if dir=='droite':
            dirx=0
            diry=1
        
        x,y=self.mat.shape
        dV=0
        N=np.copy(M)
        
        for i in range(x):
            for j in range(y):
                N[i+self.x,j+self.y]-=self.mat[i,j]  #Les poids sans la pièce qu'on bouge
    
        for i in range(x):
            for j in range(y):
                if M[i+self.x,j+self.y]>1:
                    dV-= self.mat[i,j]     
                if N[i+self.x+dirx,j+self.y+diry] > 0:
                    dV+= self.mat[i,j]
                    
        return dV


    def varV_rotate(self,Grid):
        M=Grid.mat
        x,y=self.mat.shape
        dV=0
        N=np.copy(M)
        
        for i in range(x):
            for j in range(y):
                N[i+self.x,j+self.y]-=self.mat[i,j]  #Les poids sans la pièce qu'on tourne
    
        for i in range(x):
            for j in range(y):
                if M[i+self.x,j+self.y]>1:
                    dV-= self.mat[i,j]                    
                if N[self.x + j , self.y + x -i-1] > 0:
                    dV+= self.mat[i,j]

        return dV


class bloc: #Pièce immobile
    def __init__(self,x,y):
        self.x=x
        self.y=y


