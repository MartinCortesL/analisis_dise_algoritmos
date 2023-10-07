# Complejidad O( n Log n)
# funcion para dividir el arreglo
def mergesort(arreglo):
    #caso base
    if(len(arreglo)<=1):
        return arreglo
    # dividir
    #obtener la mitad del arreglo
    mitad=len(arreglo)//2
    # divide el arreglo en mitades
    izq=arreglo[:mitad]
    der=arreglo[mitad:]
    #conquistar
    # llamar a la funcion recursiva
    izq=mergesort(izq)
    der=mergesort(der)
    #combinar o mezclar
    return merge(izq,der)

def merge(izq,der):
    ordenado=[]
    i_izq,i_der=0,0
    #ciclo para comparar elementos
    while i_izq<len(izq) and i_der < len(der):
        if izq[i_izq]<der[i_der]:
            ordenado.append(izq[i_izq])
            i_izq+=1
        else:
            ordenado.append(der[i_der])
            i_der+=1
    # agrega todos los valores restantes
    ordenado.extend(izq[i_izq:])
    ordenado.extend(der[i_der:])
    return ordenado

if __name__=='__main__':
    arreglo=[2,7,4,1,8,5,6,3,9]
    print('Arreglo sin ordendar: ', arreglo)
    ordenado=mergesort(arreglo)
    print("Arreglo ordenado: ", ordenado)
    n=int(input('Ingrese el tamaño del arreglo '))
    lista=[input('Ingrese los datos del arreglo ') for i in range(n)]
    print('Arreglo no ordenado ',lista)
    ordenado=mergesort(lista)
    print('Arreglo ordenado ', ordenado)