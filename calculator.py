
from arithmetic import *


def calculator():

    """Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""
    while True:

        user_input = raw_input("")
        tokens = user_input.split()
        operator = tokens[0]

        if operator == "q":
            break

        if len(tokens) >= 2:
            num1 = float(tokens[1])
        if len(tokens) >= 3:
            num2 = float(tokens[2])
        if len(tokens) >= 4:
            num3 = float(tokens[3])

        if operator == "+":
            print add(num1, num2)
        elif operator == "-":
            print subract(num1, num2)
        elif operator == "*":
            print multiply(num1, num2)
        elif operator == "/":
            print divide(num1, num2)
        elif operator == "square":
            print square(num1)
        elif operator == "cube":
            print cube(num1)
        elif operator == "pow":
            print power(num1, num2)
        elif operator == "mod":
            print mod(num1, num2)
        elif operator == "x+":
            print add_mult(num1, num2, num3)
        elif operator == "cubes+":
            print add_cubes(num1, num2)
        else:
            print "invalid entry"

calculator()
