# Name: Yusra Hassan
# Date: January 24, 2022
# Decription: Checks factors of a number
# Purpose: Reduce matrixSolver error to lowest terms
# Notes: Only for whole number floats

def lstGcfFinder(lst):
    newLst = lst[:]
    for i in range(lst.count(0)):
        newLst.remove(0)
    newLst.sort()
    for factor in range(int(newLst[0]), 0, -1):
        gcf = True
        for i in lst:
            if i % factor != 0:
                gcf = False
        if gcf == True:
            return factor
    return 1

def lstReducer(lst):
    gcf = lstGcfFinder(lst)
    newLst = lst[:]
    for i in range(len(lst)):
        newLst[i] = newLst[i] / gcf
    return newLst