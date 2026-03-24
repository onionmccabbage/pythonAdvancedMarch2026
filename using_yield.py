# we may write a custom generator to endlessly return useful data
import datetime
import time

def makeDateTimeStamp():
    '''Generate date-time stamp representing the moment this generator is invoked'''
    while True: # careful - this will loop endlessly
        t = datetime.datetime.now().strftime('%H:%M:%S')
        # we use the yield keyword to make this function behave as a generator
        yield t

if __name__ == '__main__':
    # we need an instance of our generator
    ts_gen = makeDateTimeStamp()
    print(type(ts_gen)) # we have a generator object
    # we may access the next available object from our generator
    t = ts_gen.__next__() # we use the instance to yield the values
    print(t)
    t2 = ts_gen.__next__() # we use the instance to yield the values
    print(t2)