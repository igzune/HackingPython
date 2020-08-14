class Carro(object):
    def __init__(self):
        self.color = 'Rojo'
        self.puertas = 4
        self.tipo = 'Deportivo'
    
    @classmethod
    def movilidad(cls, m):
        if m == True:
            print('\nAcelerar\n')
        else:
            print('\nFrenar\n')

def main():
    while True:
        print('1. Acelerar')
        print('2. Frenar')
        v = int(input('> '))
        
        if v == 1 :
            Carro.movilidad(True)
        else:
            Carro.movilidad(False)
    #print(Carro.color)
    #print(c.puertas)
    #print(c.tipo)

if __name__ == '__main__':
    main()