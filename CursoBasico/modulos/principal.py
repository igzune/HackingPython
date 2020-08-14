import moduloCalculadora as calculadora

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
            calculadora.suma(v1, v2)
        elif opcion == 2:
            v1 = int(input('Primer valor: '))
            v2 = int(input('Segundo valor: '))
            calculadora.resta(v1, v2)
        elif opcion == 3:
            v1 = int(input('Primer valor: '))
            v2 = int(input('Segundo valor: '))
            calculadora.multiplicacion(v1, v2)
        elif opcion == 4:
            v1 = int(input('Primer valor: '))
            v2 = int(input('Segundo valor: '))
            calculadora.divicion(v1, v2)
        elif opcion == 5:
            exit()
        else:
            print('\n Opcion Incorrecta \n')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nSaliendo...')
        exit()