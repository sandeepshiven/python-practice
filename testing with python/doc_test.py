def add(a,b):
    """
    >>> add(2,3)
    5
    >>> add(100,200)
    300
    """
    return a+b

def double(values):
    """ double the values in a list
    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double([True,None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
    """
    return [i*2 for i in values]


def say_hi():
    """
    >>> say_hi()
    "hi"
    """
    return "hi"

def true_that():
    """
    >>> true_that()
    True
    """
    return True


def make_dict(keys):
    """
    >>> make_dict(['a','b'])
    {'b': True, 'a': True}
    """
    return {key:True for key in keys}


