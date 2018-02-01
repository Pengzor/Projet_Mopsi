#include<iostream>
using namespace std;

#include<vector>
#include<cassert>

#include"test.h"
#include"matrice.h"
#include"piece.h"
#include"algo.h"
#include"graphique.h"


void testPetitPuzzle(){
    ///3 pieces, plateau 4x4
    Matrice* M = new Matrice(3, 16);

    ajouteConfigPiece1(M);
    ajouteConfigPiece2(M);
    ajouteConfigPiece3(M);

    cout << "Matrice des configurations possibles : " << endl;
    M->displayMatrice();

    vector<vector<Noeud*> > Solutions;
    vector<Noeud*> sp;
    rechercheSol(M, Solutions, sp, "");

    displaySolutions(Solutions, M);
    //M->displayMatrice();
}

void testRotationPiece(){
    cout << "Rotations horaires d'une piece : " << endl;
    int* a = new int[6];
    for (int i=0; i<6; ++i){
        a[i] = 1;
    }
    a[4] = 0;
    Piece p1(2, 3, a, BLUE);
    p1.display();

    p1.rotationHoraire();
    p1.display();

    p1.rotationHoraire();
    p1.display();

    p1.rotationHoraire();
    p1.display();

    delete[] a;
}

void testAffichagePlateau(){
    int z = 4;
    int w = 200;
    int h = 200;

    openWindow(w*z, h*z);

    Plateau * P = new Plateau(5, 7);
    affichePlateau(P,h,w,z);

    int* a = new int[6];
    setPointeur6(a, 1, 1, 1, 0, 1, 0);
    Piece p1(3, 2, a,BLUE);

    a[3] = 1;
    Piece p2(2, 2, a,BLACK);

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

    affichePiece(p1,P,1,1,h,w,z);
    affichePiece(p2,P,4,1,h,w,z);
    affichePiece(p3,P,4,3,h,w,z);
    affichePiece(p4,P,2,2,h,w,z);
    affichePiece(p5,P,1,3,h,w,z);
    affichePiece(p6,P,4,4,h,w,z);
    affichePiece(p7,P,5,4,h,w,z);

    endGraphics();


    delete P;
}

void testCalculConfig(){
    int z = 4;
    int w = 200;
    int h = 200;

    openWindow(w*z, h*z);

    Plateau * P = new Plateau(5,7);
    affichePlateau(P,h,w,z);

    int* a = new int[6];
    setPointeur6(a, 1, 1, 1, 0, 1, 0);
    Piece p1(3, 2, a, BLUE);
    delete[] a;

    afficheToutesConfig(p1,P,h,w,z);

    endGraphics();
}

void testEcriture(){
    int nbPcs = 3;
    int nbCs = 16;
    int Nplateau = 4;
    Matrice* M = new Matrice(nbPcs, nbCs);

    ajouteConfigPiece1(M);
    ajouteConfigPiece2(M);
    ajouteConfigPiece3(M);

    M->displayMatrice();

    vector<vector<Noeud*> > Solutions;
    vector<Noeud*> sp;
    rechercheSol(M, Solutions, sp, "");

    displaySolutions(Solutions, M);

    enregistreResultat("testEcriture.csv", Solutions, nbPcs, nbCs);
}

void testChargementDonnees(){
    Jeu g;
    lectureDonnees("puzzleReel.txt", g);
}

void testAffichagePlateauMarges(){
    Plateau* P = new Plateau(7, 10);
    int z = 4;
    int w = 200;
    int h = 200;

    openWindow(w*z, h*z);
    affichePlateau(P, h, w, z);
    endGraphics();
}


