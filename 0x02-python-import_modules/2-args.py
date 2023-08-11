#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv[1:])))
        for index, val in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(index, val))


if __name__ == "__main__":
    main()
