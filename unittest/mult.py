#!/usr/bin/python3

"""
Testing here..
>>> mult(2, 3)
6
"""

def mult(a, b):
    """
    >>> mult(2, 2)
    4
    """
    ans = a * b
    return ans

if __name__ == "__main__":
    import doctest
    doctest.testmod()
