# Name: Yusra Hassan
# Date: January 24, 2022
# Decription: Checks factors of a number
# Purpose: Reduce matrixSolver error to lowest terms
# Notes: 
# only for ints
def isPrime(num):
    lst = []
    for i in str(num):
        lst.append(int(i))
    if lst[-1] % 2 != 0 and sum(lst) % 3 != 0:
        return True
    else:
        return False

def reduceList(lst):
    factors = []
    for i in lst:
        check(i)