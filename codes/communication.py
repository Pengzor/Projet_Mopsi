import os
import csv

nomFichier = "ResultatPuzzle.csv"

os.system("puzzle.exe")


#lecture du fichier resultat

f = open("ResultatPuzzle.csv", "r")

ligne = f.readline()
a = ligne.split(";")
nbPieces = int(a[0])
taillePlateau = int(a[1])
nbSolutions = int(a[2])

def convert(listeStr):
    L = []
    for z in listeStr:
        L.append(int(z))
    return(L)

#ensemble des solutions realisables
Solutions = []

for i in range(0, nbSolutions):
    f.readline()
    sol = []
    for j in range(0, nbPieces):
        ligne = f.readline()
        ligne = ligne.split(";")
        ligne = ligne[:-1]
        ligne = convert(ligne)
        sol.append(ligne)
    Solutions.append(sol)



f.close()