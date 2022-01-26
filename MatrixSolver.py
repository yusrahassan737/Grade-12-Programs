# Name: Yusra Hassan
# Date: January 20, 21, 24, 2022
# Decription: Solves matrices of different lengths using row reduced echelon form
# Purpose: Checking matrices homework 
# Notes: Currently works only for squares (n * n) and point solutions, doesn't work for fractions, not the most efficient (eliminated some cases through 1 and 0 test though), make a nicer conclusion thing, a little weird sometimes with some 0s (eg. 0 8 9 0, 0 0 3 7, 0 2 4 5), add error handling

# Improvement ideas:
## -if a line only has one variable, find that variable immediately? would that still be rref though? maybe switch it with another, if possible.
## -check if any have the scalar multiple normals before computing (compare the lines once scalar multiplied by the reciprocal of their leading variable)
## -check if already in rref?
## -ask user for approximated # of steps wanted
## -reduce equations of error lines

# Take input with some error handling
#numVars = 3
#m = 100.0
#grid = [[1, 5, -(m ** 2) + 9, - m - 4],
        #[0, -9, 2 * (m ** 2) - 17, 2 * m + 4],
        #[0, -17, 4 * (m ** 2) - 33, 4 * m + 8]]
#grid[0] = list(map(float, grid[0]))
#grid[1] = list(map(float, grid[1]))
#grid[2] = list(map(float, grid[2]))

numRows = input("Enter the number of rows: ")
while not numRows.isdigit() or int(numRows) < 2:
    numRows = input("Try again with an integer greater than 1: ")
numRows = int(numRows)
numVars = input("Enter the number of columns (excluding after the equals signs): ")
while not numVars.isdigit() or int(numVars) < 2:
    numVars = input("Try again with an integer greater than 1: ")
numVars = int(numVars)
stepsWanted = input("Type A to see all steps, N to see the answer only or anything else, for just the main steps: ").upper()

grid = [] # error handling can't really work here
print("Now, enter your space separated matrix below.")
for i in range(numRows):
    toAdd = input().split(" ")
    grid.append(list(map(float, toAdd)))

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
    for i in range(len(grd)):
        if grd[i][:-1].count(0) == numVars:
            return i
    return -1

# Actual work
msg = "The solution to the system of equations is above."
if stepsWanted != "N":
    printMat(grid)
    print("Converted to formatted matrix")

for i in range(numVars):
    zCheck = zeroVars(grid)
    if zCheck != -1:
        switch(grid, zCheck, -1)
        printMat(grid)
        msg = "There is no point solution. Above is the closest we can get there."
        break
    if grid[i][i] != 1:
        
        grid[i] = scalMult(grid[i], 1 / grid[i][i])
        if stepsWanted == "A":
            printMat(grid)
            print("The leading digit of row %i is now a 1" %i)
    for j in range(numVars):
        if j != i and grid[j] != 0:
            grid[j] = add(grid[i], grid[j], -grid[j][i])
            if stepsWanted == "A":
                printMat(grid)
                print("Performed row addition on row %i to get only 0s in the column" %(j + 1))
    if stepsWanted != "A" and stepsWanted != "N":
        printMat(grid)
if stepsWanted == "N":
    printMat(grid)
print(msg)
