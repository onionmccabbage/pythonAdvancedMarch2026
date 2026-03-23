# we may import from one module to another

def checkIfSquare(n=9):
    '''Check if n is a square number'''
    if n**0.5 == int(n**0.5):
        return True
    else:
        return False


print(f'The name of this module is {__name__}')


if __name__ == '__main__':
    print (checkIfSquare(3))
    print (checkIfSquare(16))