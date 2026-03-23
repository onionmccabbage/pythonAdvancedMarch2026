import sys

def doStuff():
    '''see if there are any system argument variables'''
    # All the system argument varialbes will be gathered into a list of strings
    return sys.argv # by default sys.argv will contain the name of the current module


if __name__ == '__main__':
    print( doStuff() )