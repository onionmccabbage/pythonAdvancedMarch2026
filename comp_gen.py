# comprehensions and generators

# range
r = range(0, 55, 3) # the range exists in memory, but the values do not
for _ in r:
    print(_, end=', ')
print('_________________')

# generator note the ()
g = (i*i for i in r)
print(g.__next__()) # we may pull out the next member of a generator
print(g.__next__()) # we may pull out the next member of a generator
print(g.__next__()) # we may pull out the next member of a generator

# comprehension. Note the []
c = [i*i for i in r]

print(c)