

def factorial(dato):
    fact=1
    if dato<=1:
        return 1
    else:
        for i in range(2,dato+1): 
            fact=fact*i
    print(fact)
    

def fibonacci(dato):
    if dato<2:
        return dato
    else:
        return fibonacci(dato-1)+fibonacci(dato-2)
    

op=0
while op!=3:
    print('1.-Factorial')
    print('2.-Fibonacci')
    print('3.-Salir')
    op=int(input('Ingresa una opcion: '))
    if op==1:
        print('Factorial')
        n=int(input('Que Factorial quieres buscar: '))
        factorial(n)    
    elif op==2:
        print('Fibonacci')
        n=int(input('Ingrese un valor para n '))
        for i in range(n+1):
            print(fibonacci(i))
    elif op==3:
        print('Hasta pronto')
    else:
        print('Ingrese una opcion valida')