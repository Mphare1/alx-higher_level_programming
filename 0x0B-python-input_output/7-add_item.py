#!/usr/bin/python3
"""AddItem module"""


import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file_name = "add_item.json"
if __name__ == "__main__":
    try:
        lis = load_from_json_file(file_name)
    except FileNotFoundError:
        lis = []
    for i, arg in enumerate(sys.argv):
        if i > 0:
            lis.append(arg)
    save_to_json_file(lis, file_name)
