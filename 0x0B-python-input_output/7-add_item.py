#!/usr/bin/python3
""" Module adding all arguments to a Python list, and then save
"""
import sys
import os.path


saveFile = __import__('7-save_to_json_file').save_to_json_file
loadFile = __import__('8-load_from_json_file').load_from_json_file

my_list = []
if os.path.exists("add_item.json"):
    my_list = loadFile("add_item.json")

for arg in sys.argv[1:]:
    my_list.append(arg)

saveFile(my_list, "add_item.json")
