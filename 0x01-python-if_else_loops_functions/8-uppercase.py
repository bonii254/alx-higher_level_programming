#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 96 < ord(letter) < 123:
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end="")
    print("")
