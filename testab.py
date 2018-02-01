import os
import sys
import inspect

os.chdir('C:\\Users\\teovi\\Documents\\IMI\\Projet MoPSi\\')

from code.Fonctions import *
# from appli.Screen import *

L=[]

n=5
m=5
grid = grid(n,m)

pieces=pieces_default(n,m)
fixedpieces=[]

bloc = bloc_default(n,m)
        

for i in range(20):
    grid.clear()
    compteur = 0
    Pot=0
    config_init(grid, pieces, fixedpieces, bloc)
    Pot=grid.V()
    while (Pot > 0):
        compteur+=1
        Pot = transform2(pieces, Pot, grid, bloc, compteur, fixedpieces)
    print(compteur)
    L.append(compteur)


    
    
    

