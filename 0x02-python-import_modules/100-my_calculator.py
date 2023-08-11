#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul


def main():
    if len(sys.argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operators = ["+", "-", "*", "/"]
    if sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    c = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{} {} {} = {}".format(a, operator, c, add(a, c)))
    elif sys.argv[2] == "-":
        print("{} {} {} = {}".format(a, operator, c, sub(a, c)))
    elif sys.argv[2] == "*":
        print("{} {} {} = {}".format(a, operator, c, mul(a, c)))
    else:
        print("{} {} {} = {}".format(a, operator, c, div(a, c)))


if __name__ == "__main__":
    main()
