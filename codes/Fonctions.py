import os
import csv
import numpy as np
import copy
os.chdir('D:\\Documents\\Ponts ParisTech\\Projet MOPSI\\Projet')

from codes.Pieces import *


## Fonctions

liste_dep=['haut','bas','gauche','droite']

def pieces_default(n,m):
    if (n==3 and m==3):
        PA = piece3a()
        PB = piece3b()
        PC = piece3c()
        Pieces=[PA,PB,PC]
        
    if (n==4 and m==4):
        PA = piece4a()
        PB = piece4b()
        PC = piece4c()
        PD = piece4d()
        Pieces=[PA,PB,PC,PD]
        
    if (n==5 and m==5):
        PA = piece5a()
        PB = piece5b()
        PC = piece5c()
        PD = piece5d()
        PE = piece5e()
        PF = piece5f()
        Pieces=[PA,PB,PC,PD,PE,PF]
        
    if (n==6 and m==6):
        PA=piece6a()
        PC=piece6c()
        PD=piece6d()
        PE=piece6e()
        PF=piece6f()
        PG=piece6g()
        PH=piece6h()
        PI=piece6i()
        Pieces=[PA,PC,PD,PE,PF,PG,PH,PI]
    
        
    if (n==7 and m==7):
        PA=pieceA()
        PB=pieceB()
        PC=pieceC()
        PD=pieceD()
        PE=pieceE()
        PF=pieceF()
        PG=pieceG()
        PH=pieceH()
        PI=pieceI()
        Pieces=[PA,PB,PC,PD,PE,PF,PG,PH,PI]
    
    return Pieces

def bloc_default(n,m):
    if (n==3 and m==3):
        B=bloc(0,0)
        
    if (n==4 and m==4):
        B=bloc(2,1)
        
    if (n==5 and m==5):
        B=bloc(2,1)
        
    if (n==6 and m==6):
        B=bloc(2,0)
        
    if (n==7 and m==7):
        B=bloc(2,1)

    
    return B
    
def remplissable(G,Pieces):  #Une condition nécessaire pour pouvoir résoudre le puzzle
    som= int(0)
    for piece in Pieces:
        som+= np.sum(piece.mat)
    return som==(G.n*G.m) - 1


def config_init(G,Pieces, fixedPieces, Bloc= False):
    for piece in Pieces:
        ip,jp=piece.mat.shape
        piece.x=random.randint(0,G.n-ip)
        piece.y=random.randint(0,G.m-jp)
        G.add_piece(piece)
    for piece in fixedPieces:
        G.add_piece(piece)
    
    if (not Bloc):
        pass
    else:
        G.add_bloc(Bloc)


def beta(t):
    b = 1.3
    a = 0.05
    return b*pow(t,a)


def loi(t, dP):
    crit= exp(-beta(t)*dP)
    return random.random() < crit


def transform1(Pieces, Pot, G, bloc, t, fixedPieces):

    dep=random.randint(0,3)
    index=random.randint(0,len(Pieces)-1)
    P=Pieces[index]
    
    while not P.move_possible(liste_dep[dep], G):
        dep=random.randint(0,3)
    dPot1=P.varV_move(liste_dep[dep],G)
    if dPot1<=0 or loi(t,dPot1):
        P.move(liste_dep[dep], G)
        Pot+=dPot1
        G.refresh(Pieces+fixedPieces,bloc)
     
    if P.rotate_possible(G):
        dPot2=P.varV_rotate(G)
        if dPot2<=0 or loi(t,dPot2):
            P.rotate(G)
            Pot+=dPot2
            G.refresh(Pieces+fixedPieces,bloc)

    return int(Pot)


def transform2(Pieces, Pot, G, bloc, t, fixedPieces):
    
    dep=random.randint(0,3)
    index=random.randint(0,len(Pieces)-1)
    P=Pieces[index]
    
    while not P.move_possible(liste_dep[dep], G):
        dep=random.randint(0,3)
    dPot=P.varV_move(liste_dep[dep],G)
    if dPot<=0 or loi(t,dPot):
        P.move(liste_dep[dep], G)
        Pot+=dPot
        G.refresh(Pieces+fixedPieces,bloc)
        
        
    i1=random.randint(0,len(Pieces)-1)
    P=Pieces[i1]
    i2=random.randint(0,len(Pieces)-1)
    Q=Pieces[i2]
    
    while not P.permut_possible(G, Q):
        i1=random.randint(0,len(Pieces)-1)
        P=Pieces[i1]
        i2=random.randint(0,len(Pieces)-1)
        Q=Pieces[i2]
    
    dPot1=P.varV_permut(G,Q)
    if dPot1<=0 or loi(t,dPot1):
        P.permut(G, Q)
        Pot+=dPot1
        G.refresh(Pieces+fixedPieces,bloc)
     
    if P.rotate_possible(G):
        dPot2=P.varV_rotate(G)
        if dPot2<=0 or loi(t,dPot2):
            P.rotate(G)
            Pot+=dPot2
            G.refresh(Pieces+fixedPieces,bloc)
        
    return int(Pot)


##Exhaustive method

def convert_Exhaustive(listeStr):
    L = []
    for z in listeStr:
        L.append(int(z))
    return(L)

def searchIndexOne(L):
    i = 0
    while(L[i] != 1):
        i += 1
    return i

def findPosition(solPiece, sizeGrid):
    #find the position of a piece solution in a Grid
    i = 0
    j = 0
    while (solPiece[i][j] != 1):
        if ((j+1)%sizeGrid == 0):
            i += 1
            j = 0
        else:
            j += 1
    ix = i
    jx = j
    
    i = 0
    j = 0
    while (solPiece[i][j] != 1):
        if ((i+1)%sizeGrid == 0):
            j += 1
            i = 0
        else:
            i += 1
    iy = i
    jy = j
    
    i0 = min(ix, iy)
    j0 = min(jx, jy)
    
    #matrix of the piece
    #--delete rows with only zeros
    i = 0
    while (i < solPiece.shape[0]):
        s = 0
        for k in range(0, solPiece.shape[1]):
            s += solPiece[i][k]
        if s == 0:
            #delete row i
            solPiece = np.delete(solPiece, i, axis=0)
        else:
            i += 1
    
    #--delete columns with only zeros
    j = 0
    while (j < solPiece.shape[1]):
        s = 0
        for k in range(0, solPiece.shape[0]):
            s += solPiece[k][j]
        if s == 0:
            #delete column j
            solPiece = np.delete(solPiece, j, axis=1)
        else:
            j += 1
    
    return i0, j0, solPiece

def transformExhaustive(sizeGrid, listNumFixedSquares, listPieces):
    os.chdir('D:\\Documents\\Ponts ParisTech\\Projet MOPSI\\Projet\\codes')
    
    #Writing the data
    f = open("DonneesPuzzle.txt", "w")
    f.write(str(sizeGrid) + '\n\n')
    f.write(str(len(listNumFixedSquares)) + '\n')
    f.write(str(listNumFixedSquares[0]))
    for i in range(1, len(listNumFixedSquares)):
        f.write(';' + str(listNumFixedSquares[i]))
    f.write('\n\n')
    f.write(str(len(listPieces)) + '\n\n')
    
    for i in range(0, len(listPieces)):
        #write data of the piece i
        tabPiece = listPieces[i].mat
        x,y = tabPiece.shape
        f.write(str(x) + ';' + str(y) + '\n')
        for k in range(0, x):
            f.write(str(tabPiece[k][0]))
            for l in range(1, y):
                f.write(';' + str(tabPiece[k][l]))
            f.write('\n')
        f.write('\n')
        
    f.close()
    
    
    #call the C++ executable
    os.system("puzzle.exe")
    
    #read the exit file
    f = open("ResultatPuzzle.csv", "r")
    listSolutions = []          #contain 1 element for each solution found
    
    line = f.readline()
    a = line.split(";")
    nbPieces = int(a[0])
    taillePlateau = int(a[1])
    nbSolutions = int(a[2])
    
    for i in range(0, nbSolutions):
        f.readline()
        sol = []
        for j in range(0, nbPieces):
            line = f.readline()
            line = line.split(";")
            line = line[:-1]
            line = convert_Exhaustive(line)
            sol.append(line)
        listSolutions.append(sol)
    
    
    
    f.close()
    
    os.chdir('D:\\Documents\\Ponts ParisTech\\Projet MOPSI\\Projet')
    
    #Process the solutions into sets of pieces
    setSolutions = []
    for i in range(0, len(listSolutions)):
        sol = listSolutions[i]
        solPieces = []
        for j in range(0, nbPieces):
            unePiece = sol[j]
            name = unePiece[0:nbPieces]
            squares = unePiece[nbPieces:]
            numPiece = searchIndexOne(name)
            p = copy.copy(listPieces[numPiece])        #piece we are examining the position in the solution
            
            squares = np.array(squares)
            squares = squares.reshape([sizeGrid, sizeGrid])
            y, x, mat = findPosition(squares, sizeGrid)
            if (mat.shape == p.mat.shape):
                equal = (mat == p.mat).all()
            else:
                equal = False
            comptTours = 0
            while (not(equal) and comptTours < 4):
                p.rotate_()
                comptTours += 1
                if (mat.shape == p.mat.shape):
                    equal = (mat == p.mat).all()
                else:
                    equal = False
            p.mat = np.transpose(p.mat)
            p.x = x
            p.y = y
            solPieces.append(p)
        setSolutions.append(solPieces)
    
    return(setSolutions)




