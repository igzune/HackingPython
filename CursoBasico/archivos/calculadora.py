def multiplicacion(v1, v2):
    r = v1 * v2
    print('El resultado es', r, '\n')

def divicion(v1, v2):
    r = v1 / v2
    print('El resultado es', r, '\n')

def suma(v1, v2):
    r = v1 + v2
    print('El resultado es', r, '\n')

def resta(v1, v2):
    print('La resultado es: {}'.format(v1-v2), '\n')

def main():
    while True:
        print('Bienvenido\n')
        print('1. Suma dos numeros.')
        print('2. Resta dos numeros.')
        print('3. Multiplica dos numeros.')
        print('4. Divide dos numeros.')
        print('5. Salir.')

        opcion = int(input('Opcion :'))

        if opcion == 1:
            v1 = int(input('Primer valor: '))
            v2 = int(input('Segundo valor: '))
            suma(v1, v2)
        elif opcion == 2:
            v1 = int(input('Primer valor: '))
            v2 = int(input('Segundo valor: '))
            resta(v1, v2)
        elif opcion == 3:
            v1 = int(input('Primer valor: '))
            v2 = int(input('Segundo valor: '))
            multiplicacion(v1, v2)
        elif opcion == 4:
            v1 = int(input('Primer valor: '))
            v2 = int(input('Segundo valor: '))
            divicion(v1, v2)
        elif opcion == 5:
            exit()
        else:
            print('\n Opcion Incorrecta \n')
    pass

if __name__ == '__main__':
    main()