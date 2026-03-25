from contextlib import contextmanager
import sys

# we can use the contextmanager to decorate our own functions
@contextmanager
def outputRedirect(newOutput):
    '''here we redirect the sys.stdout'''
    old = sys.stdout
    sys.stdout = newOutput
    yield # this function will generate a stream of output
    sys.stdout = old # reinstate the original output stream

if __name__ == '__main__':
    # exercise this module
    sys.stdout.write('this is a fancy way to print stuff to the console')
    # 'a' will append, 'w' will (over)write i.e. repalce the file content
    with open('my_stream.txt', 'w') as fobj:
        with outputRedirect(fobj):
            print('this ends up written into the file')
            sys.stdout.write('...more file content')
    print('back to the console')