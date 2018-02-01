#pragma once

#include<iostream>
using namespace std;

#include <Imagine/Graphics.h>
using namespace Imagine;

#include"matrice.h"
#include"piece.h"

void affichePlateau(Plateau* P, int h, int w, int z);

void afficheCase(int i, int j, int N, int h, int w, int z, Color col);

void afficheCase(int numeroCase, int N, int h, int w, int z, Color col);

void affichePiece(Piece &pi, Plateau* plat, int i, int j, int h, int w, int z);

void afficheToutesConfig(Piece &pi, Plateau* plat, int h, int w, int z);

void afficheJeu(Jeu &game, int h, int w, int z);

void afficheSolutionsAlgo(Jeu &game, vector<vector<Noeud*> > Solutions, int h, int w, int z);
