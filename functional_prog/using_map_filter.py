# functional programming can include higher-oder functions, 
# where we use one function to achieve the outcome of another
# This is especially useful with 'map' and 'filter'

def isOdd(n=2):
    '''Return True for odd values of n and False in all other cases'''
    if n/2 == n//2:
        return False # not odd
    else:
        return True  
    
def squareIt(n):
    '''return the square of n'''
    return n*n # or n**2
    
if __name__ == '__main__':
    print( isOdd(3) ) # False
    # we may have a collection of values and we need just the odd members
    d = (4,3,7,2,-7,99,1234,46,73,24)
    # Python has a filter method for collections
    odds = filter(isOdd, d)
    print( odds ) # we have a filter object
    odd_nums = [i for i in odds] # this is a list comprehension
    print( odd_nums )
    # using map to apply a function to every member of a collection
    squares = map(squareIt, d)
    print(squares)
    square_values = [i for i in squares]
    print(square_values)
