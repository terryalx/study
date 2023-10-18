#!/usr/bin/python3

#Base = __import__('base').Base
from base import Base

class Rectangle(Base):
    def __init__(self, id):
        Base.__init__(self, id)

rr = Rectangle(id='Terry')
print(rr.id)

# checking -- [import vrs __import__]
