import sys
# We may import from relative locations or absolute locations
# CAREFUL - all immediate code within an imported module gets executed
from util import checkIfSquare

def doStuff():
    '''see if there are any system argument variables'''
    # All the system argument varialbes will be gathered into a list of strings
    return sys.argv # by default sys.argv will contain the name of the current module

print(f'The name of this module is {__name__}')


if __name__ == '__main__':
    print( doStuff() )
    print( checkIfSquare(36) )