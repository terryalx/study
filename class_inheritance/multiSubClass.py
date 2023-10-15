#!/usr/bin/python3

class FatherAtt:
    def __init__(self, fatherName="Andrew"):
        self.fatherName = fatherName

    def __str__(self):
        return self.fatherName

class MotherAtt:
    def __init__(self, motherName="Venita"):
        self.motherName = motherName

    def __str__(self):
        return self.motherName

class Child(FatherAtt, MotherAtt):
    def __init__(self, fatherName, motherName, myName):
        self.myName = myName
        FatherAtt.__init__(self, fatherName)
        MotherAtt.__init__(self, motherName)

    def full_name(self):
        return f"Full Names: {self.fatherName} {self.myName} | Mother Name: {self.motherName}"

    def __str__(self):
        return self.full_name()

child1 = Child("Oshendi", "Musigu", "Nosa")

print(child1.full_name())
# set all children to inherit father's and mother's name from the base class

"""
class A:
        def __init__(self, n='Rahul'):
                self.name = n

class B(A):
        def __init__(self, roll):
                self.roll = roll

object = B(23)
print(object.name)
"""

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age):
        self.sName = name
        self.sAge = age
        # inheriting the properties of parent class
        super().__init__("Rahul", age)

    def displayInfo(self):
        print(self.sName, self.sAge)

obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()

