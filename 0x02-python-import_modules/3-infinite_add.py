#!/usr/bin/python3
import sys


def main():
    a = 0
    for num in sys.argv[1:]:
        a += int(num)
    print("{}".format(a))


if __name__ == "__main__":
    main()
