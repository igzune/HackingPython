arch = open('archivo1.txt', 'w')

nombre = input('Nombre: ')
edad = input('Edad: ')
pais = input('Pais: ')

arch.write(nombre)
arch.write('\n')
arch.write(edad)
arch.write('\n')
arch.write(pais)

print('E escrito los datos')

arch.close()