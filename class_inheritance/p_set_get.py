#!/usr/bin/python3

# --------------------------------------------------- (_getter and setter_)

"""
access private att __att
get__att
set__att
The getter allows us to retrieve the private attribute's value, and the setter permits us to change the value.

The use of getter and setter methods offers several advantages:
Encapsulation: It hides the internal implementation details of the class and provides a controlled interface for accessing and modifying data.
Data Validation: You can implement checks and constraints in the setter method to ensure that the data remains valid.
Flexibility: It allows you to change the internal representation of data without affecting external code that uses the getter and setter methods.
Read-Only or Write-Only Properties: You can choose to create read-only or write-only attributes by omitting the setter or getter method, respectively.
Logging and Side Effects: You can add logging or other side effects when data is accessed or modified.
Using private instance attributes and getter/setter methods is a good practice for maintaining clean and organized code and ensuring proper data management within your classes.
"""

class car:
    def __init__(self, model=None, id=None):
        self.__model = model
        self.id = id

    def get_model(self): #get and return the __attr
        #call this method to return __attr if not you'll get an error
        #__attr cannot be accessed directly but through this class
        return self.__model

    def set_model(self, value): #set value to the __attr
        self.__model = value

print("#-------------------------------------------------------------(Getter and Setter)")
p1 = car('Toyota', 'XL329')
print(p1.get_model())
try:
    print(p1.model)
except AttributeError:
    print("AttributeError: model is a private attribute")

# --------------------------------------------------- (_@property getter, setter and deleter_)

class service(car):
    def __init__(self, model=None, date=None):
        self._date = date #protected attribute
        super().__init__(model)

    @property
    def date(self): #defining method like it is an attribute with the @property
        return self._date

    @date.setter
    def date(self, value): #define a setter for date to set att
        self._date = value

    @date.deleter
    def date(self):
        print("Deleting last serviced date")
        del self._date

print("#-------------------------------------------------------------(@property - Getter, Setter and Detter)")
s1 = service("Prado", 2009)
print(s1.date)
print(s1.get_model())
del s1.date

# --------------------------------------------------- (_@property getter, setter and deleter_)

class Service:
    def __init__(self, date=None):
        self._date = date  # Protected attribute

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if value is None or value > 2023:
            print("Enter a valid last serviced date")
        elif value <= (2023 - 2):  # Check if the date is more than 2 years ago
            print("Your car needs to be serviced")
        else:
            self._date = value

    @date.deleter
    def date(self):
        print("Deleting last serviced date")
        del self._date

print("#-------------------------------------------------------------(@property - Getter, Setter and Detter)")
s1 = Service(2020)
print(s1.date)  # Output: 2020
s1.date = 2022
print(s1.date)  # Output: 2022
s1.date = 2019  # Triggers the servicing message
del s1.date

# --------------------------------------------------- (_@property getter, setter and deleter_)

class Service:
    def __init__(self, date=None):
        self._date = date  # Protected attribute

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if value is None:
            print("Enter a valid last serviced date")
        elif isinstance(value, str) and any(char.isdigit() for char in value):
            # Check if it's a string and contains at least one digit
            if int(value) > 2023:
                print("Your car needs to be serviced")
            else:
                self._date = value
        else:
            print("Enter a valid last serviced date")

    @date.deleter
    def date(self):
        print("Deleting last serviced date")
        del self._date

print("#-------------------------------------------------------------(@property - Getter, Setter and Detter)")
s1 = Service("sf363f")
print(s1.date)  # Output: sf363f
s1.date = "2022"  # Triggers the servicing message
s1.date = None  # Triggers the "Enter a valid last serviced date" message
del s1.date

