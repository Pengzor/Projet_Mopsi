#pragma once

#include<iostream>
using namespace std;

#include<vector>
#include<cstring>

#include"matrice.h"
#include"piece.h"
#include"graphique.h"


int rechercheSol(Matrice* M, vector<vector<Noeud*> > &Solutions, vector<Noeud*> &solPartielle, string indent);

void displaySolutions(vector<vector<Noeud*> > &S, Matrice* M);

int rechercheSol2(Matrice* M, Jeu& game, vector<vector<Noeud*> > &Solutions, vector<Noeud*> &solPartielle, string indent, int h, int w, int z);

int rechercheSol3(Matrice* M, vector<vector<Noeud*> > &Solutions, vector<Noeud*> &solPartielle, string indent, int &compt);

int rechercheSol5(Matrice* M, vector<vector<Noeud*> > &Solutions, vector<Noeud*> &solPartielle, string indent, Arbre* ArbreExploration);

int rechercheSol6(Matrice* M, vector<vector<Noeud*> > &Solutions, vector<Noeud*> &solPartielle, string indent, Arbre* ArbreExploration);
