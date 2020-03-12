#include <iostream>
#include "abr.h"

using namespace std;

ofstream risultati_tempi;
ofstream risultati_dim;

int main(){
    albero T;
    T.radix=0;
    Nodo *z;
    Nodo *y;
    int op,input=0,dimensione=0;
    int numnodi=0, numrip=0;
    bool exit=false;

    cout<<"ALBERI BINARI DI RICERCA "<<endl;
    cout<<endl;
    cout<<endl;
    cout<<"Scegliere un'operazione da eseguire: "<<endl;

    do{
       do{
            cout<<"1.Inserimento elemento."<<endl;
            cout<<"2.Stampa albero in ordine crescente."<<endl;
            cout<<"3.Ricerca elemento."<<endl;
            cout<<"4.Elimina elemento."<<endl;
            cout<<"5.Trova successore."<<endl;
            cout<<"6.Trova predecessore."<<endl;
            cout<<"7.Mostra elemento massimo."<<endl;
            cout<<"8.Mostra elemento minimo."<<endl;
            cout<<"9.Effettua misurazione dei tempi di esecuzione dell'operazione di inserimento."<<endl;
            cout<<"10.Esci."<<endl<<endl;

           cin>>op;
           }while(op<1 || op>10);

              switch(op){

                     case 1:
                          cout<<"Inserire il valore da memorizzare nell'albero: ";
                          z=new Nodo;
                          z->left=0;
                          z->right=0;
                          z->p=0;
                          cin>>input;
                          z->key=input;//inizializzazione campo chiave
                          abrinsert(T,z);
                          input=0;
                          cout<<endl;
                          break;

                    case 2:
                          inorderwalk(T.radix);
                          cout<<endl;
                          break;

                    case 3:
                          cout<<"Inserire l'elemento da ricercare: ";
                          cin>>input;
                          z=new Nodo;

                          z=iterativesearch(T.radix,input);

                        if(z->key == input){
                            cout<<"Elemento "<<z->key<<" trovato."<<endl;}
                        else{
                            cout<<"Elemento non trovato nell'albero!"<<endl;}
                          input=0;
                          cout<<endl;
                          break;


                    case 4:
                          cout<<"Inserire l'elemento da eliminare: ";
                          cin>>input;
                          z=new Nodo;
                          y= new Nodo;

                          z=iterativesearch(T.radix,input);

                        if (z->key == input){
                            y=abrdelete(T,z);
                            cout<<"Il nodo con chiave "<<y->key<<" e' stato eliminato!"<<endl;}
                        else
                            {cout<<"Elemento non trovato nell'albero!"<<endl;}

                        input=0;
                        cout<<endl;
                        break;

                    case 5:
                          cout<<"Ricerca il successore dell'elemento: ";
                          cin>>input;
                          z=new Nodo;
                          y= new Nodo;
                          z=iterativesearch(T.radix,input);
                          y=successor(z);

                          if(z->key == input){
                            cout<<"Elemento "<<z->key<<" trovato."<<endl;
                            if (y!=0){
                                cout<<"Nodo successore di "<<(z->key)<<": "<<(y->key)<<endl;
                            }else{
                                cout<<"Nodo successore non trovato!"<<endl;}

                          }else {
                            cout<<"Elemento "<<input<<" non trovato nell'albero!"<<endl;}

                          cout<<endl;
                          input=0;
                          break;

                    case 6:
                          cout<<"Ricerca il predecessore dell'elemento: ";
                          cin>>input;
                          z=new Nodo;
                          y= new Nodo;
                          z=iterativesearch(T.radix,input);
                          y=predecessor(z);

                          if(z->key == input){
                            cout<<"Elemento "<<z->key<<" trovato."<<endl;
                            if (y!=0){
                                cout<<"Nodo predecessore di "<<(z->key)<<": "<<(y->key)<<endl;
                            }else{
                                cout<<"Nodo predecessore non trovato!"<<endl;}

                          }else {
                            cout<<"Elemento "<<input<<" non trovato nell'albero!"<<endl;}

                          cout<<endl;
                          input=0;
                          break;

                    case 7:
                          z= new Nodo;
                          z=maximum(T.radix);//ricerca massimo
                          cout<<"Elemento massimo trovato: "<<z->key<<endl;
                          cout<<endl;
                          break;

                     case 8:
                          z=new Nodo;
                          z=minimum(T.radix);
                          cout<<"Elemento minimo trovato: "<<z->key<<endl;
                          cout<<endl;
                          break;


                     case 9: {

                          cout << "Inserire numero di nodi: ";
                          cin >> numnodi;
                          cout << "Inserire numero di ripetizioni: ";
                          cin >> numrip;

                          cout<<endl;
                          cout<<"L'algoritmo verra' provato " << numrip <<" volte per ogni " <<numnodi<< " nodi."<<endl;
                          risultati_tempi.open ("TempiAlbero.txt" ,ios::out);
                          risultati_dim.open("DimensioniAlbero.txt", ios::out);

                          clock_t t2;
                          int microsec,i;
                          int tempi[numrip], dimensioni[numrip];

                          risultati_tempi<< 0;
                          risultati_dim << 0;

                          for (i = 0; i<numrip; i++) {
                          t2 = clock();

                          while(dimensione<= numnodi){


                          Nodo* z;
                          z=new Nodo;
                          z->key=rand()%1000; //generazione random di un numero da inserire come chiave
                          z->p=0; //inizializzazione campi di z
                          z->left=0;
                          z->right=0;

                          abrinsert(T ,z);

                          dimensione+=1;//aumento dimensione
                          }


                          t2 = clock() - t2;
                          microsec = (((float)t2)/CLOCKS_PER_SEC) *(1000000);
                          tempi[i] = microsec;
                          dimensioni[i] = numnodi *(i+1);
                          dimensione = 0;
                          cout << "Nodi presenti: "<<(numnodi*(i+1))<<", Microsecondi: "<<microsec<<endl;
                          }

                          cout<<endl;

                          for (i = 0; i<numrip; i++){
                          risultati_tempi<<" "<< tempi[i];
                          risultati_dim <<" "<< dimensioni[i];
                          }
                          risultati_tempi.close();
                          risultati_dim.close();
                          break;}

                     case 10:
                          exit=true;
                          return 0;
                          break;

                             }
             }while(!exit);

   return 0;
    }
