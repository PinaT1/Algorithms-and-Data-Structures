#ifndef HEADER_H_
#define HEADER_H_
#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>

using namespace std;

struct Nodo{

        int key;
        Nodo* p;
        Nodo* left;
        Nodo* right;

        };

struct albero{
       Nodo* radix;
       };



void inorderwalk(Nodo*);
void abrinsert(albero&,Nodo*);
Nodo* abrdelete(albero&,Nodo*);
Nodo* iterativesearch(Nodo*,int);
Nodo* treesearch(Nodo*,int);
Nodo* successor(Nodo*);
Nodo* predecessor(Nodo*);
Nodo* maximum(Nodo*);
Nodo* minimum(Nodo*);

#endif
