from threading import Thread
import time

# every additional thread shares the same instance of Python

def fn(n=1):
    '''any function may be invoked on a new thread'''
    # emulate a long running piece of code
    time.sleep(1) # 1 second
    print(f'Function {n}')

if __name__ == '__main__':
    '''invoke our function on a new thread'''
    tA = Thread(target=fn, args=(1,) ) # here is a new Thread instance (a Thread of control)


    # we may start our additional threads
    tA.start()

