from threading import Thread
import time
# a more accurate tool to measure the passage of time is timeit
import timeit # does a good job of ignoring non-python operations

# every additional thread shares the same instance of Python

def fn(n=1):
    '''any function may be invoked on a new thread'''
    # emulate a long running piece of code
    time.sleep(1) # 1 second
    print(f'Function {n}')

if __name__ == '__main__':
    '''invoke our function on a new thread'''
    tA = Thread(target=fn, args=(1,) ) # here is a new Thread instance (a Thread of control)
    tB = Thread(target=fn, args=(2,) ) # here is a new Thread instance (a Thread of control)
    tC = Thread(target=fn, args=(3,) ) # here is a new Thread instance (a Thread of control)
    tD = Thread(target=fn, args=(4,) ) # here is a new Thread instance (a Thread of control)

    # we may use a simple timing check to measure performance
    start = timeit.default_timer()

    # we may start our additional threads
    tC.start()
    tA.start()
    tB.start()
    tD.start() # if we start additional threads, they run concurrently and do not block the main thread

    # we may choose to wait until the additonal threads have finished
    tA.join() # this will cause the main thread to wait - i.e. it is blocking
    tB.join()
    tC.join()
    tD.join()

    # also write code on the main htread
    end = timeit.default_timer()
    print(f'main thread. Total time: {end-start}')



    # remember, in normal operation the function must run consecutively
    # fn(9) # invoke the function on the main thread
    # fn(8)
    # fn(7)
    # fn(6)

