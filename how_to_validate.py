# Several ways to validate types

a = 1
b = 4.3
c = 'lunch'

print(isinstance(a, int)) # True
print(type(b)) # float
print(int(float(b)))