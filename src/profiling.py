import math_lib
import cProfile
def func(FILE):
    sum = 0
    for line in FILE:
        #TODO - pridat viacej funkcii z mat_lib
        sum = math_lib.scitanie(float(line),sum)
    return sum

if __name__ == '__main__' :
    print("#Test 1 - test pre 10 hodnot",end='\n\n')
    FILE = open('../profiling/10.txt')
    cProfile.run('func(FILE)')
    print("########################################################################\n")
    print("#Test 2 - test pre 100 hodnot",end='\n\n')
    FILE = open('../profiling/100.txt')
    cProfile.run('func(FILE)')
    print("########################################################################\n")
    print("#Test 3 - test pre 1 000 hodnot",end='\n\n')
    FILE = open('../profiling/1000.txt')
    cProfile.run('func(FILE)')
    print("########################################################################\n")
    print("#Test 4 - test pre 10 000 hodnot",end='\n\n')
    FILE = open('../profiling/10000.txt')
    cProfile.run('func(FILE)')