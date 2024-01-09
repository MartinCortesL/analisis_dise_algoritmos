# N reinas 

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
import random

# N reinas con backtracking
def valido(fila,colum,tablero):
    for i in range(fila):
        if(tablero[i]==colum or (tablero[i]-i)==(colum-fila) or (tablero[i]+i)==(colum+fila)):
            return False
    return True

def solucion(n,fila,tablero,soluciones):
    if (fila==n):
        soluciones.append(tablero[:])
        return
    for columna in range(n):
        if valido(fila,columna,tablero):
            tablero[fila]=columna
            solucion(n,fila+1,tablero,soluciones)
            tablero[fila]=-1
            
def crear_tablero(n):
    soluciones=[]
    tablero=[-1]*n
    solucion(n,0,tablero,soluciones)
    return soluciones

#optimizacion con poda del arbol
def optim2(n,fila,tablero):
    if(fila==n):
        return [fila for fila in tablero]
    solu=None
    for columna in range(n):
        if valido(fila,columna,tablero):
            tablero[fila]=columna
            r_parcial=optim2(n,fila+1,tablero)
            if(r_parcial is not None):
                return r_parcial
            tablero[fila]=-1
    return solu
def tablero_optim2(n):
    tabla=[-1]*n
    return optim2(n,0,tabla)

def imprimir(tablero):
    x=len(tablero)
    for i in tablero:
        print(" ".join(" R " if j==i else " ° " for j in range(x)))

# optimizacion con heuristicas inteligentes
def tableroptim3(n):
    return [random.randint(0,n-1) for i in range(n)]
def conflicto(tab):
    m=len(tab)
    conflictos=0
    for i in range(m):
        for j in range(i+1,m):
            if tab[i]==tab[j] or abs(tab[i]-tab[j])==abs(i-j):
                conflictos += 1
    return conflictos

def hill_climbing(n):
    max=1000
    m_tab=tableroptim3(n)
    m_con=conflicto(m_tab)
    for i in range(max):
        vecino = tableroptim3(n)
        con_vecino = conflicto(vecino)
        if (con_vecino < m_con):
            m_tab=vecino
            m_con=con_vecino
        if (m_con==0):
            break
    return m_tab
    
def imp_optim3(tabl):
    m=len(tabl)
    for i in range(n):
        print(" ".join(" R " if j == tabl[i] else " ° " for j in range(m)))
  
        
if __name__=="__main__":
    n=20
    #n reinas con backtraking
    tm=time.time()
    sol=crear_tablero(n)
    if(sol):
        print('Se encontraron ',len(sol), " soluciones: ")
        for d,result in enumerate(sol,start=1):
            print(f'Solucion {d}:')
            imprimir(result)
            print('\n')
        
    else:
        print('No hay solucion')
    t1=time.time()
    print(t1-tm)
        
    print('________________________')
    # optimizacion con poda del arbol
    tn=time.time()
    resu=tablero_optim2(n)
    print('Solucion: ')
    imprimir(resu)
    t2=time.time()
    print(t2-tn)
    
    
    print('_________________________')
    # optimizacion con heuristica inteligente
    to=time.time()
    res=hill_climbing(n)
    print('Solucion: ')
    imp_optim3(res)
    t3=time.time()
    print(t3-to)
    
    
    tiempos=[]
    tiempos.append(t1-tm)
    tiempos.append(t2-tn)
    tiempos.append(t3-to)
    lista=['Backtracking','Con poda del arbol','Heuristicas \ninteligentes']
    colores=["#169c3d","#9c1675","#169c80"]
    fig,ax=plt.subplots()
    ax.set_title('Tiempos')
    ax.set_xlabel("Metodo")
    ax.set_ylabel("tiempo en segundos")
    plt.bar(lista,tiempos,color=colores)
    plt.show()