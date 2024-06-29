#################################################################
## AO PREENCHER ESSE CABEC¸ALHO COM O MEU NOME E O MEU N´UMERO USP,
## DECLARO QUE SOU O ´UNICO AUTOR E RESPONS´AVEL POR ESSE PROGRAMA.
## TODAS AS PARTES ORIGINAIS DESSE EXERC´ICIO PROGRAMA (EP) FORAM
## DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUC¸~OES
## DESSE EP E QUE PORTANTO N~AO CONSTITUEM DESONESTIDADE ACAD^EMICA
## OU PL´AGIO.
## DECLARO TAMB´EM QUE SOU RESPONS´AVEL POR TODAS AS C´OPIAS
## DESSE PROGRAMA E QUE EU N~AO DISTRIBUI OU FACILITEI A
## SUA DISTRIBUIC¸~AO. ESTOU CIENTE QUE OS CASOS DE PL´AGIO E
## DESONESTIDADE ACAD^EMICA SER~AO TRATADOS SEGUNDO OS CRIT´ERIOS
## DIVULGADOS NA P´AGINA DA DISCIPLINA.
## ENTENDO QUE EPS SEM ESTE CABEC¸ALHO N~AO SER~AO CORRIGIDOS E,
## AINDA ASSIM, PODER~AO SER PUNIDOS POR DESONESTIDADE ACAD^EMICA.
## Nome :Miqueias Salino de Almeida
## NUSP :15521635
## Turma:
## Prof.: Roberto Hirata Jr.
## Refer^encias: Com exce¸c~ao das rotinas fornecidas no enunciado
## e em sala de aula, caso voc^e tenha utilizado alguma ref^encia,
## liste-as abaixo para que o seu programa n~ao seja considerado
## pl´agio ou irregular.
## Exemplo:
## - O algoritmo Quicksort foi baseado em
## http://wiki.python.org.br/QuickSort
##############################################################

from random import random
from random import randint
from sys import platform
import time as T
import matplotlib.pyplot as plt
import ctypes

libsort = ctypes.CDLL('./libsortings.so')
libsort.selectionC.argtypes =[ctypes.POINTER(ctypes.c_int),ctypes.c_int]
libsort.bubbleC.argtypes = [ctypes.POINTER(ctypes.c_int),ctypes.c_int]
libsort.insertionC.argtypes = [ctypes.POINTER(ctypes.c_int),ctypes.c_int]
libsort.countingC.argtypes = [ctypes.POINTER(ctypes.c_int),ctypes.c_int]

def mediaT(T, n):
    '''A função recebe um vetor T e seu tamanho e retorna sua média.'''
    somaT=0
    for i in range (n):
        somaT= somaT + T[i]
    mediaTn= somaT/n
    return (mediaTn)

def varT(T, n):
    '''A função recebe um vetor T e seu tamanho e retorna a sua variância.'''
    SomaVarianca=0
    Media = mediaT(T, n)
    for i in range(n):
        SomaVarianca = SomaVarianca + (T[i]- Media)**2
        i=i+1
    Varianca= SomaVarianca / n
    return (Varianca)
    

def selectionC(V,n):
    pV=(ctypes.c_int *n)(*V)
    libsort.selectionC(pV,n)

def bubbleC(V,n):
    pV = (ctypes.c_int *n)(*V)
    libsort.bubbleC(pV,n)

def insertionC(V,n):
    pV = (ctypes.c_int *n)(*V)
    libsort.insertionC(pV,n)

def countingC(V,n):
    pV = (ctypes.c_int *n)(*V)
    libsort.countingC(pV,n)

def embaralha(V, n,p):
    '''A função recebe um vetor ordenado, seu tamanho e uma porcentagem p
     e embaralha o vetor p%'''
    l = int(n*p/200)
    for k in range(l):
        i=randint(0, n-1)
        j=randint(0, n-1)
        temp = V[i]
        V[i] = V[j]
        V[j] = temp
    return(V)   

def timeMe(func,V, n,m,p):
    '''A função recebe uma das funções de ordenação, um vetor ordenado, o tamanho do vetor, 
    a quantidade de repetições e a porcentagem que deve ser embaralhada e 
    devolve a media e a variâcia de tempo necessário para reordenar a lista'''
    for i in range(m):
        W=[]
        Vsorted = copiar(V)
        embaralha(V, n,p)         
        start = T.process_time()
        if(func==sorted):
            V=func(V)
        else:
            V=func(V, n)
        finish = T.process_time()
        V = copiar(Vsorted)
        time = finish - start
        W.append(time)
    MediaTempo = mediaT(W, len(W))
    VariancaTempo = varT(W, len(W))
    return(MediaTempo, VariancaTempo)

def GraficaSortings(mpontos,mediaMCMPi,desvioMCMPi):
    '''A função recebe três listas e retorna um gráfico com desvio padrão.'''
    fig, ax = plt.subplots()
    legenda1=["selection", "bubble", "insertion", "counting", "sort"]
    legenda2=["bubble","insertion", "sort"]
    for i in range(len(mediaMCMPi)):    
        plt.errorbar(mpontos,mediaMCMPi[i], desvioMCMPi[i], fmt='o')
    if(len(mediaMCMPi)==5):
        ax.legend(legenda1)
        ax.set_xlabel('tamanho das listas')
    else:
        ax.legend(legenda2)
        ax.set_xlabel('porcentagem de desordenação')
    ax.set_ylabel('tempo')
    ax.set_title("algoritmos de ordenação")
    fig=plt.figure()
    fig.savefig('fig.png')
    return(fig)

def Criarlistas(n):
    '''A função recebe um número n e cria uma lista desordenada de tamanho n'''
    V = [randint(0,9999) for i in range(n)]
    return (V)

def copiar(V):
    '''A função copia uma lista para outro lugar.'''
    W = []
    for i in range(len(V)):
        W.append(V[i])
    return(W)


def main():
    SelectionMil = []
    SelectionCincoMil = []
    SelectionDezMil = []
    SelectionCinqueMil = []
    SelectionCemMil = []
    BubbleMil = []
    BubbleCincoMil = []
    BubbleDezMil = []
    BubbleCinqueMil = []
    BubbleCemMil = []
    InsertionMil = []
    InsertionCincoMil = []
    InsertionDezMil = []
    InsertionCinqueMil = []
    InsertionCemMil = []   
    CountingMil = []
    CountingCincoMil = []
    CountingDezMil = []
    CountingCinqueMil = []
    CountingCemMil = []
    SortMil = []
    SortCincoMil = []
    SortDezMil = []
    SortCinqueMil = []
    SortCemMil = []
    
    for i in range(10):
        V = Criarlistas(1000)
        Temp = copiar(V)
        start = T.process_time()
        selectionC(V, len(V))
        finish = T.process_time()
        time = finish - start
        SelectionMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        bubbleC(V,len(V))
        finish = T.process_time()
        time = finish - start
        BubbleMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        insertionC(V,len(V))
        finish = T.process_time()
        time = finish - start
        InsertionMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        countingC(V, len(V))
        finish = T.process_time()
        time = finish - start
        CountingMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        V=sorted(V)
        finish = T.process_time()
        time = finish - start
        SortMil.append(time)

        V = Criarlistas(5000)
        Temp = copiar(V)
        start = T.process_time()
        selectionC(V, len(V))
        finish = T.process_time()
        time = finish - start
        SelectionCincoMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        bubbleC(V,len(V))
        finish = T.process_time()
        time = finish - start
        BubbleCincoMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        insertionC(V,len(V))
        finish = T.process_time()
        time = finish - start
        InsertionCincoMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        countingC(V, len(V))
        finish = T.process_time()
        time = finish - start
        CountingCincoMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        V=sorted(V)
        finish = T.process_time()
        time = finish - start
        SortCincoMil.append(time)

        V = Criarlistas(10000)
        Temp = copiar(V)
        start = T.process_time()
        selectionC(V, len(V))
        finish = T.process_time()
        time = finish - start
        SelectionDezMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        bubbleC(V,len(V))
        finish = T.process_time()
        time = finish - start
        BubbleDezMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        insertionC(V,len(V))
        finish = T.process_time()
        time = finish - start
        InsertionDezMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        countingC(V, len(V))
        finish = T.process_time()
        time = finish - start
        CountingDezMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        V=sorted(V)
        finish = T.process_time()
        time = finish - start
        SortDezMil.append(time)

        V = Criarlistas(50000)
        Temp = copiar(V)
        start = T.process_time()
        selectionC(V, len(V))
        finish = T.process_time()
        time = finish - start
        SelectionCinqueMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        bubbleC(V,len(V))
        finish = T.process_time()
        time = finish - start
        BubbleCinqueMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        insertionC(V,len(V))
        finish = T.process_time()
        time = finish - start
        InsertionCinqueMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        countingC(V, len(V))
        finish = T.process_time()
        time = finish - start
        CountingCinqueMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        V=sorted(V)
        finish = T.process_time()
        time = finish - start
        SortCinqueMil.append(time)

        V = Criarlistas(100000)
        Temp = copiar(V)
        start = T.process_time()
        selectionC(V, len(V))
        finish = T.process_time()
        time = finish - start
        SelectionCemMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        bubbleC(V,len(V))
        finish = T.process_time()
        time = finish - start
        BubbleCemMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        insertionC(V,len(V))
        finish = T.process_time()
        time = finish - start
        InsertionCemMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        countingC(V, len(V))
        finish = T.process_time()
        time = finish - start
        CountingCemMil.append(time)
        V = copiar(Temp)
        start = T.process_time()
        V=sorted(V)
        finish = T.process_time()
        time = finish - start
        SortCemMil.append(time)
    SelectionMilm = mediaT(SelectionMil, len(SelectionMil))
    SelectionMild = (varT(SelectionMil, len(SelectionMil)))**(1/2)
    SelectionCincoMilm = mediaT(SelectionCincoMil, len(SelectionCincoMil))
    SelectionCincoMild = (varT(SelectionCincoMil, len(SelectionCincoMil)))**(1/2)
    SelectionDezMilm = mediaT(SelectionDezMil, len(SelectionDezMil))
    SelectionDezMild = (varT(SelectionDezMil, len(SelectionDezMil)))**(1/2)
    SelectionCinqueMilm = mediaT(SelectionCinqueMil, len(SelectionCinqueMil))
    SelectionCinqueMild = (varT(SelectionCinqueMil, len(SelectionCinqueMil)))**(1/2)
    SelectionCemMilm = mediaT(SelectionCemMil, len(SelectionCemMil))
    SelectionCemMild = (varT(SelectionCemMil, len(SelectionCemMil)))**(1/2)
    
    BubbleMilm = mediaT(BubbleMil, len(BubbleMil))
    BubbleMild = (varT(BubbleMil, len(BubbleMil)))**(1/2)
    BubbleCincoMilm = mediaT(BubbleCincoMil, len(BubbleCincoMil))
    BubbleCincoMild = (varT(BubbleCincoMil, len(BubbleCincoMil)))**(1/2)
    BubbleDezMilm = mediaT(BubbleDezMil, len(BubbleDezMil))
    BubbleDezMild = (varT(BubbleDezMil, len(BubbleDezMil)))**(1/2)
    BubbleCinqueMilm = mediaT(BubbleCinqueMil, len(BubbleCinqueMil))
    BubbleCinqueMild = (varT(BubbleCinqueMil, len(BubbleCinqueMil)))**(1/2)
    BubbleCemMilm = mediaT(BubbleCemMil, len(BubbleCemMil))
    BubbleCemMild = (varT(BubbleCemMil, len(BubbleCemMil)))**(1/2)

    InsertionMilm = mediaT(InsertionMil, len(InsertionMil))
    InsertionMild = (varT(InsertionMil, len(InsertionMil)))**(1/2)
    InsertionCincoMilm = mediaT(InsertionCincoMil, len(InsertionCincoMil))
    InsertionCincoMild = (varT(InsertionCincoMil, len(InsertionCincoMil)))**(1/2)
    InsertionDezMilm = mediaT(InsertionDezMil, len(InsertionDezMil))
    InsertionDezMild = (varT(InsertionDezMil, len(InsertionDezMil)))**(1/2)
    InsertionCinqueMilm = mediaT(InsertionCinqueMil, len(InsertionCinqueMil))
    InsertionCinqueMild = (varT(InsertionCinqueMil, len(InsertionCinqueMil)))**(1/2)
    InsertionCemMilm = mediaT(InsertionCemMil, len(InsertionCemMil))
    InsertionCemMild = (varT(InsertionCemMil, len(InsertionCemMil)))**(1/2)

    CountingMilm = mediaT(CountingMil, len(CountingMil))
    CountingMild = (varT(CountingMil, len(CountingMil)))**(1/2)
    CountingCincoMilm = mediaT(CountingCincoMil, len(CountingCincoMil))
    CountingCincoMild = (varT(CountingCincoMil, len(CountingCincoMil)))**(1/2)
    CountingDezMilm = mediaT(CountingDezMil, len(CountingDezMil))
    CountingDezMild = (varT(CountingDezMil, len(CountingDezMil)))**(1/2)
    CountingCinqueMilm = mediaT(CountingCinqueMil, len(CountingCinqueMil))
    CountingCinqueMild = (varT(CountingCinqueMil, len(CountingCinqueMil)))**(1/2)
    CountingCemMilm = mediaT(CountingCemMil, len(CountingCemMil))
    CountingCemMild = (varT(CountingCemMil, len(CountingCemMil)))**(1/2)

    SortMilm = mediaT(SortMil, len(SortMil))
    SortMild = (varT(SortMil, len(SortMil)))**(1/2)
    SortCincoMilm = mediaT(SortCincoMil, len(SortCincoMil))
    SortCincoMild = (varT(SortCincoMil, len(SortCincoMil)))**(1/2)
    SortDezMilm = mediaT(SortDezMil, len(SortDezMil))
    SortDezMild = (varT(SortDezMil, len(SortDezMil)))**(1/2)
    SortCinqueMilm = mediaT(SortCinqueMil, len(SortCinqueMil))
    SortCinqueMild = (varT(SortCinqueMil, len(SortCinqueMil)))**(1/2)
    SortCemMilm = mediaT(SortCemMil, len(SortCemMil))
    SortCemMild = (varT(SortCemMil, len(SortCemMil)))**(1/2)

    SelectionsTimeM = [SelectionMilm, SelectionCincoMilm, SelectionDezMilm,  SelectionCinqueMilm,SelectionCemMilm]
    SelectionsTimeD = [SelectionMild, SelectionCincoMild, SelectionDezMild,  SelectionCinqueMild,SelectionCemMild]
    BubblesTimeM = [BubbleMilm, BubbleCincoMilm, BubbleDezMilm, BubbleCinqueMilm, BubbleCemMilm]
    BubblesTimeD = [BubbleMild, BubbleCincoMild, BubbleDezMild, BubbleCinqueMild, BubbleCemMild]
    InsertionsTimeM = [InsertionMilm, InsertionCincoMilm, InsertionDezMilm, InsertionCinqueMilm, InsertionCemMilm]
    InsertionsTimeD = [InsertionMild, InsertionCincoMild, InsertionDezMild, InsertionCinqueMild, InsertionCemMild]
    CountingsTimeM = [CountingMilm, CountingCincoMilm, CountingDezMilm, CountingCinqueMilm, CountingCemMilm]
    CountingsTimeD = [CountingMild, CountingCincoMild, CountingDezMild, CountingCinqueMild, CountingCemMild]
    SortsTimeM = [SortMilm, SortCincoMilm, SortDezMilm, SortCinqueMilm, SortCemMilm]
    SortsTimeD = [SortMild, SortCincoMild, SortDezMild, SortCinqueMild, SortCemMild]
    MediaTempo = [SelectionsTimeM, BubblesTimeM,InsertionsTimeM, CountingsTimeM,SortsTimeM]
    DesvioTempo= [SelectionsTimeD, BubblesTimeD,InsertionsTimeD, CountingsTimeD, SortsTimeD]
    pontos=[1000, 5000, 10000, 50000, 100000]
    print(pontos,MediaTempo,DesvioTempo)
    GraficodesOrdenado=GraficaSortings(pontos,MediaTempo,DesvioTempo)


main()

    