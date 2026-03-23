# all functions allow us to pass in positional arguments
# and/or keyword arguments

def usePA( *args ):
    '''here we expect only positional arguments (in the exact order)
    Python will always gather any positional arguments into a tuple'''
    # return f'{args[0]} {args[1]} {args[2]} {args[3]}'
    # this is useful if we do not know how many argujents may be presented
    if len(args)==0:
        return 'no arguments provided'
    elif len(args)<4:
        return args
    else:
        return 'too many arguments'

def useKW(m=5, **kwargs):
    '''Keyword arguemnts take a name and a default value (which can be overriden)
    Python will always gather the keyword arguments into a dict'''
    # return f'{kwargs["m"]} {kwargs["n"]}'
    return kwargs

def useBoth( *args, **kwargs): # NB positionl arguments must all come before the keyword arguments
    '''Any positional arguments will exist in the args tuple
    Any keyword arguments will exist in the kwargs dict'''
    return f'positional: {args} keyword: {kwargs}'

if __name__ == '__main__':
    # exercise the code
    x = usePA(3, False, 'wibbly', [4,5,6], 'other')
    print(x)
    # kw args do not have to be in order (and may take defaults)
    y = useKW(n=5, p=['dfgdf', 'asdsa',55])
    print(y, type(y))
    # using both
    z = useBoth(3,2,1, g=12, h=False, j='complex')
    print(z)