d = dict(nombre='alumno', plataforma='Udemy', edad=18)

print(d)
print(d['nombre'])

a = d.items()
print(a)

b = d.copy()
print(b)

for i in d.keys():
    print('{} su valor es: {}'.format(i,d[i]))