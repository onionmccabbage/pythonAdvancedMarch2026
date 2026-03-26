from threading import Thread
from threading import Lock

# here are sme global assets
count = 0 # this could be some valuable data access mechanism
lock = Lock()

def fnA():
    '''increment the count to 100'''
    global count
    lock.acquire()
    while count <100:
        count += 1
        print(f'A increments to {count}') 
    lock.release()

def fnB():
    '''decremnt the count to -100'''
    global count
    lock.acquire()
    while count >-100:
        count -= 1
        print(f'B decrements to {count}') 
    lock.release()

if __name__ == '__main__':
    tA = Thread(target=fnA)
    tB = Thread(target=fnB)
    tB.start() # whichever thread starts first will have first access to the lock
    tA.start()
    tA.join()
    tB.join()