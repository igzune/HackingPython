def saludo(nombre1, edad1):
    print('Hola {} tienes {} anios.'.format(nombre1, edad1))

def main():
    nombre = input('Nombre: ')
    edad = int(input('Edad: '))
    saludo(nombre, edad)
    pass


if __name__ == '__main__':
    main()