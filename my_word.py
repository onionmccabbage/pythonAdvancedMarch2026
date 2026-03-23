# We may override any of the built-in features of Python

class Word():
    '''Here we override the built=in equality operator
    in order to make a case-insensitive string comparator'''
    def __init__(self, chars):
        self.chars = chars # here we do not use any validation
    def __eq__(self, other_word):
        # we override teh built-in __eq__
        return str(self.chars).lower() == str(other_word.chars).lower()


if __name__ == '__main__':
    # hre is the typical equality operator
    s1 = 'hello'
    s2 = 'Hello'
    print(s1 == s2) # False
    # our instances
    w1 = Word('hello')
    w2 = Word('Hello')
    print(w1 == w2) # this will invoke the __eq__ method

    # __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object