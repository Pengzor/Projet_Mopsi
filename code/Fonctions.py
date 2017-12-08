import os
os.chdir('C:\\Users\\teovi\\Documents\\IMI\\Projet MoPSi\\')

from code.Pieces import *


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
        B=bloc(0,1)
        
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


def config_init(G,Pieces, Bloc= False):
    for piece in Pieces:
        ip,jp=piece.mat.shape
        piece.x=random.randint(0,G.n-ip)
        piece.y=random.randint(0,G.m-jp)
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


def transform1(Pieces, Pot, G, bloc, t):

    dep=random.randint(0,3)
    index=random.randint(0,len(Pieces)-1)
    P=Pieces[index]
    
    while not P.move_possible(liste_dep[dep], G):
        dep=random.randint(0,3)
    dPot1=P.varV_move(liste_dep[dep],G)
    if dPot1<=0 or loi(t,dPot1):
        P.move(liste_dep[dep], G)
        Pot+=dPot1
        G.refresh(Pieces,bloc)
     
    if P.rotate_possible(G):
        dPot2=P.varV_rotate(G)
        if dPot2<=0 or loi(t,dPot2):
            P.rotate(G)
            Pot+=dPot2
            G.refresh(Pieces,bloc)

    return int(Pot)


def transform2(Pieces, Pot, G, bloc, t):

    dep=random.randint(0,3)
    index=random.randint(0,len(Pieces)-1)
    P=Pieces[index]
    
    while not P.move_possible(liste_dep[dep], G):
        dep=random.randint(0,3)
    dPot=P.varV_move(liste_dep[dep],G)
    if dPot<=0 or loi(t,dPot):
        P.move(liste_dep[dep], G)
        Pot+=dPot
        G.refresh(Pieces,bloc)
        
        
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
        G.refresh(Pieces,bloc)
     
    if P.rotate_possible(G):
        dPot2=P.varV_rotate(G)
        if dPot2<=0 or loi(t,dPot2):
            P.rotate(G)
            Pot+=dPot2
            G.refresh(Pieces,bloc)
        
    return int(Pot)