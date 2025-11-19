"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# GitHub link:https://github.com/schlagetermarco/lab11-MS-ASK
# Partner 1 : Marco Schlageter

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Can't take the square root of a negative number")
        return math.sqrt(a)
    except ValueError:
        raise

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except ValueError as e:
        raise e

# First example
def add(a, b):
    return a+b

def subtract(a,b):
    return a-b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Can't Divide by 0")
    return b / a

def logarithm(a,b):
    if a<=0 or a==1 or b<=0:
        raise ValueError("Invalid inputs for logarithmic function")
    return math.log(b,a)

def exp(a, b):
    return a ** b



