# doctest is a simple low-level tesing tool built in to Python
import doctest

def square(n=3):
    '''return the square of n
    >>> square(2)
    4
    >>> square(-3)
    9
    >>> square() # this should use the default
    9
    '''
    return n*n


if __name__ == '__main__':
    c = square(8)
    print(c)
    # implement doctest
    # NB we coudl wrap this in a contextmanager so all doctest results could be captured in a log 
    doctest.testmod(verbose=True)