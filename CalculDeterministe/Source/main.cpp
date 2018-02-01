// Imagine++ project
// Project:  Nouveau
// Author:   Matthieu Roux

#include <Imagine/Graphics.h>
using namespace Imagine;

#include<iostream>
using namespace std;

#include<vector>

#include"matrice.h"
#include"piece.h"
#include"test.h"
#include"algo.h"
#include"puzzles.h"

////////////////////////////////////////////////

void interface(){

    ///---lit le fichier contenant les informations globales---
    Jeu game;
    lectureDonnees("DonneesPuzzle.txt", game);
    Matrice* mat = construitMatrice(game);

    ///---calcule les solutions---
    //calcule les solutions du puzzle
    vector<vector<Noeud*> > Solutions;
    vector<Noeud*> sp;
    Arbre* racine = new Arbre(0, 0);
    rechercheSol6(mat, Solutions, sp, "", racine);

    /*
    cout << endl << Solutions.size() << " solutions !" << endl << endl;
    racine->afficheInfos();
    */

    ///---sauvegarde les résultats
    //sauvegarde
    enregistreResultat("ResultatPuzzle.csv", Solutions, game.getNbPieces(), game.getNbCases());

    ///---sauvegarde les donnees de performances
    racine->enregistreInfos("ResultatInfos");
}


/////////////////////////////////////////////
int main()
{

    //testPetitPuzzle();

    //testRotationPiece();

    //testAffichagePlateau();

    //testCalculConfig();

    //puzzle1();

    //testEcriture();

    //puzzle2();

    //testChargementDonnees();

    //puzzle3();

    //puzzle4();

    //testAffichagePlateauMarges();

    //puzzle5();
    //cout << endl << endl;
    //puzzle6();



    interface();


	return 0;
}
