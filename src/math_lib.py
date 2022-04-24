##
# @file math_lib.py
# @brief mathematical library
# @author Magdaléna Bellayová
# @date April 2022
##

import math

pi = math.pi


def add(x, y):
    return round(x + y, 5)


def sub(x, y):
    return round(x - y, 5)


def mul(x, y):
    return round(x * y, 5)


def div(x, y):
    if y == 0:
        raise ZeroDivisionError
    return round(x / y, 5)


def mod(x, y):
    if y == 0:
        raise ZeroDivisionError
    if isinstance(x, float):
        raise ValueError
    if isinstance(y, float):
        raise ValueError
    if x >= 0 and y > 0:
        return round(x % y, 5)
    if x <= 0 and y < 0:
        return round(x % y, 5)
    if x < 0:
        return -(round((-x) % y, 5))
    if y < 0:
        return round(x % (-y), 5)


def pow(x, y):
    if y < 0:
        raise ValueError
    if isinstance(y, float):
        raise ValueError
    return round(x**y, 5)


def root(x, y):
    if x < 0 and y % 2 == 0:
        raise ValueError
    if y < 0:
        raise ValueError
    if isinstance(y, float):
        raise ValueError
    if x < 0 and y % 2 != 0:
        return -round((-x) ** (1 / y), 5)
    return round(x**(1/y), 5)


def sin(x):
    return round(math.sin(x), 5)


def cos(x):
    return round(math.cos(x), 5)


def tan(x):
    not_defined = 2*x/math.pi
    if not_defined.is_integer() and not_defined % 2 != 0:
        raise ValueError
    return round(math.tan(x),5)
    

def log(x):
    if x <= 0:
        raise ValueError
    return round(math.log10(x), 5)


def factorial(x):
    if x < 0:
        raise ValueError
    if isinstance(x, float):
        raise ValueError
    return round(math.factorial(x), 5)
