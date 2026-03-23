# Abstract Classes can be useful
from abc import ABCMeta, abstractmethod

# by using ABCMeta, this class becomes an abstract base class
class AbstractShape(metaclass=ABCMeta):
    '''Here we declare methods and properties that need to be included in
    classes derived from this abtract class'''
    @abstractmethod # an ABC can enforce the implementation of methods
    def num_sides(self):
        pass # we do not write any implementation
    @abstractmethod
    def colour(self):
        pass


