datos= [1,3,5,7,9,12,14,16,18,19,21,23,25,27,29,30]


def Busqueda_bin(lista,elemento):
    inicio=0
    final=len(lista)-1
    while inicio<=final:
        medio=(inicio+final)//2
        if(lista[medio]==elemento):
          return  print('Dato encontrado')
        elif lista[medio]<elemento:
            inicio=medio+1
        elif lista[medio]>elemento:
            final=medio-1
    return print('Dato no encontrado')

def Busqueda_lineal(list,numero):
    for i in range(len(list)):
        if(list[i]==numero):
            return print('Se encontro el dato')
    return print('No se encontro el dato')

def salir():
    print('Hasta pronto')

op=1
while op!=3:
    print('1.-Busqueda Binaria')
    print('2.-Busqueda Lineal')
    print('3.-Salir')
    op=int(input('Ingresa una opcion: '))
    if op==1:
        print('Busqueda Binaria')
        n=int(input('Que dato quieres buscar '))
        Busqueda_bin(datos,n)
    elif op==2:
        print('Busqueda Lineal')
        n=int(input('Que dato quieres buscar '))
        Busqueda_lineal(datos,n)
    elif op==3:
        salir()
    else:
        print('Ingrese una opcion valida')   


#x=int(input('Que tamaño tiene el arreglo'))
#datos=[input("Valor: ") for j in range(x)]    
