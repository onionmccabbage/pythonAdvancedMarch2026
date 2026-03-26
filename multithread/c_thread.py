# another approach to class-based threads
from threading import Thread
import time
import timeit
import random

class SimpleClass(): # inherits from object
    '''This class will be callable from a Thread of control'''
    def __init__(self):
        pass
    def __call__(self, n): # we my call this as an instance function
        for _ in range(0,4):
            time.sleep(random.random()*0.5)
        print(f'{n} done')

if __name__ == '__main__':
    sc = SimpleClass() 
    # we may need to work with very many threads
    thread_list = []
    for _ in range(0,8):
        thread_list.append( Thread(target=sc, args=(_,)) )
    start = timeit.default_timer()
    for _ in thread_list:
        _.start()
    for _ in thread_list:
        _.join()
    end = timeit.default_timer()
    print(f'Total time: {end-start}')
