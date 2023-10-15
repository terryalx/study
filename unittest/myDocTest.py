#!/usr/bin/python3

"""
>>> sum(2, 3)
5
"""

def sum(a, b):
    """
    >>> sum(3, 3)
    6
    """
    total = a+b
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()
