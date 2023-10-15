#!/usr/bin/python3

import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

file_path = "data.json"

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file)

with open(file_path, 'r', encoding='utf-8') as file:
    load_content = json.load(file)

    try:
        if isinstance(load_content, dict):
            for key, value in load_content.items():
                print(key, ":", value)
    except FileNotFoundError:
        print("No such file..{}")
    
    for c in load_content:
        print(c)
    
    print("File:", load_content)

print(f"{file_path}")
