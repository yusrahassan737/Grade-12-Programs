# Name: Yusra Hassan
# Date: November 15, 2021
# Description: Finds different information about coordinate pairs
# Purpose: Data homework
# Notes: Works for decimals too

import math

## Function that does the same
#def pairsInfo(xVals, yVals):
    ## variables
    #n = len(xVals)
    #sumX = sum(xVals)
    #sumY = sum(yVals)
    #sumXSquared = 0
    #sumYSquared = 0
    #sumXY = 0
    #corrCoeff = 0
    #corrType = ["none", "weak", "moderate", "strong", "perfect"]
    #corrSign = "positive"
    #lstSqrsA = 0
    #lstSqrsB = 0
    #lstSqrsLn = ""
    
    ## set proper values for the sum values
    #for i in range(n):
        #sumXSquared += (xVals[i]) ** 2
        #sumYSquared += (yVals[i]) ** 2
        #sumXY += (xVals[i]) * yVals[i]
    
    ## proper values for coefficient and relation-type
    #corrCoeff = ((n * sumXY) - (sumX) * (sumY))/(math.sqrt((n * sumXSquared) - (sumX) ** 2) * math.sqrt((n * sumYSquared) - (sumY) ** 2))
    #cc = abs(corrCoeff)
    
    #if cc == 0:
        #corrType = corrType[0]
    #elif cc == (1 / 3) and cc > 0:
        #corrType = corrType[1]
    #elif cc == (2 / 3) and cc >= (1 / 3):
        #corrType = corrType[2]
    #elif cc < 1 and cc >= (2 / 3):
        #corrType = corrType[3]
    #else:
        #corrType = corrType[4]
    
    #if corrCoeff < 0:
        #corrSign = "negative"
    #elif corrCoeff == 0:
        #corrSign = ""
    
    ## linear regression real values
    #lstSqrsA = (n * (sumXY) - (sumX * sumY)) / ((n * sumXSquared) - (sumX) ** 2)
    #lstSqrsB = (sumY / n) - (lstSqrsA * (sumX / n))
    #lstSqrsLn = "y = %.2fx + %.2f" %(lstSqrsA, lstSqrsB)
    
    #return corrCoeff, corrSign, corrType, lstSqrsLn



# input
xVals = []
yVals = []

while True:
    inp = input()
    if inp == "-1":
        break
    xVals.append(float(inp[:inp.find(" ")]))
    yVals.append(float(inp[inp.find(" ") + 1:]))

# variables
n = len(xVals)
sumX = sum(xVals)
sumY = sum(yVals)
sumXSquared = 0
sumYSquared = 0
sumXY = 0
corrCoeff = 0
corrType = ["none", "weak", "moderate", "strong", "perfect"]
corrSign = "positive"
lstSqrsA = 0
lstSqrsB = 0
lstSqrsLn = ""

# set proper values for the sum values
for i in range(n):
    sumXSquared += (xVals[i]) ** 2
    sumYSquared += (yVals[i]) ** 2
    sumXY += (xVals[i]) * yVals[i]

# proper values for coefficient and relation-type
corrCoeff = ((n * sumXY) - (sumX) * (sumY))/(math.sqrt((n * sumXSquared) - (sumX) ** 2) * math.sqrt((n * sumYSquared) - (sumY) ** 2))
cc = abs(corrCoeff)

if cc == 0:
    corrType = corrType[0]
elif cc == (1 / 3) and cc > 0:
    corrType = corrType[1]
elif cc == (2 / 3) and cc >= (1 / 3):
    corrType = corrType[2]
elif cc < 1 and cc >= (2 / 3):
    corrType = corrType[3]
else:
    corrType = corrType[4]

if corrCoeff < 0:
    corrSign = "negative"
elif corrCoeff == 0:
    corrSign = ""

# linear regression real values
lstSqrsA = (n * (sumXY) - (sumX * sumY)) / ((n * sumXSquared) - (sumX) ** 2)
lstSqrsB = (sumY / n) - (lstSqrsA * (sumX / n))
lstSqrsLn = "y = %.2fx + %.2f" %(lstSqrsA, lstSqrsB)

# print it all
print("The correlation coefficient is %.2f, so it is a %s, %s relation." %(corrCoeff, corrSign, corrType))
print("The equation of the line of best fit is about %s." %lstSqrsLn)
