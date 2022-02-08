# Name: Yusra Hassan
# Date: January 20, 21, 24, 2022
# Decription: Solves matrices of different lengths using row reduced echelon form
# Purpose: Checking matrices homework 
# Notes: Currently works only for numRows = numVars, doesn't work for fractions, not the most efficient (eliminated some cases through 1 and 0 test though), make a nicer conclusion thing, a little weird sometimes with some 0s (eg. [[0.0, 3.0, 9.0, 0.0], [0.0, 1.0, 3.0, 7.0], [0.0, 2.0, 4.0, 5.0]]), lstReducer has some problems with decimals

# Improvement ideas:
## -if a line only has one variable, find that variable immediately? would that still be rref though? maybe switch it with another, if possible.
## -check if any have the scalar multiple normals before computing (compare the lines once scalar multiplied by the reciprocal of their leading variable)
## -check if already in rref?
## -ask user for approximated # of steps wanted
## x-reduce equations of error lines


# Take input with some error handling
#numRows = input("Enter the number of rows: ")
#while not numRows.isdigit() or int(numRows) < 2:
    #numRows = input("Try again with an integer greater than 1: ")
#numRows = int(numRows)
#stepsWanted = input("Type A to see all steps, N to see the answer only or anything else, for just the main steps: ").upper()

#grid = [] # error handling can't really work here
#print("Now, enter your space separated matrix below.")
#for i in range(numRows):
    #toAdd = input().split(" ")
    #grid.append(list(map(float, toAdd)))
#numVars = len(grid[0]) - 1

from listFactRed import lstReducer

# Functions
def scalMult(row, scal):
    for i in range(len(row)):
        row[i] *= scal
    return row
        
def add(row1, row2, scal1 = 1): # the second row inputted is the one to change
    for i in range(len(row1)):
        row2[i] = scal1 * row1[i] + row2[i]
    return row2
        
def switch(grd, rN1, rN2):
    grd[rN1], grd[rN2] = grd[rN2], grd[rN1]
    return grd

def printMat(grd, roundBy = 2): # all that IS necessary for the intended formatting
    print()
    for i in grd:
        lineTA = "[ "
        for j in i[:-1]:
            ta = round(j, roundBy)
            if ta.is_integer():
                ta = int(ta)
            lineTA += str(ta) + " "
        tA = round(i[-1], roundBy)
        if tA.is_integer():
            tA = int(tA)
        print(lineTA[:-1] + " | " + str(tA) + " ]")

def zeroVars(grd):
    numVars = len(grd[0]) - 1
    for i in range(len(grd)):
        if grd[i][:-1].count(0) == numVars:
            return i
    return -1

# Actual work
def matrixSolve(mtrx, displayType):
    numVars = len(mtrx[0]) - 1
    msg = "The solution to the system of equations is above."
    
    if displayType != "N":
        printMat(mtrx)
        print("Converted to formatted matrix")
    
    for i in range(numVars):
        zCheck = zeroVars(mtrx)
        if zCheck != -1 or mtrx[i][i] == 0:
            switch(mtrx, zCheck, -1)
            mtrx = list(map(lstReducer, mtrx))
            if displayType != "N":
                printMat(mtrx)
            msg = "There is no point solution. Above is the closest we can get there."
            break
        if mtrx[i][i] != 1:
            mtrx[i] = scalMult(mtrx[i], 1 / mtrx[i][i])
            if displayType == "A":
                printMat(mtrx)
                print("The leading digit of row %i is now a 1" %i)
        for j in range(numVars):
            if j != i and mtrx[j] != 0:
                mtrx[j] = add(mtrx[i], mtrx[j], -mtrx[j][i])
                if displayType == "A":
                    printMat(mtrx)
                    print("Performed row addition on row %i to get only 0s in the column" %(j + 1))
        if displayType != "A" and displayType != "N":
            printMat(mtrx)
    if displayType == "N":
        printMat(mtrx)
    print(msg)
