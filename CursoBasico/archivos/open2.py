arch = open('wordlist.lst','r')

#print(arch.readlines())

#for l in arch.read().split('\n'):
#    print(l)

lista = arch.read().split('\n')

print(len(lista))

for i in lista:
    print(i)