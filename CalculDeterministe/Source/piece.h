#pragma once

#include<iostream>
using namespace std;
#include <Imagine/Graphics.h>
using namespace Imagine;

#include<vector>


///------------Classe Plateau---------------------

class Plateau{
    //plateau carre de taille taille*taille
    int taille;
    //contient des '0' pour les cases occupées, contraintes fixees
    int* tab;
public:
    //constructeurs
    Plateau();
    Plateau(int N);     //plateau vide, aucune case fixee
    Plateau(int N, vector<int> casesVides);
    Plateau(int N, int n1);     //la case numero n1 est fixee
    //constructeur de copie
    Plateau(const Plateau &P);
    //accesseurs
    int operator()(int i, int j) const;
    int operator ()(int numCase) const;
    int getTaille() const;
    int getNbCasesFixees() const;
    //destructeur
    ~Plateau();

};


///-----------Classe Piece-------

class Piece{
    int hauteur;
    int largeur;
    //tab = matrice de taille hauteur*largeur
    //  tab[(i-1)*largeur + j-1] = 1 lorsque piece occupe cette case dans la matrice
    //i=1...hauteur, j=1...largeur
    int* tab;
    //couleur graphique
    Color col;
public:
    //constructeurs
    Piece();
    Piece(int newHauteur, int newLargeur, int* config, Color c);
    Piece(int newHauteur, int newLargeur, vector<int> config, Color c);
    //constructeur de copie
    Piece(const Piece &pi);
    //destructeur
    ~Piece();
    //accesseurs
    int operator ()(int i, int j) const;
    int getHauteur() const;
    int getLargeur() const;
    Color getCouleur() const;
    //operateurs
    bool compare(Piece &p) const;
    const Piece& operator =(const Piece &p);
    //rotation horaire
    void rotationHoraire();
    //calcul de toutes les configurations possibles dans le plateau
    vector<vector<int> > calculeConfigurations(Plateau* plat) const;
    //affichage
    void display() const;
};


///---------------------Classe jeu-----------------------

class Jeu{
    //Plateau
    Plateau* plat;
    int taillePlateau;
    int nbCasesFixees;
    //Pieces
    int nbPieces;
    vector<Piece*> pcs;
    //Position des pieces : //coordonnées de la case superieure gauche dans la matrice
    vector<vector<int> > positions;
public:
    //constructeurs
    Jeu();
    Jeu(Plateau* P);
    //accesseurs
    Plateau* getPlateau() const;
    Piece* getPiece(int num) const;
    vector<int> getPositionPiece(int numPiece) const;
    int getNbPieces() const;
    int getNbCasesLibres() const;
    int getNbCases() const;
    //mutateurs
    void ajoutePiece(Piece* p, int xi, int xj);
    void setPlateau(Plateau* P);
};


///---------------Autres fonctions-----------------

void setPointeur6(int* a, int x1, int x2, int x3, int x4, int x5, int x6);

void setPointeur9(int* a, int x1, int x2, int x3, int x4, int x5, int x6, int x7, int x8, int x9);

vector<vector<int> > calculeToutesConfig(Piece pi, Plateau* plat);

vector<vector<int> > calculeToutesConfig(Piece* pi, Plateau* plat);

