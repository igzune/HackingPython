# classmethod
# staticmethod
# property

class prueba1(object):
    def __init__(self, radio):
        self.radio = radio
        pass

    @classmethod # Nos ayuda a usar una funcion sin que antes la clase sea atribuida a un objeto
    def saludo(cls, nombre):
        print('Hola {}'.format(nombre))
    
    @staticmethod # Hace que la funcion no necesite argumento
    def saludoStatic():
        print('Bienvenido')
    
    @property # Trabajar con funciones como si fueran variables
    def areaCirculo(self):
        return 3.1416*(self.radio**2)


def main():
    n = input('Nombre: ')
    prueba1.saludo(n)

    c = prueba1(5)
    c.saludoStatic()

    area = c.areaCirculo
    print(area)

if __name__ == "__main__":
    main()