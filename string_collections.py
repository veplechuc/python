#strings examples
#usar comillas simples
print(''' multi line
string''')
#es lo mismo que
print(""" multi line
string""")

#define a path wit raw string
# use 'r command
path = r'c:\ruta\a\lo\que\quiero'
print(path)
#print the character on the specific position
print(path[10], path[11])

#bytes
bytes = b'data in bytes'
print(bytes.split())

#lists - mutable objects
list1 = [1,2,3]
print(list1)
list1[2] = 'banana'
print(list1)
list1.append('otro agregado')
print(list1)
print(list('characters'))

#dictionaries mutable mapping

d = {'n': 1, 'n2':3}
print(d)
print("d['n'] = ", d['n'])

#for loop
for dat in d:
    print("key value =", dat, " value =", d[dat])

d[2] ='momo'

for dat in d:
    print("key value =", dat, " value =", d[dat])


