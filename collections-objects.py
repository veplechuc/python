from builtins import print

import commons
#tuples

commons.banner('uso de tuplas')

p = ('hola',1, 2.3)
print('la tupla es: ', p)
print('el valor de p[1], es: ', p[1])

print()
commons.banner('string a tuplas')

commons.banner('eliminar elementos de una tupla.. no se puede hacerla lista')
p = tuple([12,3,5,6])
print('la tupla es: ', p)
print('el valor de p[1], es: ', p[1])
commons.banner('mostrar tupla usando for loop')
for dat in p:
    print(dat)

print('is 12 in the tuple? ', 12 in p)

#add/remnove
tuplex = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tuplex = list(tuplex)
for x in tuplex:
  if (x % 2 == 0):
     tuplex.pop(tuplex.index(x))
tuplex = tuple(tuplex)
print(tuplex)



#str... formatting

print('formating {0} text {1}'.format('the', '!'))

print('formating {primero} text {segundo}'.format(primero='the', segundo='!'))

tup = (23,22,55)
print('formating con los datos dde tup {tup[0]} {tup[1]} {tup[2]}'.format(tup=tup))


#range
commons.banner('uso de range')
for i in range(5):
    print(i)

print("")
print('rage converted to list')
print(list(range(5,10)))

print("")
print('rage with step converted to list')
print(list(range(5,20, 2)))

print("")
print('enumerate')
e = [55,88,999,66,77]
for  i, v  in enumerate(e):
    print('position {}  and value {}'.format(i,v))

commons.banner('list acepta negativos como indices, empieza por el final del strsing en -1','*')

cant_elem = (len(e)*-1)
print(cant_elem)
i = -1
while i >= cant_elem:
    print(e[i])
    i-=1
print("slice")

print(e[1:-1])
print("slice.. full list using lis[:]")
print(e[:])

#dictionaries
commons.banner('diccionarios')
#creacion
f = {}
dictio = {'key1': 'valor1', 'key2': ' valor 2'}

print(dictio)
print(dictio['key2'])

commons.banner('listas a diccionarios')

array = [('uno', 25), ('dos', 33)]
d = dict(array)
print(d)

#creation
result = dict(a='uno', b='dos', c='tres', d=3, e=2.366, f='un string')
print(result)
print(result['c'])
print(result['e'])
print(type(result['e']))

for dat in result:
    print('key = {key}  value= {value}'.format(key=dat,value=result[dat]))

#dictionaries
commons.banner('set')
#creacion
f = set()
f = {'key1', 'valor 2'}

print(f)
f.remove('valor 2')
print(f)
f.add(2)
f.add(1.366)
print(f)
f.update([99,6,8,'otrostring'])
print(f)

commons.banner('set usa la union, intersection, difference, simetric_difference(en uno u otro pero no es los dos conjuntos), methods ', '*')
commons.banner('set usa issubset issuperset, isdisjoint(nada en comun), methods ', '*')