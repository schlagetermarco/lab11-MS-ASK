"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# GitHub link:https://github.com/schlagetermarco/lab11-MS-ASK
# Partner 1 : Marco Schlageter

import math

# First example
def add(a, b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if a==0:
        raise ZeroDivisionError("Can't Divide by 0")
    return b/a

def logarithm(a,b):
    if a<=0 or a==1 or b<=0:
        raise ValueError("Invalid inputs for logarithmic function")
    return math.log(b,a)

def exponent(a,b):
    return a**b




