#include"ecriture.h"



void enregistreResultat(string nomFichier, vector<vector<Noeud*> > &Solutions, int nbPieces, int taillePlateau){
    ofstream f;
    f.open(nomFichier);

    vector<Noeud*> uneSol;
    Noeud* node;
    Noeud* ligne;
    int numColonne;
    int Ncolonnes = nbPieces + taillePlateau;

    f << nbPieces << ";" << taillePlateau << ";" << Solutions.size() << ";" << '\n';
    for (int i=0; i<Solutions.size(); ++i){
        uneSol = Solutions[i];
        f << '\n';
        for (int j=0; j<uneSol.size(); ++j){
            ligne = uneSol[j];
            node = ligne->getDroite();
            numColonne = 0;
            while (node != ligne){
                for (int k=0; k<node->getCol()->getId() - numColonne - 1; ++k){
                    f << 0 << ";";
                }
                f << 1 << ";";
                numColonne = node->getCol()->getId();
                node = node->getDroite();
            }
            for (int k=0; k<Ncolonnes-numColonne; ++k){
                f << 0 << ";";
            }
            f << '\n';
        }
    }

    f.close();
}

vector<int> lectureLigneInt(string L){
    string coma = ";";
    string s;
    L += ";";
    vector<int> liste;
    for (int k=0; k<L.size(); ++k){
        if (L[k] == coma[0]){
            liste.push_back(stod(s));
            s = "";
        }
        else{
            s += L[k];
        }
    }
    return liste;
}

void lectureDonnees(string nomFichier, Jeu& game){
    ifstream f;
    f.open(nomFichier);
    string ligne;

    //creation du plateau de jeu
    f >> ligne;
    int taille = stod(ligne);
    //cout << taille << endl;

    f >> ligne;
    int nbCasesFixes = stod(ligne);
    //cout << nbCasesFixes << endl;

    f >> ligne;
    vector<int> listeCasesFixees = lectureLigneInt(ligne);
    for (int i=0; i<listeCasesFixees.size(); ++i){
        //cout << listeCasesFixees[i] << " ";
    }
    //cout << endl;

    Plateau* plat = new Plateau(taille, listeCasesFixees);

    game.setPlateau(plat);

    //construction des pieces

    f >> ligne;
    int nbPieces = stod(ligne);
    //cout << nbPieces << endl;

    vector<int> dimensions;
    vector<int> casesPiece;
    vector<int> v;
    Color c;

    for (int i=0; i<nbPieces; ++i){
        dimensions.clear();
        casesPiece.clear();
        f >> ligne;
        dimensions = lectureLigneInt(ligne);
        //cout << dimensions[0] << " " << dimensions[1] << endl;
        for (int j=0; j<dimensions[0]; ++j){
            f >> ligne;
            v.clear();
            v = lectureLigneInt(ligne);
            //cout << "   ";
            for (int k=0; k<v.size(); ++k){
                //cout << v[k] << " ";
                casesPiece.push_back(v[k]);
            }
            //cout << endl;
        }
        c = Color(rand()%256, rand()%256, rand()%256);
        Piece* p = new Piece(dimensions[0], dimensions[1], casesPiece, c);
        game.ajoutePiece(p, 1, 1);
    }


    f.close();
}
