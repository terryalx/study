#!/usr/bin/python3

row = 10
colum = 5

for _ in range(row):
    print(end="")
    for _ in range(colum):
        print("#", end="")
    print()

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rect(self):
        for _ in range(self.x):
            print(end="")
            for _ in range(self.y):
                print("#", end="")
            print()

r1 = Rectangle(4, 7)
r1.rect()
