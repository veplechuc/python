"""
     examples for object
"""
import time
import commons


# id object

a= 100
print(id(a))

# is operator
b = 100
print(a is b)
print(id(a), id(b))

b=a

print(a is b)
print(id(a), id(b))

p = [1,2]
q = [1,2]

print(p == q)
print(p is q)

print(id(p), id(q))

# p y q referencias objetos  distintos ,, no hay variables en Python sino referencias a objetos el == evalua el contenido mientras
# que el operador is define si son el mismo objeto

# pasaje de valor a una func es por valor.. si modifico el valor en la func se modifica el original
commons.banner('paso de parametros sin modificar el valor')
m = [1,2]
print('valor del array original', m)

def add_number(k):
    print('valor del array antes de la asignacion: ', k)
    k.append(25)
    print('valor del array en la funcion: ', k)

add_number(m)

print('valor del array original', m)

#ahora ojo con
commons.banner('paso de parametros cambiando el valor pero no el original')

m = [1,2]
print('valor del array original', m)

def add_number2(g):
    print('valor del array antes de la asignacion: ', g)
    g = [3,4]
    print('valor del array en la funcion: ', g)

add_number2(m)

print('valor del array original', m)

commons.banner('paso de parametros cambiando el valor original')
# se pueden cambiar los valores con
m = [1,2]
print('valor del array original', m)

def add_number3(g):
    print('valor del array antes de la asignacion: ', g)
    g[0] = 3
    g[1] = 4
    print('valor del array en la funcion: ', g)

add_number3(m)

print('valor del array original', m)


commons.banner('ojo con esto', '*')

def show_default_time(arg=time.ctime()):
    print(arg)
show_default_time()
print()
show_default_time()
commons.banner('solucion al problema anterior', '*')

def show_default_time1(arg=None):
    if arg is None:
        arg = time.ctime()
    print(arg)
show_default_time1()
x =0
while x < 9000000:
    x+=1

show_default_time1()
