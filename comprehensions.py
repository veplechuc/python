"""
comprehension examples

"""

data = 'array de string'.split()

print([len(word) for word in data])

#iterable .. iterator

seasons =[ 1,2,3,4]

iterable = iter(seasons)

print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))