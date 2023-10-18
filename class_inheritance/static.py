#!/usr/bin/python3

"""
A static method is a method that belongs to the class rather than an instance of the class
"""

class MyClass:

    class_variable = 10

    def __init__(self, value):
        self.instance_variable = value

    def instance_method(self):
        # This is an instance method and can access instance-specific data.
        return self.instance_variable

    @staticmethod
    def static_method():
        # This is a static method and cannot access instance-specific data.
        return MyClass.class_variable

# Creating an instance of MyClass
obj = MyClass(42)

# Accessing instance-specific data using an instance method
print(obj.instance_method())  # Output: 42

# Accessing class-specific data using a static method
print(MyClass.static_method())  # Output: 10

