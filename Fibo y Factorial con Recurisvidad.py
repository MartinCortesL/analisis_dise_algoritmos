def fibo(x):
    if x==0:
        return 0
    if x==1:
        return 1
    
    return fibo(x-2)+fibo(x-1)

def facto(x):
    if x==0 or x==1:
        return 1
    return x*facto(x-1)

op=0
while(op!=3):
    print('Menu')
    print('1.-Fibonacci')
    print('2.-Factorial')
    print('3.Salir')
    op=int(input('Elige una opcion: '))
    if op==1:
        y=int(input('Que dato de fibonacci desea: '))
        for i in range(y+1):
            print(fibo(i))
    if op==2:
        n=int(input('Que factorial desea: '))
        print(facto(n))
    if op==3:
        print('Hasta pronto')


