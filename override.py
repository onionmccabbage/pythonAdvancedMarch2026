from concrete import Shape

# We may extend any of the built in classes of Python
class MyTuple(tuple):
    '''This class now has all the properties and methods of tuple'''
    pass

# we may iherit from our own classes
class Rectangle(Shape):
    '''All the properties and methods of Shape are now available here'''
    def __init__(self, colour):
        # we often call the __init__ of the parent class
        # we may do this by calling super() and NOT provining self
        super().__init__(4, colour) # pass a fixed value for num_sides
    # we need to ensure the num_sdes remains fixed at 4 (for any Rectangle)
    @property
    def num_sides(self):
        return self.__num_sides # calls the parent method
    @num_sides.setter
    def num_sides(self, new_sides):
        # NB all rectangles MUST have 4 sides
        self.__num_sides = 4 # ensure it is always 4 for every rectangle

if __name__ == '__main__':
    # here we may exercise the code within this module
    m1 = MyTuple((3,4,5,7))
    print(m1, type(m1))
    # some rectangles
    r1 = Rectangle('yellow')
    r2 = Rectangle('brown')
    r1.num_sides = 8
    r1.colour = 'ochre'
    print(r1, r2)