#include<iostream>
using namespace std;

#include<cassert>

#include"matrice.h"


///------------------Classe Noeud---------------------------

//constructeurs

Noeud::Noeud(){
    valeur = 0;
    id = 0;
    sommeColonne = 0;
    haut = 0;
    bas = 0;
    droite = 0;
    gauche = 0;
    col = 0;
    lig = 0;
}

Noeud::Noeud(int value, int identif){
    if (value == -3){
        valeur = -3;
        id = 0;
        col = 0;
        lig = 0;
    }
    else if (value == -1){
        valeur = -1;
        id = identif;
        col = this;
        lig = 0;
    }
    else if (value == -2){
        valeur = -2;
        id = identif;
        col = 0;
        lig = this;
    }
    else{
        valeur = 0;
        id = 0;
        col = 0;
        lig = 0;
    }
    sommeColonne = 0;
    haut = this;
    bas = this;
    droite = this;
    gauche = this;

}

//accesseurs

Noeud* Noeud::getDroite() const{
    return droite;
}

Noeud* Noeud::getGauche() const{
    return gauche;
}

Noeud* Noeud::getHaut() const{
    return haut;
}

Noeud* Noeud::getBas() const{
    return bas;
}

Noeud* Noeud::getCol() const{
    return col;
}

Noeud* Noeud::getLig() const{
    return lig;
}

int Noeud::getValeur() const{
    return valeur;
}

int Noeud::getId() const{
    return id;
}

int Noeud::getSommeColonne() const{
    return sommeColonne;
}

//mutateurs

void Noeud::setDroite(Noeud *node){
    droite = node;
}

void Noeud::setGauche(Noeud *node){
    gauche = node;
}

void Noeud::setHaut(Noeud *node){
    haut = node;
}

void Noeud::setBas(Noeud *node){
    bas = node;
}

void Noeud::setCol(Noeud *node){
    col = node;
}

void Noeud::setLig(Noeud *node){
    lig = node;
}

void Noeud::incrSommeColonne(){
    sommeColonne += 1;
}

void Noeud::decrSommeColonne(){
    sommeColonne -= 1;
}

//insertion

void Noeud::insereLigneEntre(Noeud *n1, Noeud *n2){
    ///insere le noeud courant dans la liste entre n1 et n2, en ligne
    gauche = n1;
    n1->setDroite(this);
    droite = n2;
    n2->setGauche(this);
    if (valeur >= 0){
        //noeud de type 'data' insere
        col->incrSommeColonne();
    }
}

void Noeud::insereColonneEntre(Noeud *n1, Noeud *n2){
    ///insere le noeud courant dans la liste entre n1 et n2, en colonne
    haut = n1;
    n1->setBas(this);
    bas = n2;
    n2->setHaut(this);
    if (valeur >= 0){
        //noeud de type 'data' insere
        col->incrSommeColonne();
    }
}

void Noeud::effaceLigneEntre(){
    ///efface le noeud courant de la liste en ligne
    gauche->setDroite(droite);
    droite->setGauche(gauche);
    if (valeur >= 0){
        //noeud de type 'data' efface
        col->decrSommeColonne();
    }
}

void Noeud::effaceColonneEntre(){
    ///efface le noeud courant de la liste en colonne
    haut->setBas(bas);
    bas->setHaut(haut);
    if (valeur >= 0){
        //noeud de type 'data' efface
        col->decrSommeColonne();
    }
}

void Noeud::restaureLigneEntre(){
    droite->setGauche(this);
    gauche->setDroite(this);
    if (valeur >= 0){
        //noeud de type 'data' restaure
        col->incrSommeColonne();
    }
}

void Noeud::restaureColonneEntre(){
    haut->setBas(this);
    bas->setHaut(this);
    if (valeur >= 0){
        //noeud de type 'data' restaure
        col->incrSommeColonne();
    }
}



///---------------------Classe Matrice--------------------------------

//constructeurs

Matrice::Matrice(){
    h = 0;
    nbLignes = 0;
    nbColonnes = 0;
}

Matrice::Matrice(int nbPieces, int nbCases){
    //construit un 'header' de matrice
    h = new Noeud(-3, 0);
    //contruit les colonnes de pieces et de cases
    Noeud* c;
    for (int j=0; j<(nbPieces+nbCases); ++j){
        c = new Noeud(-1, j+1);
        c->insereLigneEntre(h->getGauche(), h);
    }
    //mets a jour les informations generales de la matrice
    nbLignes = 0;
    nbColonnes = nbPieces + nbCases;
}

Matrice::Matrice(Jeu game){
    Plateau* P = game.getPlateau();
    int nbPcs = game.getNbPieces();

    //construit un header de matrice
    h = new Noeud(-3, 0);
    //contruit les colonnes de pieces et de cases
    Noeud* c;
    for (int j=1; j<nbPcs+1; ++j){
        c = new Noeud(-1, j);
        c->insereLigneEntre(h->getGauche(), h);
    }
    for (int j=1; j<game.getNbCases()+1; ++j){
        if (P->operator ()(j) == 1){
            c = new Noeud(-1, j+nbPcs);
            c->insereLigneEntre(h->getGauche(), h);
        }
    }
    //mets a jour les informations generales de la matrice
    nbLignes = 0;
    nbColonnes = nbPcs + game.getNbCasesLibres();
}

//accesseurs

int Matrice::getNbLignes() const{
    return nbLignes;
}

int Matrice::getNbColonnes() const{
    return nbColonnes;
}

Noeud* Matrice::getHeaderMatrice() const{
    return h;
}

Noeud* Matrice::getHeaderColonne(int numCol) const{
    Noeud* a = h->getDroite();
    while (a->getId() < numCol){
        a = a->getDroite();
    }
    //verifie que numCol est bien valide
    assert(a->getId() == numCol);
    return a;
}

Noeud* Matrice::getHeaderLigne(int numLig) const{
    Noeud* a = h->getBas();
    while (a->getId() < numLig){
        a = a->getBas();
    }
    //verifie que numLig est bien valide
    assert(a->getId() == numLig);
    return a;
}

Noeud* Matrice::getColonneMin() const{
    ///retourne la colonne possedant le moins de '1'
    Noeud* nodeMin = h->getDroite();
    int nbMin = nodeMin->getSommeColonne();

    Noeud* node = nodeMin->getDroite();

    while (node != h){
        if (node->getSommeColonne() < nbMin){
            nbMin = node->getSommeColonne();
            nodeMin = node;
        }
        node = node->getDroite();
    }
    return nodeMin;
}

//mutateurs

void Matrice::ajouteDerniereLigne(vector<int> &emplacementUns){
    ///tab : designe les numeros des colonnes où doit figurer un un dans la nouvelle ligne
    //construit un 'header' de ligne
    Noeud* l = new Noeud(-2, nbLignes + 1);
    l->insereColonneEntre(h->getHaut(), h);
    Noeud* b;
    Noeud* c;
    Noeud* nodeDroite;
    Noeud* nodeGauche;
    //construit et positionne les Noeuds 'data'
    for (int j=0; j<emplacementUns.size(); ++j){
        //cout << "   config " << j+1 << endl;
        b = new Noeud(1, 0);
        c = getHeaderColonne(emplacementUns[j]);
        b->setCol(c);
        b->setLig(l);
        //insere b au bon endroit dans l
        nodeDroite = l->getDroite();
        while ((nodeDroite != l) && (nodeDroite->getCol()->getId() < emplacementUns[j])){
            nodeDroite = nodeDroite->getDroite();
        }
        nodeGauche = nodeDroite->getGauche();
        b->insereLigneEntre(nodeGauche, nodeDroite);
        b->insereColonneEntre(c->getHaut(), c);
    }
    //met a jour les informations de la matrice
    nbLignes += 1;
}

void Matrice::effaceLigne(Noeud* l){
    ///efface la ligne de header l de la matrice
    //verifie que l est bien dans la matrice
    Noeud* node = h->getBas();
    while ((node != h) && (node != l)){
        node = node->getBas();
    }
    assert(node == l);
    //on efface tous les elements de la ligne
    l->effaceColonneEntre();
    Noeud* elem = l->getDroite();
    while (elem != l){
        elem->effaceColonneEntre();
        elem = elem->getDroite();
    }
    //actualise les informations de la matrice
    nbLignes -= 1;
}

void Matrice::effaceColonne(Noeud *c){
    ///efface la colonne de header c de la matrice
    //verifie que c est bien dans la matrice
    Noeud* node = h->getDroite();
    while ((node != h) && (node != c)){
        node = node->getDroite();
    }
    assert(node == c);
    //on efface tous les elements de la colonne
    c->effaceLigneEntre();
    Noeud* elem = c->getBas();
    while (elem != c){
        elem->effaceLigneEntre();
        elem = elem->getBas();
    }
    //actualise les informations de la matrice
    nbColonnes -= 1;
}

void Matrice::restaureLigne(Noeud *l){
    ///restaure la ligne effacee dont le header de ligne est l
    l->restaureColonneEntre();
    Noeud* elem = l->getDroite();
    while (elem != l){
        elem->restaureColonneEntre();
        elem = elem->getDroite();
    }
    //actualise les informations de la matrice
    nbLignes += 1;
}

void Matrice::restaureColonne(Noeud *c){
    ///restaure la colonne effacee dont le header de colonne est c
    c->restaureLigneEntre();
    Noeud* elem = c->getBas();
    while (elem != c){
        elem->restaureLigneEntre();
        elem = elem->getBas();
    }
    //actualise les informations de la matrice
    nbColonnes += 1;
}

//operateur ()

int Matrice::operator ()(const Noeud* ligne, const Noeud* colonne) const{
    ///retourne la valeur d'une case de la matrice,
    /// où 'ligne' et 'colonne' sont des 'headers'
    int numCol = colonne->getId();

    Noeud* node = ligne->getDroite();

    while ((node != ligne) && (node->getCol()->getId() < numCol)){
        node = node->getDroite();
    }
    if (node->getCol() == colonne){
        return 1;
    }
    else{
        return 0;
    }
}

int Matrice::get(const Noeud *l, const Noeud *c) const{
    return operator ()(l,c);
}

//affichage

void Matrice::displayLigne(const Noeud *l) const{
    assert (l->getValeur() == -2);
    Noeud* c = h->getDroite();
    while (c != h){
        cout << get(l,c) << " ";
        c = c->getDroite();
    }
    cout << endl;
}

void Matrice::displayColonne(const Noeud *c) const{
    assert (c->getValeur() == -1);
    Noeud* l = h->getBas();
    while (l != h){
        cout << get(l,c) << " ";
        l = l->getBas();
    }
    cout << endl;
}

void Matrice::displayMatrice() const{
    Noeud* l = h->getBas();
    cout << endl;
    while (l != h){
        displayLigne(l);
        l = l->getBas();
    }
    cout << endl;
}

void Matrice::displayColonnesId() const{
    Noeud* c = h->getDroite();
    while (c != h){
        cout << c->getId() << " ";
        c = c->getDroite();
    }
    cout << endl;
}


///------------------------Classe Arbre (d'exploration)---------------

//constructeurs

Arbre::Arbre(){
    updates = -1;
    pere = 0;
}

Arbre::Arbre(int valUpdate, Arbre* noeudPere){
    updates = valUpdate;
    pere = noeudPere;
}

//destructeur

Arbre::~Arbre(){
    for (int i=0; i<fils.size(); ++i){
        delete fils[i];
    }
}

//accesseur

Arbre* Arbre::getFils(int i) const{
    assert((i >= 0) && (i < fils.size()));
    return fils[i];
}

int Arbre::getNbFils() const{
    return fils.size();
}

int Arbre::getUpdates() const{
    return updates;
}

//ajoute un fils

Arbre* Arbre::ajouteFils(int valUpdates){
    Arbre* a = new Arbre(valUpdates, this);
    fils.push_back(a);
    return a;
}

//affichage des infos

void Arbre::calculeInfos(int &nbTotalNoeuds, int &nbTotalUpdates, vector<vector<int> > &tab) const{
    vector<Arbre*> file;
    nbTotalNoeuds = 0;
    nbTotalUpdates = 0;
    tab.clear();

    int kGeneration = 0;
    Arbre* a;

    //initialisation

    for (int i=0; i<fils.size(); ++i){
        file.push_back(fils[i]);
    }
    int nbGeneration0 = 1;
    int nbGeneration1 = 0;
    int nbUpdates = updates;
    vector<int> niveau;
    niveau.push_back(kGeneration);
    niveau.push_back(nbGeneration0);
    niveau.push_back(nbUpdates);
    tab.push_back(niveau);

    kGeneration += 1;
    nbGeneration0 = fils.size();
    nbUpdates = 0;
    niveau.clear();

    while (file.size() > 0){

        //parcours une generation
        for (int i=0; i<nbGeneration0; ++i){
            a = file[0];
            file.erase(file.begin());

            //ajoute a la file la generation suivante issu de ce noeud
            for (int j=0; j<a->getNbFils(); ++j){
                file.push_back(a->getFils(j));
            }
            nbGeneration1 += a->getNbFils();

            //prend en compte les 'updates' de ce noeud
            nbUpdates += a->getUpdates();
        }

        niveau.push_back(kGeneration);
        niveau.push_back(nbGeneration0);
        niveau.push_back(nbUpdates);
        tab.push_back(niveau);
        niveau.clear();

        nbGeneration0 = nbGeneration1;
        nbGeneration1 = 0;
        kGeneration += 1;
        nbUpdates = 0;
    }

    for (int i=0; i<tab.size(); ++i){
        nbTotalNoeuds += tab[i][1];
        nbTotalUpdates += tab[i][2];
    }
}

void Arbre::afficheInfos() const{
    //initialisation
    vector<vector<int>> tab;
    int nbTotalNoeuds = 0;
    int nbTotalUpdates = 0;

    calculeInfos(nbTotalNoeuds, nbTotalUpdates, tab);

    cout << "Level      " << "Nodes      " << "Updates      " << "Updates per node" << endl;
    if ((nbTotalNoeuds > 0) && (nbTotalUpdates > 0)){
        for (int i=0; i<tab.size(); ++i){
            cout << tab[i][0] << "           " << tab[i][1] << "(" << tab[i][1]*100/nbTotalNoeuds << "%)   ";
            cout << tab[i][2] << "(" << tab[i][2]*100/nbTotalUpdates << "%)       ";
            cout << tab[i][2]/tab[i][1] << endl;
        }
    }
    else if ((nbTotalNoeuds == 0) && (nbTotalUpdates == 0)){
        for (int i=0; i<tab.size(); ++i){
            cout << tab[i][0] << "           " << tab[i][1] << "( - %)   ";
            cout << tab[i][2] << "( - %)       ";
            cout << tab[i][2]/tab[i][1] << endl;
        }
    }
    else if (nbTotalNoeuds == 0){
        for (int i=0; i<tab.size(); ++i){
            cout << tab[i][0] << "           " << tab[i][1] << "( - %)   ";
            cout << tab[i][2] << "(" << tab[i][2]*100/nbTotalUpdates << "%)       ";
            cout << tab[i][2]/tab[i][1] << endl;
        }
    }
    else if (nbTotalUpdates == 0){
        for (int i=0; i<tab.size(); ++i){
            cout << tab[i][0] << "           " << tab[i][1] << "(" << tab[i][1]*100/nbTotalNoeuds << "%)   ";
            cout << tab[i][2] << "( - %)       ";
            cout << tab[i][2]/tab[i][1] << endl;
        }
    }
}

//enregistre les infos de l'arbre dans un fichier csv

void Arbre::enregistreInfos(string nomFichier) const{
    //initialisation
    vector<vector<int>> tab;
    int nbTotalNoeuds = 0;
    int nbTotalUpdates = 0;

    calculeInfos(nbTotalNoeuds, nbTotalUpdates, tab);

    ofstream f;
    f.open(nomFichier + ".csv");

    f << "Level" << ";" << "Nodes" << ";" << "Updates" << ";" << "Updates per node" << ";" << "\n";

    if ((nbTotalNoeuds > 0) && (nbTotalUpdates > 0)){
        for (int i=0; i<tab.size(); ++i){
            f << tab[i][0] << ";" << tab[i][1] << " (" << tab[i][1]*100/nbTotalNoeuds << "%)" << ";" << \
                            tab[i][2] << " (" << tab[i][2]*100/nbTotalUpdates << "%)" << ";" << \
                            tab[i][2]/tab[i][1] << ";" << "\n";
        }
    }
    else if ((nbTotalNoeuds == 0) && (nbTotalUpdates == 0)){
        for (int i=0; i<tab.size(); ++i){
            f << tab[i][0] << ";" << tab[i][1] << " ( - %)" << ";" << \
                            tab[i][2] << " ( - %)" << ";" << \
                            tab[i][2]/tab[i][1] << ";" << "\n";
        }
    }
    else if (nbTotalNoeuds == 0){
        for (int i=0; i<tab.size(); ++i){
            f << tab[i][0] << ";" << tab[i][1] << " ( - %)" << ";" << \
                            tab[i][2] << " (" << tab[i][2]*100/nbTotalUpdates << "%)" << ";" << \
                            tab[i][2]/tab[i][1] << ";" << "\n";
        }
    }
    else if (nbTotalUpdates == 0){
        for (int i=0; i<tab.size(); ++i){
            f << tab[i][0] << ";" << tab[i][1] << " (" << tab[i][1]*100/nbTotalNoeuds << "%)" << ";" << \
                            tab[i][2] << " ( - %)" << ";" << \
                            tab[i][2]/tab[i][1] << ";" << "\n";
        }
    }

    f.close();
}



///---------------------Autres fonctions---------------------------

void uneConfigPiece1(int n1, int n2, int n3, int n4, int n5, int n6, int n7, Matrice* M){
    vector<int> config;
    config.push_back(1);
    config.push_back(n1 + 3);
    config.push_back(n2 + 3);
    config.push_back(n3 + 3);
    config.push_back(n4 + 3);
    config.push_back(n5 + 3);
    config.push_back(n6 + 3);
    config.push_back(n7 + 3);
    M->ajouteDerniereLigne(config);
}

void ajouteConfigPiece1(Matrice* M){
    uneConfigPiece1(1,2,3,4,8,12,16,M);
    uneConfigPiece1(4,8,12,16,15,14,13,M);
    uneConfigPiece1(16,15,14,13,9,5,1,M);
    uneConfigPiece1(13,9,5,1,2,3,4,M);
}

void uneConfigPiece2(int n1, int n2, int n3, int n4, int n5, int n6, Matrice* M){
    vector<int> config;
    config.push_back(2);
    config.push_back(n1 + 3);
    config.push_back(n2 + 3);
    config.push_back(n3 + 3);
    config.push_back(n4 + 3);
    config.push_back(n5 + 3);
    config.push_back(n6 + 3);
    M->ajouteDerniereLigne(config);
}

void ajouteConfigPiece2(Matrice* M){
    uneConfigPiece2(1,5,9,2,6,10,M);
    uneConfigPiece2(2,6,10,3,7,11,M);
    uneConfigPiece2(3,7,11,4,8,12,M);
    uneConfigPiece2(5,9,13,6,10,14,M);
    uneConfigPiece2(6,10,14,7,11,15,M);
    uneConfigPiece2(7,11,15,8,12,16,M);
    uneConfigPiece2(1,2,3,5,6,7,M);
    uneConfigPiece2(5,6,7,9,10,11,M);
    uneConfigPiece2(9,10,11,13,14,15,M);
    uneConfigPiece2(2,3,4,6,7,8,M);
    uneConfigPiece2(6,7,8,10,11,12,M);
    uneConfigPiece2(10,11,12,14,15,16,M);
}


void uneConfigPiece3(int a, int b, int c, Matrice* M){
    vector<int> config;
    config.push_back(3);
    config.push_back(a + 3);
    config.push_back(b + 3);
    config.push_back(c + 3);
    M->ajouteDerniereLigne(config);
}

void ajouteConfigPiece3(Matrice* M){
    uneConfigPiece3(1,5,9,M);
    uneConfigPiece3(2,6,10,M);
    uneConfigPiece3(3,7,11,M);
    uneConfigPiece3(4,8,12,M);

    uneConfigPiece3(5,9,13,M);
    uneConfigPiece3(6,10,14,M);
    uneConfigPiece3(7,11,15,M);
    uneConfigPiece3(8,12,16,M);

    uneConfigPiece3(1,2,3,M);
    uneConfigPiece3(5,6,7,M);
    uneConfigPiece3(9,10,11,M);
    uneConfigPiece3(13,14,15,M);

    uneConfigPiece3(2,3,4,M);
    uneConfigPiece3(6,7,8,M);
    uneConfigPiece3(10,11,12,M);
    uneConfigPiece3(14,15,16,M);
}





