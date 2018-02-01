#include<iostream>
using namespace std;


#include<cassert>

#include"piece.h"


///-------------------Classe Plateau-----------------

//constructeurs

Plateau::Plateau(){
    taille = 0;
    tab = 0;
}

Plateau::Plateau(int N){
    taille = N;
    tab = new int[N*N];
    for (int i=0; i<N*N; ++i){
        tab[i] = 1;
    }
}

Plateau::Plateau(int N, vector<int> casesVides){
    ///construit un plateau a partir de la liste des cases vacantes
    /// 'casesVides' contient les numeros des cases fixees
    taille = N;
    tab = new int[N*N];
    for (int i=0; i<N*N; ++i){
        tab[i] = 1;
    }
    for (int i=0; i<casesVides.size(); ++i){
        assert((casesVides[i] > 0) && (casesVides[i] <= N*N));
        tab[casesVides[i]-1] = 0;
    }
}

Plateau::Plateau(int N, int n1){
    ///construit un plateau de taille N avec la case n1 d'occupee
    assert((n1 > 0) && (n1 <= N*N));
    taille = N;
    tab = new int[taille*taille];
    for (int i=0; i<taille*taille; ++i){
        tab[i] = 1;
    }
    tab[n1-1] = 0;
}

//constructeur de copie

Plateau::Plateau(const Plateau &P){
    taille = P.taille;
    tab = new int[taille*taille];
    for (int i=0; i<taille*taille; ++i){
        tab[i] = P.tab[i];
    }
}

//accesseurs

int Plateau::operator ()(int i, int j) const{
    ///retourne l'etat de la case en ligne numero i et colonne numero j
    assert((i > 0) && (i <= taille));
    assert((j > 0) && (j <= taille));
    return tab[(i-1)*taille + (j-1)];
}

int Plateau::operator ()(int numCase) const{
    ///retourne l'etat de la case numero 'numCase'
    int j = (numCase-1)%taille + 1;
    int i = (numCase-j)/taille + 1;
    return operator ()(i,j);
}

int Plateau::getTaille() const{
    return taille;
}

int Plateau::getNbCasesFixees() const{
    int S = 0;
    for (int i=0; i<taille*taille; ++i){
        if (tab[i] == 0){
            S += 1;
        }
    }
    return S;
}

//destructeur

Plateau::~Plateau(){
    delete[] tab;
}


///------------------------------Classe Piece----------------------------

//constructeurs

Piece::Piece(){
    hauteur = 0;
    largeur = 0;
    tab = 0;
}

Piece::Piece(int newHauteur, int newLargeur, int *config, Color c){
    hauteur = newHauteur;
    largeur = newLargeur;
    tab = new int[hauteur*largeur];
    for (int i=0; i<hauteur*largeur; ++i){
        tab[i] = config[i];
    }
    col = c;
}

Piece::Piece(int newHauteur, int newLargeur, vector<int> config, Color c){
    assert(config.size() == newHauteur*newLargeur);
    hauteur = newHauteur;
    largeur = newLargeur;
    tab = new int[hauteur*largeur];
    for (int i=0; i<hauteur*largeur; ++i){
        tab[i] = config[i];
    }
    col = c;
}

//constructeur de copie

Piece::Piece(const Piece &pi){
    largeur = pi.largeur;
    hauteur = pi.hauteur;
    tab = new int[largeur*hauteur];
    for (int i=0; i<largeur*hauteur; ++i){
        tab[i] = pi.tab[i];
    }
}

//destructeur

Piece::~Piece(){
    delete[] tab;
}

//accesseurs

int Piece::operator ()(int i, int j) const{
    assert((i > 0) && (i <= hauteur) && (j > 0) && (j <= largeur));
    return tab[(i-1)*largeur + j-1];
}

int Piece::getHauteur() const{
    return hauteur;
}

int Piece::getLargeur() const{
    return largeur;
}

Color Piece::getCouleur() const{
    return col;
}

//operateurs

bool Piece::compare(Piece &p) const{
    bool sontEgales = true;
    sontEgales = ((hauteur == p.hauteur) && (largeur == p.largeur));

    int i = 0;
    while ((sontEgales) && (i < largeur*hauteur)){
        sontEgales = (tab[i] == p.tab[i]);
        i += 1;
    }
    return sontEgales;
}

const Piece &Piece::operator =(const Piece &p){
    hauteur = p.hauteur;
    largeur = p.largeur;
    delete[] tab;
    tab = new int[largeur*hauteur];
    for (int i=0; i<largeur*hauteur; ++i){
        tab[i] = p.tab[i];
    }
    col = p.col;
}

//rotation horaire

void Piece::rotationHoraire(){
    int newHauteur = largeur;
    int newLargeur = hauteur;
    int* newTab = new int[hauteur*largeur];
    for (int j=0; j<newLargeur; ++j){
        for (int i=0; i<newHauteur; ++i){
            newTab[i*newLargeur + j] = tab[(hauteur - j-1)*largeur + i];
        }
    }
    delete[] tab;
    tab = newTab;
    hauteur = newHauteur;
    largeur = newLargeur;
}

//calcul de toutes les configurations possibles dans le plateau

vector<vector<int> > Piece::calculeConfigurations(Plateau* plat) const{
    vector<vector<int> > V;
    vector<int> v;
    bool valide = true;
    int taillePlateau = plat->getTaille();
    for (int dj=0; dj<(taillePlateau-largeur+1); ++dj){
        for (int di=0; di<(taillePlateau-hauteur+1); ++di){
            for (int j=0; j<largeur; ++j){
                for (int i=0; i<hauteur; ++i){
                    if (tab[i*largeur + j] == 1){
                        valide = ((plat->operator ()(i+1+di, j+1+dj) == 1) && (valide));
                        v.push_back((i+di)*taillePlateau + (j+dj) + 1);
                    }
                }
            }
            if (valide){
                V.push_back(v);
            }
            valide = true;
            v.clear();
        }
    }
    return V;
}

//affichage

void Piece::display() const{
    cout << endl;
    for (int i=0; i<hauteur; ++i){
        for (int j=0; j<largeur; ++j){
            cout << tab[i*largeur + j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}



///------------------------Classe jeu-------------------------

//constructeurs

Jeu::Jeu(){
    plat = 0;
    taillePlateau = 0;
    nbPieces = 0;
    nbCasesFixees = 0;
}

Jeu::Jeu(Plateau *P){
    plat = P;
    taillePlateau = P->getTaille();
    nbPieces = 0;
    nbCasesFixees = 0;
    for (int i=1; i<(taillePlateau + 1); ++i){
        for (int j=1; j<(taillePlateau + 1); ++j){
            if (plat->operator ()(i,j) == 0){
                nbCasesFixees += 1;
            }
        }
    }
}

//accesseurs

Plateau* Jeu::getPlateau() const{
    return plat;
}

Piece* Jeu::getPiece(int num) const{
    assert((num > 0) && (num <= pcs.size()));
    return pcs[num-1];
}

vector<int> Jeu::getPositionPiece(int numPiece) const{
    assert((numPiece > 0) && (numPiece <= pcs.size()));
    return positions[numPiece-1];
}

int Jeu::getNbPieces() const{
    return nbPieces;
}

int Jeu::getNbCasesLibres() const{
    return (taillePlateau*taillePlateau - nbCasesFixees);
}

int Jeu::getNbCases() const{
    return taillePlateau*taillePlateau;
}

//mutateurs

void Jeu::ajoutePiece(Piece *p, int xi, int xj){
    pcs.push_back(p);
    vector<int> pos;
    pos.push_back(xi);
    pos.push_back(xj);
    positions.push_back(pos);
    nbPieces += 1;
}

void Jeu::setPlateau(Plateau *P){
    plat = P;
    taillePlateau = P->getTaille();
    nbCasesFixees = P->getNbCasesFixees();
}

///--------------------Autres fonctions--------------------

void setPointeur6(int* a, int x1, int x2, int x3, int x4, int x5, int x6){
    a[0] = x1;
    a[1] = x2;
    a[2] = x3;
    a[3] = x4;
    a[4] = x5;
    a[5] = x6;
}

void setPointeur9(int* a, int x1, int x2, int x3, int x4, int x5, int x6, int x7, int x8, int x9){
    setPointeur6(a, x1, x2, x3, x4, x5, x6);
    a[6] = x7;
    a[7] = x8;
    a[8] = x9;
}

vector<vector<int> > calculeToutesConfig(Piece pi, Plateau* plat){
    //calcule les 4 pieces possibles selon les 4 orientations
    vector<Piece> quatreOrientations;
    quatreOrientations.push_back(pi);
    pi.rotationHoraire();
    quatreOrientations.push_back(pi);
    pi.rotationHoraire();
    quatreOrientations.push_back(pi);
    pi.rotationHoraire();
    quatreOrientations.push_back(pi);

    //ajoute les configurations seulement si elles sont différentes
    vector<vector<int> > S = quatreOrientations[0].calculeConfigurations(plat);
    vector<vector<int> > s;

    //examine les orientations i
    bool configDifferente;
    for (int i=1; i<4; ++i){
        //compare aux orientations j precedentes
        configDifferente = true;
        for (int j=0; j<i; ++j){
            configDifferente = (configDifferente && (!quatreOrientations[i].compare(quatreOrientations[j])) );
        }
        if (configDifferente){
           s = quatreOrientations[i].calculeConfigurations(plat);
           for (int k=0; k<s.size(); ++k){
               S.push_back(s[k]);
           }
        }
    }
    return S;
}

vector<vector<int> > calculeToutesConfig(Piece* pi, Plateau* plat){
    Piece p(*pi);

    //calcule les 4 pieces possibles selon les 4 orientations
    vector<Piece> quatreOrientations;
    quatreOrientations.push_back(p);
    p.rotationHoraire();
    quatreOrientations.push_back(p);
    p.rotationHoraire();
    quatreOrientations.push_back(p);
    p.rotationHoraire();
    quatreOrientations.push_back(p);

    //ajoute les configurations seulement si elles sont différentes
    vector<vector<int> > S = quatreOrientations[0].calculeConfigurations(plat);
    vector<vector<int> > s;

    //examine les orientations i
    bool configDifferente;
    for (int i=1; i<4; ++i){
        //compare aux orientations j precedentes
        configDifferente = true;
        for (int j=0; j<i; ++j){
            configDifferente = (configDifferente && (!quatreOrientations[i].compare(quatreOrientations[j])) );
        }
        if (configDifferente){
           s = quatreOrientations[i].calculeConfigurations(plat);
           for (int k=0; k<s.size(); ++k){
               S.push_back(s[k]);
           }
        }
    }
    return S;
}







