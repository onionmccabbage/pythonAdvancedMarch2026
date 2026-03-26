# We may need to execute many test concurrently
# here we explore balancing number of threads with number of tasks
import threading
import time
import timeit
import random

# some global assets
testAvailable = []
numthreads    = 16
for _ in range(0,1000):
    t = {'id':_, 'kind':'Python'}
    testAvailable.append(t)

# a class (inheriting from Thread)
class TestRunner(threading.Thread):
    '''Each intance of this class will be executed on a worker thread
    to run one of a finite collection of tests (or other assets)'''
    tests_completed = 0 # this belongs to the class
    def __init__(self, lock, n):
        threading.Thread.__init__(self)
        self.lock = lock
        self.test_count = 0 # how many tests has this instance executed
        self.n = n
    def run(self):
        global testAvailable
        running = True
        while running:
            '''wait for a random short time then lock and run a test'''
            self.randomDelay()
            self.lock.acquire()
            if len(testAvailable)>0:
                whichTest = testAvailable.pop() # remove from the list
                # here we would invoke the test......
                self.test_count += 1
            else:
                running = False
            self.lock.release()
            # we might report the status
            print(f'Task {self.n} ran {self.test_count} tests')
    def randomDelay(self):
        '''pause execution for a short random time'''
        time.sleep(random.randint(0,4)/4) # 0, 0.25, 0.5, 0.75, 1.0

if __name__ == '__main__':
    '''exercise this module'''
    lock = threading.Lock()
    runners_list = []
    for _ in range(0, numthreads):
        runner = TestRunner(lock, _)
        runners_list.append(runner)
    start = timeit.default_timer()
    # start all the threads
    for _ in runners_list:
        _.start()
    # join all the threads
    for _ in runners_list:
        _.join()
    end = timeit.default_timer()
    print(f'Total time: {end-start}')