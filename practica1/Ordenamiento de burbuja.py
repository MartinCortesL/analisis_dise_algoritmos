list=[]


def Burbuja_Optimizada(lista):
    comparacion=0
    for i  in range(len(lista)-1):
        for j  in range(len(lista)-i-1):
            if lista[j]>lista[j+1]:
                temporal=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=temporal
                comparacion+=1
    
    print(lista)
    print(comparacion)
               
def Burbuja(lista):
    com=0
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if(lista[j]>lista[j+1]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
                com+=1
    print(lista)  
    print(com)

def salir():
    print('Hasta pronto')

op=1
while op!=3:
    print('1.-Burbuja optimizado')
    print('2.-Burbuja')
    print('3.-Salir')
    op=int(input('Ingresa una opcion: '))
    if op==1:
        print('Burbuja optimizada')
        n=int(input('Ingrese la cantidad de datos del arreglo:'))
        list=[input('Valores: ') for i in range(n)]
        print('Lista ordenada')
        Burbuja_Optimizada(list)
    elif op==2:
        print('Burbuja')
        m=int(input('Ingrese la cantidad de datos del arreglo '))
        list=[input('Valores: ') for j in range(m)]
        print('Lista ordenada')
        Burbuja(list)
    elif op==3:
        salir()
    else:
        print('Ingrese una opcion valida')   

