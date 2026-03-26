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
            print(f'{self.n} is sleeping')
            time.sleep(random.random()*self.x)

if __name__ == '__main__':
    '''use our class as threads'''
