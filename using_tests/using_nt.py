# Here we use a named tuple then we will test if it operates a expected
from collections import namedtuple

# here we create a 'Task' which will be a named tuple with specific members
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
# here we declare the defaults for any new Task
Task.__new__.__defaults__ = (None, None, False, None)

# test the function
def testDefaults():
    '''creating a default named tuple should behave as expected'''
    tA = Task() # this will be a default task
    tB = Task(None, None, False, None)
    assert tA == tB

if __name__ == '__main__':
    tC = Task('Learn Python', 'Oenid', False, 3)
    print(tC)