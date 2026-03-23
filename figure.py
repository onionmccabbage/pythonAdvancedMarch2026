from concrete import Shape

class Figure(Shape):
    '''Inherit all the properties and methods from the Shape class
    Also, write a class property (not tied to any particular instance)'''
    # here is a class property
    num_instances = 0
    # I we choose, we may provide default values for any or all the properties of this class
    def __init__(self, sides=3, col='black'):
        Shape.__init__(self, sides, col) # or super().__init__(sides, col)
        Figure.count() # call the class method 
    # here is a method that belongs to this class
    def count(): # Note - we do not include 'self' for class methods
        Figure.num_instances += 1
    def howMany():
        return f'There are {Figure.num_instances} instances of the Figure class'

if __name__ == '__main__':
    # exercise the code in this module
    f1 = Figure() # this will take the default values
    print(f1)
    f2 = Figure(col='grey') # here we override the default value for col
    print(f2)
    f3 = Figure(8, 'blue')
    f3.colour = 'green'
    f1.num_sides = 99
    print(f3.num_sides, f3.colour, f1.num_sides)
    print(Figure.howMany())  # 3

