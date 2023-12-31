#Calculadora que hace operaciones basicas en python (sumas,restas,multiplicacion y division)

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Suma', accion1),
        '2': ('Resta', accion2),
        '3': ('Multiplicacion', accion3),
        '4': ('Division',accion4),
        '5': ('Salir', salir)
    }

    generar_menu(opciones, '5')


def accion1():
    print('Has elegido la suma')
    x=float (input('Ingrese un valor: '))
    y=float (input('Ingrese un segundo valor:'))
    print('El resultado es= ',x+y)
    from timeit import timeit
    print('Tiempo de ejecucion')
    print(timeit("'Hello, world!'.replace('hello','goodbye')"))


def accion2():
    print('Has elegido la resta')
    x=float (input('Ingrese un valor: '))
    y=float (input('Ingrese un segundo valor:'))
    print('El resultado es= ',x-y)
    from timeit import timeit
    print('Tiempo de ejecucion')
    print(timeit("'Hello, world!'.replace('hello','goodbye')"))


def accion3():
    print('Has elegido la multiplicacion')
    x=float (input('Ingrese un valor: '))
    y=float (input('Ingrese un segundo valor:'))
    print('El resultado es= ',x*y)
    from timeit import timeit
    print('Tiempo de ejecucion')
    print(timeit("'Hello, world!'.replace('hello','goodbye')"))

def accion4():
    print('Has elegido la division')
    x=float (input('Ingrese un valor: '))
    y=float (input('Ingrese un segundo valor:'))
    print('El resultado es= ',x/y)
    from timeit import timeit
    print('Tiempo de ejecucion')
    print(timeit("'Hello, world!'.replace('hello','goodbye')"))


def salir():
    print('Saliendo, Hasta pronto')
    


if __name__ == '__main__':
    menu_principal()

from timeit import timeit
print('Tiempo de ejecucion')
print(timeit("'Hello, world!'.replace('hello','goodbye')"))