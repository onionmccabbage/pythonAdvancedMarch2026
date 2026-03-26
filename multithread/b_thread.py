# we may also use Thread with classes
from threading import Thread
import time
import random
import timeit

class MyClass(Thread):
    '''This class inherits from Thread (a thread of control)'''
    def __init__(self, n, x):
        Thread.__init__(self)
        # super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.n = n # we could write get/set methods to validate
        self.x = x
    def run(self):
        '''When this class is invoked the run method is called'''
        for _ in range(0,4):
            # NB print MUST access the main thread. it is I/O bound
            print(f'{self.n} is sleeping')
            time.sleep(random.random()*self.x)

if __name__ == '__main__':
    '''use our class as threads'''
    tA = MyClass('A', 1)
    tB = MyClass('B', 2)
    tC = MyClass('C', 0.5)
    start = timeit.default_timer()
    tA.start()
    tB.start()
    tC.start()
    tA.join()
    tB.join()
    tC.join()
    end = timeit.default_timer()
    print(f'Total time {end-start}')
