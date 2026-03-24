# we may access and read any text file
# Python using file access objects

def readText():
    '''retrieve text from a file'''
    try:
        # we wish to read text
        with open('my_file.txt', 'rt') as fin:
            t = fin.read() # retrieve the entire contents of the file
            # t = fin.readlines() # retrieve as a list of lines
        return t
    except Exception as err:
        print(err)

def readBytes():
    '''retrieve bytes from a file'''

if __name__ == '__main__':
    '''exercise this module'''
    r = readText()
    print(r) # the entire file contents