# We may redirect the standard streams
import sys 

class ShowStuff():
    def __init__(self, new): # runs ONCE when any instance is first created
        self.new = new
    # anything __xxx__ is part of Python
    # there are special methods available to classes:
    def dummy(self):
        print('working')
    def __enter__(self): # run every time we invoke an instance
        print('enter')
    # the three arguments here are used by exception handling within Python
    def __exit__(self, exc_type, exc, tb): # runs every time an invoked instance concludes
        print('exit')
        
if __name__ == '__main__':
    r = ShowStuff(True) # at this point an instance is created, so __init__ runs once
    with r:
        print('clever') # the __enter__ method gets called BEFORE anything in our instance is operated
        print('clever')
    with r:   
        print('clever') 
        print('clever') 
        print('clever') 
        print('clever') 
    # when we have finished using an instance, __exit__ is called
