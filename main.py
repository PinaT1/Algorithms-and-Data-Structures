#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import tkinter
import time
import random
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt
import numpy as np
import _thread
import threading
import HeapSort
import CountingSort
import MergeSort
import InsertionSort

#Variabili
leng = 0
A = [] # Vettore su cui vengono effettuate le operazioni di Sort
A1 = [] # Vettore di supporto
lock = 0 #Semaforo 
k = 0 
font = 'calibri'
algorithms = ["HeapSort", "MergeSort", "CountingSort", "InsertionSort"]


#Funzione di scrittura su file
def writefile (a, title) :
    f = open(title+'.txt','w')
    j = 0
    for i in range (len(a)) :
        j = a[i]
        f.write(' ')
        f.write(str(j))

    f.close()


def GetAlgorithm() :
    global A
    global k
    switcher = {

        algorithms[0] : (HeapSort.HeapSort, (A,) ), 
        algorithms[1] : (MergeSort.MergeSort, (A, 0, len(A) - 1) ),
        algorithms[2] : (CountingSort.counting_sort ,(A, k) ),
        algorithms[3] : (InsertionSort.insertion_sort, (A,) ),

    }
    return switcher


def algorithmcommand(algorithm_name) :
    global lock
    global A
    global k

    lock.acquire()
    leng = len(A)

    #Caso Counting Sort
    if algorithm_name == "CountingSort" :
        A.clear()
        t.insert(tkinter.END, "Generazione automatica nuovo vettore per Counting Sort :" + '\n')
        k = int(leng/2 - 1)
        for i in range(leng) :
            A.insert(i, random.randint(0,k))


    #DISPLAY VETTORE DI PARTENZA
    t.insert(tkinter.END, "Vettore in input :" + '\n' + "{}".format( A[:50] ), font)
    if (leng > 50) :
        t.insert(tkinter.END, '\n' + "...e altri %s elementi" %(len(A) - 50), font)


    t.insert(tkinter.END, '\n' + "Ordinamento vettore in corso..." + '\n', font)

    Algorithm = GetAlgorithm()[algorithm_name]
    arguments = list(Algorithm[1])

    start_time = time.time()
    B = Algorithm[0] (*arguments)
    time1 = time.time() - start_time
    if(B) :
        A = B[:]
    t.insert(tkinter.END, "TEMPO : %s SECONDI." %time1 + '\n', font)


    t.insert(tkinter.END, "Vettore ordinato con %s :" %algorithm_name + '\n' + "{}".format( A[:50] ), font)

    if (leng > 50) : 
        t.insert(tkinter.END, '\n' + "...e altri %s elementi" %(len(A) - 50), font)



    if (leng < 10000) :

        writefile(A, 'Vettore ordinato')
        t.insert(tkinter.END, '\n' + "Salvato su file di testo" + '\n', font)


    A = A1[:]
    displayline()
    lock.release()


#Funzione che genera un vettore casuale data una dimensione
def generavettore(dim) :
    global A
    global A1
    A.clear()
    for i in range(dim) :
        A.insert(i, random.randint(0, dim))


    t.insert(tkinter.END, "VETTORE GENERATO :" + '\n' + "{}".format(A[:50]), font)
    if (dim > 50) :
        t.insert(tkinter.END, '\n' + "...e altri %s elementi" %(len(A) - 50) + '\n', font)

    #Salva il vettore per future operazioni
    savedata(A)
    displayline()


#Funzione che consente di inserire un vettore da tastiera
def inseriscivett() :
    global A
    global A1

    try :
        if  not (bool(E2.get().strip())  ) :
            raise ValueError

        A = stringtoarray(E2.get())

        t.insert(tkinter.END, "Vettore inserito : " + '\n' + "{}".format(A), font)
        savedata(A)
        displayline()


    except ValueError :
        t.insert(tkinter.END, "Errore. Inserire parametri validi." + '\n', 'alert')


#Lettura del vettore da file di testo
def leggifile():
    global A
    global A1
    ftypes = [('Text Files', '.txt')]
    dlg = tkinter.filedialog.Open(filetypes = ftypes)
    fl = dlg.show()

    try :
        if fl != '':

            with open(fl, 'r') as myfile:
                A = stringtoarray(myfile.read().replace('\n', ' '))

            t.insert(tkinter.END, "Vettore letto da file : " + '\n' + "{}".format(A), font )

            savedata(A)
            displayline()
    except :
        t.insert(tkinter.END, "Errore nella lettura del file. Verificare che il formato sia corretto (.txt) o che vi siano in input solo numeri interi" + '\n', 'alert')
        displayline()



def stringtoarray(string) :
    array = []
    temp = ""
    alphanumeric = False

    for char in string :
        if ((char.isalpha()) or (char.isdigit()) ) :
            temp = temp + char
            if(char.isalpha()) :
                alphanumeric = True
        else :
            if (temp is not ""):
                array.append(temp)
            temp = ""

    array.append(temp)

    if(alphanumeric is not True) :
        for i in range (len(array)) :

            if(array[i] == '') :
                array.remove(array[i])
            else :
                array[i] = int(array[i])

    return array



def ClearWindow() :
    t.delete('1.0', tkinter.END)
    

def displayline() :
    t.insert(tkinter.END, "\n" + "-----------------------------------------------" + "\n", 'endline' )

def openexe() :
    try :
        os.startfile("alberi.exe")
    except :
        t.insert(tkinter.END, "Errore. Eseguibile "alberi" non trovato." + '\n', 'alert')


def savedata(A) :
    global A1
    A1 = A[:]



def ThreadInit(i) :
    global A


    if(i == "GeneraVettore" ) :
        try :

            leng = int(E1.get())
            threading.Thread(target = generavettore, args = (int(E1.get()), )).start()

        except ValueError :

            t.insert(tkinter.END, "Errore. Inserire dimensione valida per il vettore e riprovare." + '\n', 'alert')


    elif (i == "TestaAlgoritmo") :
        try :

            threading.Thread(target = testalgorithm, args = (variable.get() , int(E3.get()), int(E4.get()), int(E5.get()),variable2.get() )).start()
            t.insert(tkinter.END, "Test algoritmo " + variable.get() + " in corso..." + '\n', font)

        except  ValueError :
            t.insert(tkinter.END, "Errore. Inserire parametri validi per il testing e riprovare." + '\n', 'alert')


    elif ( i == "MostraRisultati") :
        try :

            t2 = np.loadtxt('CampioniTempi.txt', dtype=int)
            d2 = np.loadtxt("CampioniDimensioni.txt", dtype = int)


            plt.grid(color = "b", linestyle = "-", linewidth = 0.1)
            plt.plot(d2 , t2, 'ro')
            plt.plot(d2 , t2, 'r--')
            plt.axis([ 0 ,d2[-1], 0, t2[-1]])
            plt.ylabel('Tempi')
            plt.xlabel('Dimensioni')
            plt.title("Risultati")
            plt.figure(1)

            y = np.arange(0, 40000, 1)
            x = np.arange(0, d2[-1], 1)
            plt.plot(x, x, 'y')
            plt.plot(y, y**2, 'g')
            x1 = np.arange(1, d2[-1], 1)
            plt.plot(x1, x1 * np.log2(x1), 'b')

            plt.legend(['Campioni', 'Interpolazione', 'n', 'n^2', 'n*log2(n)'], loc='best')
            t.insert(tkinter.END, "Dimensione vettore in input | Tempo in microsecondi" + '\n' + "{}".format((np.column_stack((d2, t2))) ), font)

            displayline()
            plt.show()

        except OSError :
            t.insert(tkinter.END, "Errore. Risultati test non trovati." + '\n', 'alert')

    
    elif (i == "MostraRisultatiAlberi") :
        try :
            t2 = np.loadtxt('TempiAlbero.txt', dtype=int)
            d2 = np.loadtxt("DimensioniAlbero.txt", dtype = int)


            plt.grid(color = "b", linestyle = "-", linewidth = 0.1)
            plt.plot(t2 ,np.log2(d2+1), 'ro')
            plt.plot(t2 , np.log2(d2+1), 'r--')
            plt.axis([ 0 ,d2[-1], 0, 50])
            plt.ylabel('Tempi')
            plt.xlabel('Altezza albero')
            plt.title("Risultati Alberi")
            plt.figure(1)

            x1 = np.arange(1, d2[-1], 1)
            plt.plot( x1, np.log2(x1), 'b')

            plt.legend(['Campioni', 'Interpolazione', 'log2(n)'], loc='best')

            t.insert(tkinter.END, "Dimensione albero | Tempo in microsecondi" + '\n' + "{}".format((np.column_stack((d2, t2)))), font)

            displayline()
            plt.show()

        except OSError :
            t.insert(tkinter.END, "Errore. Risultati test alberi non trovati." + '\n', 'alert')

    else :

        try :
            if (len(A) <= 0) :
                raise ValueError("Errore. Verificare correttezza dei parametri di input.")

            threading.Thread(target = algorithmcommand, args = (i, )).start()

        except ValueError as err:
            t.insert(tkinter.END, err.args[0] + '\n', 'alert')



def testalgorithm(algorithm_name, dim , fattoremoltiplicativo, numripetizioni, inputtype) :
    global A
    global k
    lock.acquire()
    #prende da menu a tendina
    times = [] #Tempi di esecuzione
    dims = [] #Dimensioni
    j = dim * fattoremoltiplicativo
    times.insert(0, 0.0)
    dims.insert(0, 0)

    A.clear()
    misura = 0
    for rip in range (numripetizioni) :
        p = 0
        if (inputtype == "Random") :
            for i in range(dim) :
                A.insert(i, random.randint(0, int(dim/2 - 1)))

        elif (inputtype == "Crescente" or inputtype == "Decrescente"):
            for i in range(dim) :
                if(algorithm_name == "CountingSort"):
                    A.insert(i, p)
                    if ((i+1)%3 == 0) :
                        p+=1
                else :
                    A.insert(i, i)
            if(inputtype == "Decrescente") :
                A = A[::-1]

        k = int(len(A)/2 - 1)
        
        Algorithm = GetAlgorithm()[algorithm_name]
        arguments = list(Algorithm[1])

        start_time = time.time()
        Algorithm[0] (*arguments)
        misura = time.time() - start_time

        times.append(misura*1000000)
        dims.append(dim)
        clock.config(text="Tempo " + str(misura) + " | Dimensione input " + str(dim) + " | Ripetizione  " + str(rip+1))
        dim = dim + j # Incremento dimensione per prossima iterazione
        A.clear()
     
    
    #Salvataggio su file di testo
    writefile(times, "CampioniTempi")
    writefile(dims, "CampioniDimensioni")

    t.insert(tkinter.END, "Test concluso. Tempi e dimensioni sono salvati su file." + '\n', font)
    displayline()
    lock.release()



#Interfaccia
mainWindow = tkinter.Tk()
mainWindow.title("Smart Tester - Algoritmi e Strutture Dati")
mainWindow.geometry('860x600')
mainWindow.resizable(width=False,height=False)
mainWindow.iconbitmap('fedii.ico')


rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(padx=10,side='right', anchor='n', expand=True)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(padx=10,side = 'left', anchor = 'n', expand = True)

bottomFrame = tkinter.Frame(mainWindow)
bottomFrame.pack(side = 'bottom', anchor = 'n', expand = True)

t = ScrolledText(mainWindow, borderwidth=3, relief="sunken")


t.tag_config('alert', background="yellow", foreground="red")
t.tag_config('cmd', background="blue", foreground="white")
t.tag_config('calibri', font = "Calibri")
t.tag_config('endline', foreground = "blue")
t.pack()



#Bottoni
buttons = []

for h in range (len(algorithms)) :
    buttons.insert ( h, tkinter.Button(rightFrame, command=lambda h = h : ThreadInit(algorithms[h]),  text=algorithms[h]) ) #h = h per operazioni su lambda
    buttons[h].pack(side = 'top', pady=2)

button3 = tkinter.Button(rightFrame, command=ClearWindow, text="ClearWindow", fg = 'red')

button6 = tkinter.Button(bottomFrame, command=lambda : ThreadInit("TestaAlgoritmo"),  text="Testa Algoritmo")
button7 = tkinter.Button(bottomFrame, command=lambda : ThreadInit("MostraRisultati"),  text="Mostra Risultati Test")
button8 = tkinter.Button(rightFrame, command= openexe,  text="Apri .exe alberi")
button9 = tkinter.Button(rightFrame, command=lambda : ThreadInit("MostraRisultatiAlberi"),  text="Mostra Risultati Alberi")



button3.pack(side='top')

button7.pack(side = 'right',padx=(0,20),pady=(60,0))
button6.pack(side = 'right',padx=(20,10),pady=(60,0))


#Label
label1 = tkinter.Label( leftFrame, text="Dimensione Vettore")
label2 = tkinter.Label (leftFrame, text = "Inserimento manuale")
label3 = tkinter.Label(leftFrame, text = "Leggi da file")
label4 = tkinter.Label(bottomFrame, text = ("Dim. iniziale : \n \n " + " Fattore moltiplicativo : \n \n" + "Ripetizioni : \n") )

tkinter.Label(rightFrame,pady=10).pack()

button8.pack(side = 'top', pady=5)
button9.pack(side = 'top')

E1 = tkinter.Entry(leftFrame, bd =5)
E2 = tkinter.Entry(leftFrame, bd = 5)
E3 = tkinter.Entry(bottomFrame, bd = 5)
E4 = tkinter.Entry(bottomFrame, bd = 5)
E5 = tkinter.Entry(bottomFrame, bd = 5)

genera = tkinter.Button(leftFrame, text ="Genera", command = lambda : ThreadInit("GeneraVettore"))
inserisci = tkinter.Button(leftFrame, text = "Inserisci", command = inseriscivett)
leggi = tkinter.Button(leftFrame, text = "Apri", command = leggifile) 

lock = _thread.allocate_lock()



variable = tkinter.StringVar(bottomFrame)
variable.set(algorithms[0]) # default value

variable2 = tkinter.StringVar(bottomFrame)
variable2.set("Random")     # default value


clock = tkinter.Label(mainWindow, font=('calibri', 12, 'bold'), bg='white', relief="groove")
clock.pack(fill="both")

options = tkinter.OptionMenu(bottomFrame, variable, *algorithms)
options.pack( pady=(10,0))

inputopt = tkinter.OptionMenu(bottomFrame, variable2, "Random", "Crescente", "Decrescente")
inputopt.pack( pady=(0,10))




label1.pack(side = 'top')
E1.pack(side = 'top')
genera.pack(side = 'top',pady=(0,5))
label2.pack(side = 'top')
E2.pack(side = 'top')
inserisci.pack(side = 'top',pady=(0,5))
label3.pack(side = 'top')
label4.pack(side = 'left')
leggi.pack(side = 'top')

E3.pack()
E4.pack()
E5.pack()

mainWindow.mainloop()
