#include<iostream>
using namespace std;



#include"puzzles.h"


///---------------------Fonctions de construction du puzzle

Matrice* construitMatrice(Jeu &game){
    //contruit la matrice
    Plateau* P = game.getPlateau();
    int nbPcs = game.getNbPieces();
    Matrice* mat = new Matrice(game);
    mat->displayColonnesId();

    //ajoute les lignes, correspondant à chaque piece
    vector<vector<int> > configsPiece;
    vector<int> s;
    vector<int> ligne;

    for (int k=0; k<nbPcs; ++k){
        //cout << "piece " << k+1 << endl;
        configsPiece = calculeToutesConfig(game.getPiece(k+1), P);
        for (int j=0; j<configsPiece.size(); ++j){
            s = configsPiece[j];
            //ajoute numero de piece
            ligne.push_back(k+1);
            //ajoute numeros de colonnes
            for (int i=0; i<s.size(); ++i){
                ligne.push_back(nbPcs + s[i]);
            }
            //cout << "fait" << endl;
            mat->ajouteDerniereLigne(ligne);
            ligne.clear();
        }
    }
    return mat;
}


///-----------------Puzzle n°1--------------------
///  plateau 5x5


void puzzle1(){
    //plateau
    Plateau* P = new Plateau(5, 7);

    //pieces

    int* a = new int[6];
    setPointeur6(a, 1, 1, 1, 0, 1, 0);
    Piece p1(3, 2, a, BLUE);

    a[3] = 1;
    Piece p2(2, 2, a, BLACK);

    Piece p3(2, 1, a, RED);

    a[0] = 0;
    Piece p4(2, 2, a, GREEN);
    delete[] a;

    a = new int[9];
    setPointeur9(a,1,1,1,0,1,1,0,1,1);
    Piece p5(3,3,a,YELLOW);

    Color c(12,154,89);
    setPointeur6(a,1,1,0,1,0,0);
    Piece p6(2,2,a,c);

    Color c2(56,0,169);
    Piece p7(1,1,a,c2);

    int z = 4;
    int w = 200;
    int h = 200;

    openWindow(w*z, h*z);

    //jeu

    Jeu game(P);
    game.ajoutePiece(&p1,1,1);
    game.ajoutePiece(&p2,4,1);
    game.ajoutePiece(&p3,4,3);
    game.ajoutePiece(&p4,2,2);
    game.ajoutePiece(&p5,1,3);
    game.ajoutePiece(&p6,4,4);
    game.ajoutePiece(&p7,5,4);
    afficheJeu(game, h, w, z);
    click();
    clearWindow();

    //construit la matrice
    Matrice* mat = construitMatrice(game);
    //mat->displayMatrice();

    //calcule les solutions du puzzle
    vector<vector<Noeud*> > Solutions;
    vector<Noeud*> sp;
    rechercheSol(mat, Solutions, sp, "");
    cout << "solutions : " << Solutions.size() << endl << endl;
    //enregistreResultat("puzzle1.csv", Solutions, 7, 5);

    //affiche toutes les solutions

    afficheSolutionsAlgo(game, Solutions, h, w, z);

    endGraphics();

    delete P;
}

void puzzle2(){
    //plateau
    Plateau* P = new Plateau(5, 7);

    //pieces

    int* a = new int[6];
    setPointeur6(a, 1, 1, 1, 0, 1, 0);
    Piece p1(3, 2, a, BLUE);

    a[3] = 1;
    Piece p2(2, 2, a, BLACK);

    Piece p3(2, 1, a, RED);

    a[0] = 0;
    Piece p4(2, 2, a, GREEN);
    delete[] a;

    a = new int[9];
    setPointeur9(a,1,1,1,0,1,1,0,1,1);
    Piece p5(3,3,a,YELLOW);

    Color c(12,154,89);
    setPointeur6(a,1,1,0,1,0,0);
    Piece p6(2,2,a,c);

    Color c2(56,0,169);
    Piece p7(1,1,a,c2);

    int z = 4;
    int w = 200;
    int h = 200;

    openWindow(w*z, h*z);

    //jeu

    Jeu game(P);
    game.ajoutePiece(&p1,1,1);
    game.ajoutePiece(&p2,4,1);
    game.ajoutePiece(&p3,4,3);
    game.ajoutePiece(&p4,2,2);
    game.ajoutePiece(&p5,1,3);
    game.ajoutePiece(&p6,4,4);
    game.ajoutePiece(&p7,5,4);
    afficheJeu(game, h, w, z);
    click();
    clearWindow();

    //construit la matrice
    Matrice* mat = construitMatrice(game);
    //mat->displayMatrice();

    //calcule les solutions du puzzle
    vector<vector<Noeud*> > Solutions;
    vector<Noeud*> sp;
    rechercheSol2(mat, game, Solutions, sp, "", h, w, z);

    endGraphics();
}

void puzzle3(){
    Jeu game;
    lectureDonnees("puzzleReel.txt", game);
    Matrice* mat = construitMatrice(game);
    //mat->displayMatrice();

    //calcule les solutions du puzzle
    vector<vector<Noeud*> > Solutions;
    vector<Noeud*> sp;
    rechercheSol(mat, Solutions, sp, "");

    //affiche toutes les solutions
    int z = 4;
    int w = 200;
    int h = 200;

    openWindow(w*z, h*z);
    afficheSolutionsAlgo(game, Solutions, h, w, z);
    endGraphics();

    //sauvegarde
    enregistreResultat("puzzle3.csv", Solutions, game.getNbPieces(), game.getNbCasesLibres());
}

void puzzle4(){
    Jeu game;
    lectureDonnees("puzzleReel.txt", game);
    Matrice* mat = construitMatrice(game);
    //mat->displayMatrice();

    //calcule les solutions du puzzle
    vector<vector<Noeud*> > Solutions;
    vector<Noeud*> sp;
    int compt = 0;
    double tempsDebut;
    double tempsFin;
    tempsDebut = time(0);
    rechercheSol3(mat, Solutions, sp, "", compt);
    tempsFin = time(0);

    cout << endl << Solutions.size() << " solutions !" << endl << endl;
    cout << compt << " explorations" << endl;
    cout << "temps de calcul : " << tempsFin - tempsDebut << " secondes" << endl;

    //affiche toutes les solutions
    int z = 4;
    int w = 200;
    int h = 200;

    openWindow(w*z, h*z);
    afficheSolutionsAlgo(game, Solutions, h, w, z);
    endGraphics();

    //sauvegarde
    enregistreResultat("puzzle4.csv", Solutions, game.getNbPieces(), game.getNbCasesLibres());
}

void puzzle5(){
    //plateau
    Plateau* P = new Plateau(5, 7);

    //pieces

    int* a = new int[6];
    setPointeur6(a, 1, 1, 1, 0, 1, 0);
    Piece p1(3, 2, a, BLUE);

    a[3] = 1;
    Piece p2(2, 2, a, BLACK);

    Piece p3(2, 1, a, RED);

    a[0] = 0;
    Piece p4(2, 2, a, GREEN);
    delete[] a;

    a = new int[9];
    setPointeur9(a,1,1,1,0,1,1,0,1,1);
    Piece p5(3,3,a,YELLOW);

    Color c(12,154,89);
    setPointeur6(a,1,1,0,1,0,0);
    Piece p6(2,2,a,c);

    Color c2(56,0,169);
    Piece p7(1,1,a,c2);

    int z = 4;
    int w = 200;
    int h = 200;

    openWindow(w*z, h*z);

    //jeu

    Jeu game(P);
    game.ajoutePiece(&p1,1,1);
    game.ajoutePiece(&p2,4,1);
    game.ajoutePiece(&p3,4,3);
    game.ajoutePiece(&p4,2,2);
    game.ajoutePiece(&p5,1,3);
    game.ajoutePiece(&p6,4,4);
    game.ajoutePiece(&p7,5,4);
    afficheJeu(game, h, w, z);
    click();
    clearWindow();

    //construit la matrice
    Matrice* mat = construitMatrice(game);
    //mat->displayMatrice();

    //calcule les solutions du puzzle
    vector<vector<Noeud*> > Solutions;
    vector<Noeud*> sp;
    Arbre* racine = new Arbre(0, 0);
    rechercheSol5(mat, Solutions, sp, "", racine);
    cout << "solutions : " << Solutions.size() << endl << endl;
    //enregistreResultat("puzzle1.csv", Solutions, 7, 5);

    //affiche toutes les solutions

    //afficheSolutionsAlgo(game, Solutions, h, w, z);
    racine->afficheInfos();
    endGraphics();

    delete P;
    delete racine;
}

void puzzle6(){
    //plateau
    Plateau* P = new Plateau(5, 7);

    //pieces

    int* a = new int[6];
    setPointeur6(a, 1, 1, 1, 0, 1, 0);
    Piece p1(3, 2, a, BLUE);

    a[3] = 1;
    Piece p2(2, 2, a, BLACK);

    Piece p3(2, 1, a, RED);

    a[0] = 0;
    Piece p4(2, 2, a, GREEN);
    delete[] a;

    a = new int[9];
    setPointeur9(a,1,1,1,0,1,1,0,1,1);
    Piece p5(3,3,a,YELLOW);

    Color c(12,154,89);
    setPointeur6(a,1,1,0,1,0,0);
    Piece p6(2,2,a,c);

    Color c2(56,0,169);
    Piece p7(1,1,a,c2);

    int z = 4;
    int w = 200;
    int h = 200;

    openWindow(w*z, h*z);

    //jeu

    Jeu game(P);
    game.ajoutePiece(&p1,1,1);
    game.ajoutePiece(&p2,4,1);
    game.ajoutePiece(&p3,4,3);
    game.ajoutePiece(&p4,2,2);
    game.ajoutePiece(&p5,1,3);
    game.ajoutePiece(&p6,4,4);
    game.ajoutePiece(&p7,5,4);
    afficheJeu(game, h, w, z);
    click();
    clearWindow();

    //construit la matrice
    Matrice* mat = construitMatrice(game);
    //mat->displayMatrice();

    //calcule les solutions du puzzle
    vector<vector<Noeud*> > Solutions;
    vector<Noeud*> sp;
    Arbre* racine = new Arbre(0, 0);
    rechercheSol6(mat, Solutions, sp, "", racine);
    cout << "solutions : " << Solutions.size() << endl << endl;
    //enregistreResultat("puzzle1.csv", Solutions, 7, 5);

    //affiche toutes les solutions

    //afficheSolutionsAlgo(game, Solutions, h, w, z);
    racine->afficheInfos();
    endGraphics();

    delete P;
    delete racine;
}
