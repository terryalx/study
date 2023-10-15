#!/usr/bin/python3

class School(object):
  def __init__(self, name, card_id):
    self.name = name
    self.card_id = card_id

  def Display(self):
      print(f"Student: {self.name} | Card_Id: {self.card_id}")

# ----------------use------------------
emp = School("Adam", 901)
emp.Display()

class Students(School):
    def __init__(self, name, card_id, grade, year):
        self.grade = grade
        self.year = year
        # invoking the __init__ of the parent class
        School.__init__(self, name, card_id)

    def Print(self):
        print("School class is called here")
        print(f"Name: {self.name} | Card_Id: {self.card_id} | Grade: {self.grade} | Year: {self.year}")

# ----------------use------------------
std1 = Students("Ali", 991, "9th Grade", 2023)
# calling the baseclass method from the derived class
std1.Display()
# using the BaseClass inside the DerievedClass
std1.Print()

# *************************************************************************************************************************************************** #

class Person(object):
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	def isEmployee(self):
		return False

class Employee(Person):
	def isEmployee(self):
		return True

# ----------------use------------------
emp1 = Person("Geek1")
print(emp1.getName(), emp1.isEmployee())

emp2 = Employee("Geek2")
print(emp2.getName(), emp2.isEmployee())


