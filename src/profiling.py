##
# @file profiling.py
# @brief skript for profiling measures
# @author Matúš Vráblik
# @date April 2022
##

# Imports
from sys import stderr
import math_lib as ml
import cProfile


##
# @brief function using all functions from math_lib
# @param FILE file filled with values for math_lib functions
def func(FILE):
    sum = 0
    subtr = 0
    square = 0
    root = 0
    for line in FILE:
        sum = ml.add(float(line),ml.mul(sum,2))
        subtr = ml.sub(ml.mul(subtr,2),float(line))
        square = ml.add(ml.pow(float(line),2),ml.div(square,2))
        root = ml.sub(ml.root(float(line),2),ml.div(root,2))
        modulo = ml.mod(round(square),9)
        trigoniometry = ml.cos(ml.tan(ml.sin(float(line))))
        factor = ml.factorial(round(float(line)))
        logarithm = ml.log(float(line))
    return sum

if __name__ == '__main__' :
    print("#Test 1 - test 10 values",end='\n\n')
    FILE = open('../profiling/10.txt')
    cProfile.run('func(FILE)')
    print("########################################################################\n")
    print("#Test 2 - test 100 values",end='\n\n')
    FILE = open('../profiling/100.txt')
    cProfile.run('func(FILE)')
    print("########################################################################\n")
    print("#Test 3 - test 1 000 values",end='\n\n')
    FILE = open('../profiling/1_000.txt')
    cProfile.run('func(FILE)')
    print("########################################################################\n")
    print("#Test 4 - test 10 000 values",end='\n\n')
    FILE = open('../profiling/10_000.txt')
    cProfile.run('func(FILE)')
    print("########################################################################\n")
    print("#Test 5 - test 100 000 values",end='\n\n')
    FILE = open('../profiling/100_000.txt')
    cProfile.run('func(FILE)')
    print("########################################################################\n")
    print("#Test 5 - test 1 000 000 values",end='\n\n')
    FILE = open('../profiling/1_000_000.txt')
    cProfile.run('func(FILE)')