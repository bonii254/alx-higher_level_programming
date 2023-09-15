#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys
import json

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

arg_list = sys.argv[1:]
filename = "add_item.json"
try:
    prev_list = load_from_json_file(filename)
except FileNotFoundError:
    prev_list = []

new_list = []
if type(prev_list) is list:
    new_list = prev_list + arg_list
save_to_json_file(new_list, filename)
