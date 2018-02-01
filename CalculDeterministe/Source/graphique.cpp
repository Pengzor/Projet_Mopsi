#include<iostream>
using namespace std;

#include <Imagine/Graphics.h>
using namespace Imagine;

#include"graphique.h"


void affichePlateau(Plateau* P, int h, int w, int z){
    int N = P->getTaille();

    //trace lignes du quadrillage
    for (int i=0; i<N; ++i){
        drawLine(0, (i+1)*(h/N)*z, w*z, (i+1)*(h/N)*z, BLACK);
        drawLine((i+1)*(w/N)*z, 0, (i+1)*(w/N)*z, h*z, BLACK);
    }

    //affiche les cases bloquees
    for (int i=1; i<(N+1); ++i){
        for (int j=1; j<(N+1); ++j){
            if (P->operator ()(i,j) == 0){
                drawLine((j-1)*(h/N)*z, (i-1)*(w/N)*z, j*(h/N)*z, i*(w/N)*z, BLACK);
                drawLine((j-1)*(h/N)*z, i*(w/N)*z, j*(h/N)*z, (i-1)*(w/N)*z, BLACK);
            }
        }
    }
}

void afficheCase(int i, int j, int N, int h, int w, int z, Color col){
    ///i=1...N  ;  j=1...N

    int xh = (j-1)*(w/N)*z;
    int yh = (i-1)*(h/N)*z;
    fillRect(xh, yh, (w/N)*z, (h/N)*z, col);
}

void afficheCase(int numeroCase, int N, int h, int w, int z, Color col){
    ///numeroCase = 1...N^2

    int j = (numeroCase - 1)%N +1;
    int i = (numeroCase - j)/N + 1;
    int xh = (j-1)*(w/N)*z;
    int yh = (i-1)*(h/N)*z;
    fillRect(xh, yh, (w/N)*z, (h/N)*z, col);
}

void affichePiece(Piece &pi, Plateau* plat, int i, int j, int h, int w, int z){
    Color col = pi.getCouleur();
    ///affiche la piece pi en mettant le coin superieur gauche dans la case (i,j)
    int N = plat->getTaille();
    for (int l=1; l<=pi.getHauteur(); ++l){
        for (int c=1; c<=pi.getLargeur(); ++c){
            if (pi(l,c) == 1){
                afficheCase(l+i-1,c+j-1,N,h,w,z,col);
            }
        }
    }
}

void afficheToutesConfig(Piece &pi, Plateau* plat, int h, int w, int z){
    vector<vector<int> > S = calculeToutesConfig(pi, plat);
    vector<int> config;

    int x;
    int y;
    int N = plat->getTaille();
    Color col = pi.getCouleur();

    for (int i=0; i<S.size(); ++i){
        config = S[i];
        for (int j=0; j<config.size(); ++j){
            y = (config[j]-1) % N + 1;
            x = ((config[j]-1) - (y-1))/N + 1;
            afficheCase(x,y,N,h,w,z,col);
        }
        milliSleep(250);
        clearWindow();
        affichePlateau(plat,h,w,z);
    }
}

void afficheJeu(Jeu &game, int h, int w, int z){
    affichePlateau(game.getPlateau(), h, w, z);
    int i;
    int j;
    for (int k=0; k<game.getNbPieces(); ++k){
        i = game.getPositionPiece(k+1)[0];
        j = game.getPositionPiece(k+1)[1];
        affichePiece(*game.getPiece(k+1), game.getPlateau(), i, j, h, w, z);
    }
}

void afficheSolutionsAlgo(Jeu &game, vector<vector<Noeud*> > Solutions, int h, int w, int z){
    ///affiche toutes les solutions d'un puzzle resolu
    vector<Noeud*> uneSolution;
    Noeud* ligne;
    Noeud* nodePiece;
    Noeud* nodeCase;

    Plateau* P = game.getPlateau();

    Piece* pieceAConstruire;

    for (int i=0; i<Solutions.size(); ++i){
        noRefreshBegin();
        uneSolution = Solutions[i];
        affichePlateau(P, h, w, z);
        for (int k=0; k<uneSolution.size(); ++k){
            ligne = uneSolution[k];
            cout << ligne->getId() << " ";

            nodePiece = ligne->getDroite();
            pieceAConstruire = game.getPiece(nodePiece->getCol()->getId());

            nodeCase = nodePiece->getDroite();
            while (nodeCase != ligne){
                afficheCase(nodeCase->getCol()->getId() - game.getNbPieces(), P->getTaille(), h, w, z, pieceAConstruire->getCouleur());
                nodeCase = nodeCase->getDroite();
            }
            //milliSleep(300);
        }
        cout << endl;
        noRefreshEnd();
        //milliSleep(500);
        click();
        clearWindow();
        //milliSleep(100);
    }
}
