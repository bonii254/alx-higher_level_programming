#!/usr/bin/python3
"""Sript that adds all args to a python list & saves them to a file"""
import json
import sys


load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

my_obj = sys.argv
curr_list = [item for item in my_obj]

filename = "add_item.json"
try:
    prev_list = load_from_json_file(filename)
except FileNotFoundError:
    prev_list = []

new_list = []
if type(prev_list) is list:
    new_list = prev_list + curr_list[1:]
save_to_json_file(new_list, filename)
