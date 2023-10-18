#!/usr/bin/python3

# --------------------> Class Hierarchy <--------------------

class Grandparent:
    def __init__(self, grandparent_name=None):
        self.grandparent_name = grandparent_name # Main declearator

class Parent(Grandparent):
    def __init__(self, parent_name=None):
        super().__init__(parent_name) # Passed from Main

class Child(Parent):
    def __init__(self, child_name=None):
        super().__init__(child_name) # Passed from Parent and holds the identity of the Grandparent

child00 = Child("Bob")
print(child00.grandparent_name)
# so this function sees just 1 self which is from the GrandParent


# _____________________________

class ParentNew:
    def __init__(self, name):
        self.name = name

class ChildNew(ParentNew):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

child01 = ChildNew("Alice", 25)
print(child01.name) 
print(child01.age) 


# _____________________________


