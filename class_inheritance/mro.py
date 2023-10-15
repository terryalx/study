#!/usr/bin/python3

class Parent:
    def show(self):
        print("Parent class")
    def more(self):
        print("Called from the parent class")

class Child(Parent):
    def display(self):
        print("Child class")

c = Child()
c.show()  # Calls the show method of the Parent class
c.display()
c.more()

class ClassA:
    def show(self):
        print("Class A")

class ClassB:
    def show(self):
        print("Class B")

class ClassC(ClassA, ClassB):
    pass

obj = ClassC()
obj.show()  # Calls the show method of Class A because it comes first in the inheritance list
print(ClassC.mro())

class A:
    def __init__(self):
        print("Initializing A")

    def method(self):
        print("Method in A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Initializing B")

    def method(self):
        super().method()
        print("Method in B")

class C(A):
    def __init__(self):
        super().__init__()
        print("Initializing C")

    def method(self):
        super().method()
        print("Method in C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("Initializing D")

    def method(self):
        super().method()
        print("Method in D")

d = D()
d.method()
print(D.mro())
