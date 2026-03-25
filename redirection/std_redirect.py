# We may redirect the standard streams
import sys 

class RedirectOut():
    '''When this is invoked it will redirect the standard output 
    to a different output stream
    When complete, the original output stream will be restored'''
    def __init__(self, new_stream): # runs ONCE when any instance is first created
        self.new_stream = new_stream
    # anything __xxx__ is part of Python
    # there are special methods available to classes:
    def __enter__(self): # run every time we invoke an instance
        '''swap the original stream for our new stream'''
        self.old_stream = sys.stdout
        sys.stdout = self.new_stream # here we replace the stdout
    # the three arguments here are used by exception handling within Python
    def __exit__(self, exc_type, exc, tb): # runs every time an invoked instance concludes
        '''swap the original stream back in'''
        sys.stdout = self.old_stream # replace the original stream
        
if __name__ == '__main__':
    #  streams default to 't' for text
    with open('my_file.txt', 'a') as fout:
        r = RedirectOut(fout) # at this point an instance is created, so __init__ runs once
        with r: # this invokes __enter__
            print('this text will be redirected to the file')
    print('normal service resumed')
