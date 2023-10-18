#!/usr/bin/python3

import unittest

# ------------------ testing a function output

fish_list = ["shark", "tuna", "wale"]

def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    if len(fish_list) <= 0:
        raise ValueError("No fish fount")
    return {"tank_a": fish_list}

class TestAddFishToAquarium(unittest.TestCase):
    def test_add_fish_to_aquarium_success(self):
        actual = add_fish_to_aquarium(fish_list)
        expected = {"tank_a": ["shark", "tuna", "wale"]}
        self.assertEqual(actual, expected, "Output is wrong")

# ------------------ testing a function output

def student(name="John", age=11, grade="5th"):
    return [name, age, grade]

class StudentClass:
    def __init__(self, name=None, age=None, grade=None):
        self.name, self.age, self.grade = student()
    def student_info(self):
        print(f"My name is {self.name}\nI am {self.age} years old\nGrade: {self.grade}")
    def __str__(self):
        return f"{self.name} {self.age} {self.grade}"

student1 = StudentClass(name=None, age=None, grade=None)
print(student1.name, student1.age, student1.grade)
print("test...")
student1.student_info()
print("test...")

class CheckStudent(unittest.TestCase, StudentClass):
    def test_student_name(self):
        self.assertEqual(student1.name, 'John', "Name test failed")
    def test_student_age(self):
        self.assertEqual(student1.age, 11, "Age test failed")
    def test_student_grade(self):
        self.assertEqual(student1.grade, '5th', "Grade test failed")
    def test_student_info(self):
        student1 = StudentClass(name=None, age=None, grade=None)
        print("Tessssssst...", student1.student_info())
        print(student1, "Tesssssssssssst")
        expected = "My name is John\nI am 11 years old\nGrade: 5th"
        actual = student1.student_info()
        print("Test...", student1.student_info(), "Test...")
        self.assertEqual(actual, expected, "Info test failed")
    def test_student_default(self):
        self.assertEqual(student(), ['John', 11, '5th'], "Default values test failed")

# ------------------ testing a function output
"""
All worked except tring to call the student_info method inside the CheckStudent class
i would work on it if i come back
"""
if __name__ == "__main__":
    unittest.main()
