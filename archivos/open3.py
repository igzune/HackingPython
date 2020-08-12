arch = open('archivo1.txt', 'a')

dedicacion = input('Dedicacion: ')
empresa = input('Empresa: ')
idioma = input('Idioma: ')

arch.write('\n')
arch.write(dedicacion)
arch.write('\n')
arch.write(empresa)
arch.write('\n')
arch.write(idioma)



arch.close()