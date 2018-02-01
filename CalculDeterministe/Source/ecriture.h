#pragma once

#include <Imagine/Graphics.h>
using namespace Imagine;

#include<iostream>
using namespace std;

#include<vector>
#include<fstream>
#include<cstring>
#include<cstdlib>

#include"matrice.h"



void enregistreResultat(string nomFichier, vector<vector<Noeud*> > &Solutions, int nbPieces, int nbCasesLibres);

void lectureDonnees(string nomFichier, Jeu& game);
