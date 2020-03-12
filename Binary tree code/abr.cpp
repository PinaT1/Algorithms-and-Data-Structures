#include "abr.h"

void inorderwalk(Nodo* x){

     if(x!=0){
             inorderwalk(x->left);
             cout<<x->key<<" ";
             inorderwalk(x->right);
     }
}

void abrinsert(albero& T,Nodo* z){

     Nodo* y=0;
     Nodo* x=T.radix;
     while (x!=0){
           y=x;
           if ((z->key)<(x->key)){
                x=x->left;
           }else{
              x=x->right;
            }
     }
     z->p=y;
     if (y==0) T.radix=z;
     else {
         if ((z->key)<(y->key))     //albero non vuoto, valuto dove attaccare l'elemento
            { y->left=z;
         }else{
            y->right=z;}
          }
     }


Nodo * abrdelete(albero& T,Nodo* z){
    Nodo* x;
    Nodo* y;
    if (((z->left)==0) || ((z->right)==0)) {y=z;}
    else {y= successor(z);}

    if (y->left !=0) {
            x=y->left;}
    else {x=y->right;}

    if(x != 0) {x->p=y->p;}

    if(y->p ==0) {
            T.radix=x;}
    else {
        if(y==(y->p)->left) (y->p)->left=x;
        else (y->p)->right=x;
    }
    if( y!= z){
        z->key=y->key;
        z->p=y->p;
        z->left=y->left;
        z->right=y->right;
    }
    return y;
}

Nodo * iterativesearch(Nodo* x,int k){

     Nodo* n;
     while (( x != 0 ) && ( k != x->key )){
            if (k<x->key) x=x->left;
            else x=x->right;
            }

    if(x) return x;
    else return n;

}

Nodo * treesearch(Nodo*x, int k){

    if(( x == 0 ) || x->key == k){
        return x;}

    if (k < x->key){
        return treesearch(x->left, k);
    } else {
        return treesearch(x->right, k);}

}


Nodo * minimum(Nodo *x ){

      while (x->left!=0){
            x=x->left;}
      return x;

     }

Nodo * maximum(Nodo *x ){

      while (x->right!=0){
            x=x->right;}
      return x;

     }


Nodo* successor(Nodo* x){

    Nodo* y;
    if(x->right!=0){
        return minimum(x->right); //il più piccolo elemento del sottoalbero con radice x->right;
        }

    y=x->p;
    while(y!=0 && x==y->right){
        x=y;
        y=y->p;
        }
    return y;
      }


Nodo* predecessor(Nodo* x){
    Nodo* y;
    if(x->left!=0){
        return maximum(x->left); //l' elemento più grande del sottoalbero con radice x->left;
        }

    y=x->p;
    while(y!=0 && x==y->left){
        x=y;
        y=y->p;
        }
    return y;
      }


