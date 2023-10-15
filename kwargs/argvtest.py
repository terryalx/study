#!/usr/bin/python3

import sys

usr = input("Enter some numbers separated by spaces: ")
num = [int(n) for n in usr.split()]

# ------------------------- *args -----------------------

def sum_all(arg1, *arg2):
    sum = 0
    for n in arg2:
        sum += n
    print(arg1)
    print(arg2)
    print(sum)

    return sum


sum_all('Sum of numbers: ', *num)

# ------------------------- **kwargs -----------------------

all_names = {
        "1" : "Bisi",
        "2" : "Ben",
        "3" : "Prince"
        }

def printall(**names):
    if names is not None:
        for key, value in names.items():
            print(key, ':', value)
    return names

printall(my_names='Yemi Yusuf Afolabi')
printall(**all_names)

# ------------------------- **kwargs -----------------------

def arg(arg1, arg2, arg3):
    print("arg1", arg1)
    print("arg2", arg2)
    print("arg3", arg3)

test_arg1 = ['list', 3, 'light']

arg(*test_arg1)

# ------------------------- **kwargs -----------------------

def dict(**kwargs):
    if kwargs is None:
        return None
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    return kwargs

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

dict(**my_dict)
dict(**all_names)

# ------------------------- *args -----------------------

num1 = sys.argv[1:]
print(num1)
