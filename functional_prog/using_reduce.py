# we need to import the reduce tool from the functionl tools library
from functools import reduce

def addThem(n,m):
    '''return the sum of n+m'''
    return n+m

if __name__ == '__main__':
    # the reduce tool lets us iteratively apply a function to the result of calling that function
    v = range(0, 10**16) # start:stop-before
    # there are no realistic restrictions on how large the values we use may be
    # The operation system will run out of resources before Python does
    # Ther are limits on the physical size of memory object, but that is bitness derived
    total = reduce(addThem, v)
    print(total)