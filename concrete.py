# here we declare concrete classes, in this case derived from an abstract class
from absract import AbstractShape

# We do not have to use abstraction to make classes
# but if we do, we may enforce features of the class
class Shape(AbstractShape): # NB by default everything in Python is an Object
    '''We must implement what the Abstract class enforces'''
    def __init__(self, sides, col): # we choose to pass in arguments
        # the __init__ will be executed once, when any instance is created
        self.num_sides = sides # this will invoke the setter method for num_sides
        self.colour    = col
    @property # the property decorator makes this method behave as a property getter
    def num_sides(self): # class methods MUST take 'self' as the first argument
        return self.__num_sides # note the __
    @num_sides.setter # here we make the method behave as a setter for a property
    def num_sides(self, new_sides):
        '''We may validate that the new_sides is within bounds'''
        if type(new_sides) == int and new_sides>0:
            # We use __ to 'mangle' a property name, so it's not visible outside the class
            self.__num_sides = new_sides
        else:
            raise TypeError('Number of sides must be a positive integer')

    # @property
    def colour(self):
        return self.__colour
    

if __name__ == '__main__':
    # make instances
    s1 = Shape(3, 'blue')
    print(s1.num_sides) # calls the getter method for __num_sides