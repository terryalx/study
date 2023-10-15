#!/usr/bin/python3

import os

with open("outLoop.txt", mode="w", encoding="utf-8") as file:
    file.write("Wild\nCrazy\nAnd gangstar world\n")

with open("outLoop.txt", mode="r", encoding="utf-8")as file:
    
    linecount = 0
    num_words = -1 #to remove the added new line
    total_count = 0

    while True:    
        fileRead = file.readline()
        if not fileRead:
            print("\nNo more lines\n")
            break
        linecount += 1
        for _ in fileRead:
            total_count += 1
            num_words = len(fileRead)
        print(f"Line {linecount} : {fileRead} | Number of words:{num_words}")
        print(f"Total number of words counted plus new lines: {total_count}\n")
