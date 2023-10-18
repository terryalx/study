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

class grandchildren(FatherAtt, MotherAtt):
    def __init__(self, myName, fatherName, motherName):
        self.myName = myName
        FatherAtt.__init__(self, fatherName)  # Call the constructor of FatherAtt
        MotherAtt.__init__(self, motherName)  # Call the constructor of MotherAtt

    def __str__(self):
        return f"Full Names: father: {self.fatherName} | myName: {self.myName}"

gc = grandchildren('Femi', 'Ben', 'Tumi')
print(gc)
print(gc.motherName) 
print(gc.fatherName) 
print(gc.myName)





