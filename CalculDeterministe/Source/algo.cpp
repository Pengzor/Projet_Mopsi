#include<iostream>
using namespace std;

#include<vector>

#include"algo.h"



int rechercheSol(Matrice* M, vector<vector<Noeud*> > &Solutions, vector<Noeud*> &solPartielle, string indent){
    if ((M->getNbLignes() == 0) && (M->getNbColonnes()==0)){
        Solutions.push_back(solPartielle);
        return 0;
    }
    else if ((M->getNbColonnes() == 0) || (M->getNbLignes() == 0)){
        return 0;
    }
    else{
        Noeud* Mh = M->getHeaderMatrice();

        //choix d'une colonne : aveugle au debut
        Noeud* c = Mh->getDroite();

        //parcours l'ensemble des lignes
        Noeud* r = Mh->getBas();
        while (r != Mh){
            if (M->get(r,c) == 1){
                //memoire pour le backtracking
                vector<Noeud*> memoire;

                //ajoute r a la solution partielle, et l'efface de la matrice
                solPartielle.push_back(r);
                M->effaceLigne(r);
                memoire.push_back(r);
                //cout << indent << r->getId() << endl;

                //parcours l'ensemble des colonnes
                Noeud* cj = Mh->getDroite();
                while (cj != Mh){
                    if (M->get(r,cj) == 1){
                        //parcours les lignes
                        Noeud* li = Mh->getBas();
                        while (li != Mh){
                            if (M->get(li,cj) == 1){
                                //efface ligne li
                                M->effaceLigne(li);
                                memoire.push_back(li);
                            }
                            li = li->getBas();
                        }

                        //efface colonne cj
                        M->effaceColonne(cj);
                        memoire.push_back(cj);
                    }
                    cj = cj->getDroite();
                }

                //on appelle l'algorithme recursivement sur la matrice reduite
                rechercheSol(M, Solutions, solPartielle, indent + "   ");

                //backtracking
                solPartielle.pop_back();
                Noeud* depile;
                for (int i=memoire.size(); i>0; --i){
                    depile = memoire[i-1];
                    if (depile->getValeur() == -1){
                        M->restaureColonne(depile);
                    }
                    else if (depile->getValeur() == -2){
                        M->restaureLigne(depile);
                    }
                    else{cerr << "Error !" << endl;}
                }
            }
            r = r->getBas();
        }
        return 0;
    }
}

void displaySolutions(vector<vector<Noeud*> > &S, Matrice* M){
    cout << endl << "Affichage des solutions : " << endl;
    vector<Noeud*> s;
    for (int i=0; i<S.size(); ++i){
        s = S[i];
        for (int j=0; j<s.size(); ++j){
            M->displayLigne(s[j]);
        }
        cout << endl;
    }
}

void affichageExploration(Jeu& game, vector<Noeud*> sp, int h, int w, int z){
    Plateau* plat = game.getPlateau();
    Noeud* lig;
    Noeud* n;
    Piece* piec;
    //affichage graphique de l'exploration
    noRefreshBegin();
    clearWindow();
    affichePlateau(plat, h, w, z);
    for (int i=0; i<sp.size(); ++i){
        lig = sp[i];
        n = lig->getDroite();
        piec = game.getPiece(n->getCol()->getId());
        n = n->getDroite();
        while (n != lig){
            afficheCase(n->getCol()->getId() - game.getNbPieces(), plat->getTaille(), h, w, z, piec->getCouleur());
            n = n->getDroite();
        }
    }
    noRefreshEnd();
    milliSleep(200);
}

int rechercheSol2(Matrice* M, Jeu& game, vector<vector<Noeud*> > &Solutions, vector<Noeud*> &solPartielle, string indent, int h, int w, int z){
    if ((M->getNbLignes() == 0) && (M->getNbColonnes()==0)){
        Solutions.push_back(solPartielle);
        return 0;
    }
    else if ((M->getNbColonnes() == 0) || (M->getNbLignes() == 0)){
        return 0;
    }
    else{
        Noeud* Mh = M->getHeaderMatrice();

        //choix d'une colonne : aveugle au debut
        Noeud* c = Mh->getDroite();

        //parcours l'ensemble des lignes
        Noeud* r = Mh->getBas();
        while (r != Mh){
            if (M->get(r,c) == 1){
                //memoire pour le backtracking
                vector<Noeud*> memoire;

                //ajoute r a la solution partielle, et l'efface de la matrice
                solPartielle.push_back(r);
                affichageExploration(game, solPartielle, h, w, z);
                M->effaceLigne(r);
                memoire.push_back(r);
                //cout << indent << r->getId() << endl;

                //parcours l'ensemble des colonnes
                Noeud* cj = Mh->getDroite();
                while (cj != Mh){
                    if (M->get(r,cj) == 1){
                        //parcours les lignes
                        Noeud* li = Mh->getBas();
                        while (li != Mh){
                            if (M->get(li,cj) == 1){
                                //efface ligne li
                                M->effaceLigne(li);
                                memoire.push_back(li);
                            }
                            li = li->getBas();
                        }

                        //efface colonne cj
                        M->effaceColonne(cj);
                        memoire.push_back(cj);
                    }
                    cj = cj->getDroite();
                }

                //on appelle l'algorithme recursivement sur la matrice reduite
                rechercheSol2(M, game, Solutions, solPartielle, indent + "   ", h, w, z);

                //backtracking
                solPartielle.pop_back();
                affichageExploration(game, solPartielle, h, w, z);
                Noeud* depile;
                for (int i=memoire.size(); i>0; --i){
                    depile = memoire[i-1];
                    if (depile->getValeur() == -1){
                        M->restaureColonne(depile);
                    }
                    else if (depile->getValeur() == -2){
                        M->restaureLigne(depile);
                    }
                    else{cerr << "Error !" << endl;}
                }
            }
            r = r->getBas();
        }
        return 0;
    }
}

int rechercheSol3(Matrice* M, vector<vector<Noeud*> > &Solutions, vector<Noeud*> &solPartielle, string indent, int &compt){
    ///on introduit un compteur d'itérations et une première technique d'optimisation
    compt += 1;
    if ((M->getNbLignes() == 0) && (M->getNbColonnes()==0)){
        Solutions.push_back(solPartielle);
        return 0;
    }
    else if ((M->getNbColonnes() == 0) || (M->getNbLignes() == 0)){
        return 0;
    }
    else{
        Noeud* Mh = M->getHeaderMatrice();

        //choix d'une colonne : celle qui possede le plus de 1
        Noeud* c = M->getColonneMin();

        //parcours l'ensemble des lignes
        Noeud* r = Mh->getBas();
        while (r != Mh){
            if (M->get(r,c) == 1){
                //memoire pour le backtracking
                vector<Noeud*> memoire;

                //ajoute r a la solution partielle, et l'efface de la matrice
                solPartielle.push_back(r);
                M->effaceLigne(r);
                memoire.push_back(r);
                //cout << indent << r->getId() << endl;

                //parcours l'ensemble des colonnes
                Noeud* cj = Mh->getDroite();
                while (cj != Mh){
                    if (M->get(r,cj) == 1){
                        //parcours les lignes
                        Noeud* li = Mh->getBas();
                        while (li != Mh){
                            if (M->get(li,cj) == 1){
                                //efface ligne li
                                M->effaceLigne(li);
                                memoire.push_back(li);
                            }
                            li = li->getBas();
                        }

                        //efface colonne cj
                        M->effaceColonne(cj);
                        memoire.push_back(cj);
                    }
                    cj = cj->getDroite();
                }

                //on appelle l'algorithme recursivement sur la matrice reduite
                rechercheSol3(M, Solutions, solPartielle, indent + "   ", compt);

                //backtracking
                solPartielle.pop_back();
                Noeud* depile;
                for (int i=memoire.size(); i>0; --i){
                    depile = memoire[i-1];
                    if (depile->getValeur() == -1){
                        M->restaureColonne(depile);
                    }
                    else if (depile->getValeur() == -2){
                        M->restaureLigne(depile);
                    }
                    else{cerr << "Error !" << endl;}
                }
            }
            r = r->getBas();
        }
        return 0;
    }
}

int rechercheSol5(Matrice* M, vector<vector<Noeud*> > &Solutions, vector<Noeud*> &solPartielle, string indent, Arbre* ArbreExploration){
    ///quantifier le nombre d'operation efectuees dans l'arbre d'exploration
    if ((M->getNbLignes() == 0) && (M->getNbColonnes()==0)){
        Solutions.push_back(solPartielle);
        return 0;
    }
    else if ((M->getNbColonnes() == 0) || (M->getNbLignes() == 0)){
        return 0;
    }
    else{
        Noeud* Mh = M->getHeaderMatrice();
        int nbUpdates = 0;

        //choix d'une colonne : aveugle au debut
        Noeud* c = Mh->getDroite();

        //parcours l'ensemble des lignes
        Noeud* r = Mh->getBas();
        while (r != Mh){
            if (M->get(r,c) == 1){
                //memoire pour le backtracking
                vector<Noeud*> memoire;

                //nombre de mises a jour necessaires au niveau de ce noeud de l'arbre d'exploration
                nbUpdates = 0;

                //ajoute r a la solution partielle, et l'efface de la matrice
                solPartielle.push_back(r);
                M->effaceLigne(r);
                nbUpdates += 1;
                memoire.push_back(r);
                //cout << indent << r->getId() << endl;

                //parcours l'ensemble des colonnes
                Noeud* cj = Mh->getDroite();
                while (cj != Mh){
                    if (M->get(r,cj) == 1){
                        //parcours les lignes
                        Noeud* li = Mh->getBas();
                        while (li != Mh){
                            if (M->get(li,cj) == 1){
                                //efface ligne li
                                M->effaceLigne(li);
                                nbUpdates += 1;
                                memoire.push_back(li);
                            }
                            li = li->getBas();
                        }

                        //efface colonne cj
                        M->effaceColonne(cj);
                        nbUpdates += 1;
                        memoire.push_back(cj);
                    }
                    cj = cj->getDroite();
                }

                //insere ces informations 'nbUpdates' dans l'arbre d'exploration
                Arbre* branche = ArbreExploration->ajouteFils(nbUpdates);

                //on appelle l'algorithme recursivement sur la matrice reduite
                rechercheSol5(M, Solutions, solPartielle, indent + "   ", branche);

                //backtracking
                solPartielle.pop_back();
                Noeud* depile;
                for (int i=memoire.size(); i>0; --i){
                    depile = memoire[i-1];
                    if (depile->getValeur() == -1){
                        M->restaureColonne(depile);
                    }
                    else if (depile->getValeur() == -2){
                        M->restaureLigne(depile);
                    }
                    else{cerr << "Error !" << endl;}
                }
            }
            r = r->getBas();
        }
        return 0;
    }
}

int rechercheSol6(Matrice* M, vector<vector<Noeud*> > &Solutions, vector<Noeud*> &solPartielle, string indent, Arbre* ArbreExploration){
    ///quantifier le nombre d'operation efectuees dans l'arbre d'exploration
    if ((M->getNbLignes() == 0) && (M->getNbColonnes()==0)){
        Solutions.push_back(solPartielle);
        return 0;
    }
    else if ((M->getNbColonnes() == 0) || (M->getNbLignes() == 0)){
        return 0;
    }
    else{
        Noeud* Mh = M->getHeaderMatrice();
        int nbUpdates = 0;

        //choix d'une colonne optimise
        Noeud* c = M->getColonneMin();

        //parcours l'ensemble des lignes
        Noeud* r = Mh->getBas();
        while (r != Mh){
            if (M->get(r,c) == 1){
                //memoire pour le backtracking
                vector<Noeud*> memoire;

                //nombre de mises a jour necessaires au niveau de ce noeud de l'arbre d'exploration
                nbUpdates = 0;

                //ajoute r a la solution partielle, et l'efface de la matrice
                solPartielle.push_back(r);
                M->effaceLigne(r);
                nbUpdates += 1;
                memoire.push_back(r);
                //cout << indent << r->getId() << endl;

                //parcours l'ensemble des colonnes
                Noeud* cj = Mh->getDroite();
                while (cj != Mh){
                    if (M->get(r,cj) == 1){
                        //parcours les lignes
                        Noeud* li = Mh->getBas();
                        while (li != Mh){
                            if (M->get(li,cj) == 1){
                                //efface ligne li
                                M->effaceLigne(li);
                                nbUpdates += 1;
                                memoire.push_back(li);
                            }
                            li = li->getBas();
                        }

                        //efface colonne cj
                        M->effaceColonne(cj);
                        nbUpdates += 1;
                        memoire.push_back(cj);
                    }
                    cj = cj->getDroite();
                }

                //insere ces informations 'nbUpdates' dans l'arbre d'exploration
                Arbre* branche = ArbreExploration->ajouteFils(nbUpdates);

                //on appelle l'algorithme recursivement sur la matrice reduite
                rechercheSol6(M, Solutions, solPartielle, indent + "   ", branche);

                //backtracking
                solPartielle.pop_back();
                Noeud* depile;
                for (int i=memoire.size(); i>0; --i){
                    depile = memoire[i-1];
                    if (depile->getValeur() == -1){
                        M->restaureColonne(depile);
                    }
                    else if (depile->getValeur() == -2){
                        M->restaureLigne(depile);
                    }
                    else{cerr << "Error !" << endl;}
                }
            }
            r = r->getBas();
        }
        return 0;
    }
}
