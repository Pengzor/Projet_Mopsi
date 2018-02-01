#pragma once

#include<cstring>
#include<set>

#include"piece.h"


class Noeud{
    ///---------type de noeud-----------
    /// valeur >= 0 : alors noeud de type 'data'
    /// valeur == -1 : 'header' de colonne
    /// valeur == -2 : 'header' de ligne
    /// valeur == -3 : 'header' de matrice
    int valeur;
    ///--------------identifiant--------
    /// eq numero de ligne/colonne
    /// vaut 0 si valeur != -1 ou -2
    int id;
    ///somme des valeurs dans une colonne (seulement pour les noeuds de type -1
    int sommeColonne;
    ///------pointeurs vers les noeuds voisins-----------
    Noeud* haut;
    Noeud* bas;
    Noeud* droite;
    Noeud* gauche;
    ///----------pointeurs vers les 'headers' de ligne et de colonne
    /// pointeur null si noeud deja de type 'header'
    Noeud* col;
    Noeud* lig;
public:
    //constructeurs
    Noeud();
    Noeud(int value, int identif);
    //mutateurs
    void setDroite(Noeud* node);
    void setGauche(Noeud* node);
    void setHaut(Noeud* node);
    void setBas(Noeud* node);
    void setCol(Noeud* node);
    void setLig(Noeud* node);
    void incrSommeColonne();
    void decrSommeColonne();
    //accesseurs
    Noeud* getDroite() const;
    Noeud* getGauche() const;
    Noeud* getHaut() const;
    Noeud* getBas() const;
    Noeud* getCol() const;
    Noeud* getLig() const;
    int getValeur() const;
    int getId() const;
    int getSommeColonne() const;
    //insertion
    void insereLigneEntre(Noeud* n1, Noeud* n2);
    void insereColonneEntre(Noeud* n1, Noeud* n2);
    void effaceLigneEntre();
    void effaceColonneEntre();
    void restaureLigneEntre();
    void restaureColonneEntre();
};


class Matrice{
    Noeud* h;       //de type 'header' de matrice
    int nbLignes;
    int nbColonnes;
public:
    //constructeurs
    Matrice();
    Matrice(int nbPieces, int nbCases);
    Matrice(Jeu game);
    //accesseurs
    int getNbLignes() const;
    int getNbColonnes() const;
    Noeud* getHeaderMatrice() const;
    Noeud* getHeaderColonne(int numCol) const;
    Noeud* getHeaderLigne(int numLig) const;
    Noeud* getColonneMin() const;
    //mutateurs
    void ajouteDerniereLigne(vector<int> &emplacementUns);
    void effaceLigne(Noeud* l);
    void effaceColonne(Noeud* c);
    void restaureLigne(Noeud* l);
    void restaureColonne(Noeud* c);
    //operateur ()
    int operator()(const Noeud* ligne, const Noeud* colonne) const;
    int get(const Noeud* l, const Noeud* c) const;
    //affichage
    void displayLigne(const Noeud* l) const;
    void displayColonne(const Noeud* c) const;
    void displayColonnesId() const;
    void displayMatrice() const;
};


///---------------------Classe Arbre (d'exploration)--------------

class Arbre{
    int updates;
    Arbre* pere;
    vector<Arbre*> fils;
public:
    //constructeurs
    Arbre();
    Arbre(int valUpdate, Arbre* noeudPere);
    //destructeur
    ~Arbre();
    //accesseur
    Arbre* getFils(int i) const;
    int getNbFils() const;
    int getUpdates() const;
    //ajoute un fils
    Arbre* ajouteFils(int valUpdates);
    //affichage des infos
    void calculeInfos(int &nbTotalNoeuds, int &nbTotalUpdates, vector<vector<int>> &tab) const;
    void afficheInfos() const;
    //enregistre les infos de l'arbre dans un fichier csv
    void enregistreInfos(string nomFichier) const;
};



///-------------------Autres fonctions-----------------------------

void ajouteConfigPiece1(Matrice* M);

void ajouteConfigPiece2(Matrice* M);

void ajouteConfigPiece3(Matrice* M);
