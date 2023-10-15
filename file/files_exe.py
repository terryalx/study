#!/usr/bin/python3

with open("newfile1.txt", "a", encoding="utf-8") as file:
    file.write("This is a script to write text to a file. \n")

print(file.closed)
