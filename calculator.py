from arithmetic import *


def calculator():

    """Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

    while True:

        user_input = raw_input("")
        tokens = user_input.split()
        operator = tokens[0]
        valid_operators = ['q', '+', '/', '*', '-', 'square', 'cube', 'mod', 'x+', 'cubes+']
        if operator not in valid_operators:
            print "Invalid operator"

        if operator == "q":
            break

        if tokens[1].isalpha() or tokens[2].isalpha() or tokens[3].isalpha():
            print "Please enter a number"
        if len(tokens) == 2:
            num1 = float(tokens[1])
            if operator == "square":
                print square(num1)
            elif operator == "cube":
                print cube(num1)
        if len(tokens) == 3:
            num1 = float(tokens[1])
            num2 = float(tokens[2])
            if operator == "+":
                print add(num1, num2)
            elif operator == "-":
                print subract(num1, num2)
            elif operator == "*":
                print multiply(num1, num2)
            elif operator == "/":
                print divide(num1, num2)
            elif operator == "pow":
                print power(num1, num2)
            elif operator == "mod":
                print mod(num1, num2)
            elif operator == "cubes+":
                print add_cubes(num1, num2)
        if len(tokens) == 4:
            num1 = float(tokens[1])
            num2 = float(tokens[2])
            num3 = float(tokens[3])
            if operator == "x+":
                print add_mult(num1, num2, num3)
        elif len(tokens) > 4 or len(tokens) < 2:
            print "invalid entry"

calculator()



# """A prefix-notation calculator."""q


# from arithmetic import *

# while True:
#     user_input = raw_input("> ")
#     tokens = user_input.split(" ")

#     if "q" in tokens:
#         print "You will exit."
#         break

#     elif len(tokens) < 2:
#         print "Not enough inputs."
#         continue

#     operator = tokens[0]
#     num1 = tokens[1]

#     if len(tokens) < 3:
#         num2 = "0"

#     else:
#         num2 = tokens[2]

#     if len(tokens) > 3:
#         num3 = tokens[3]

#     # A place to store the return value of the math function we call,
#     # to give us one clear place where that result is printed.
#     result = None

#     if not num1.isdigit() or not num2.isdigit():
#         print "Those aren't numbers!"
#         continue

#     elif operator == "+":
#         result = add(float(num1), float(num2))

#     elif operator == "-":
#         result = subtract(float(num1), float(num2))

#     elif operator == "*":
#         result = multiply(float(num1), float(num2))

#     elif operator == "/":
#         result = divide(float(num1), float(num2))

#     elif operator == "square":
#         result = square(float(num1))

#     elif operator == "cube":
#         result = cube(float(num1))

#     elif operator == "pow":
#         result = power(float(num1), float(num2))

#     elif operator == "mod":
#         result = mod(float(num1), float(num2))

#     elif operator == "x+":
#         result = add_mult(float(num1), float(num2), float(num3))

#     elif operator == "cubes+":
#         result = add_cubes(float(num1), float(num2))

#     else:
#         result = "Please enter an operator followed by two integers."

#     print result

