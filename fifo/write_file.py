# All file access is I/O bound
# NB every time we use print() our code is I/O bound
# Also every input() is I/O bound

def writeText(t):
    '''commit some text to a text file'''
    try:
        # fout = open('my_file.txt', 'at')
        # fout.write(t) # NB this does not append a new line character
        # fout.write('\n') # we may choose to append a new line character, or anything else
        # fout.close() # tidy up
        #                        'a' will append 't' for text
        with open('my_file.txt', 'at') as fout:
            fout.write(t) # NB this does not append a new line character
            fout.write('\n') # we may choose to append a new line character, or anything else
    except Exception as err:
        print(err)

def writeBytes(b):
    '''commit some byte data to a file'''
    try: #                    'a' append 'b' bytes
        with open('my_bytes', 'ab') as fout:
            fout.write(b)
    except Exception as err:
        print(err)

if __name__ == '__main__':
    '''exercise this module'''
    writeText('some plain text.')