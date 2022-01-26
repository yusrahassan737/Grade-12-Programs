# Name: Yusra Hassan
# Date: November 4, 2021
# Description: Finds different information about a dataset
# Purpose: Data homework
# Notes: Can also add mode, answers all rounded to 2 decimal places, one version commented out at a time

import math

## Function that does the same
#def oneVarInfo(data):
    #data.sort()
    #diffSquared = []
    #outliers = []

    ## Find variance
    #mean = sum(data) / len(data)
    #for i in data:
        #diffSquared.append((i - mean) ** 2)
    #pVar = sum(diffSquared) / len(diffSquared)
    #sVar = sum(diffSquared) / (len(diffSquared) - 1)
    
    ## Find quartiles and iqr
    #term = (len(data) + 1)
    #q1 = (data[int(term / 4) - 1] + data[math.ceil(term / 4) - 1]) / 2 # subtracting 1 because of computer indexing
    #q2 = (data[int(term / 2) - 1] + data[math.ceil(term / 2) - 1]) / 2
    #q3 = (data[int(3 * term / 4) - 1] + data[math.ceil(3 * term / 4) - 1]) / 2
    #iqr = q3 - q1
    
    ## Find outliers
    #lowerFence = q1 - (1.5 * iqr)
    #higherFence = q3 + (1.5 * iqr)
    #for i in data:
        #if (i < lowerFence or i > higherFence) and str(i) not in outliers:
            #outliers.append(i)
    
    ## Returns in order: mean, pop. variance, pop. standard dev, sam. variance, sam. standard deviation, quartiles, iqr, fences, outliers
    #return mean, pVar, math.sqrt(pVar), sVar, math.sqrt(sVar), (q1, q2, q3), iqr, lowerFence, higherFence, outliers

data = []
diffSquared = []
outliers = ""
indcs = []
counts = []

# Decide whether to treat as single values or values * a frequency, then append values to a list
action = input("For frequencies of values type f, otherwise just press enter: ").lower()
dataLen = int(input("Number of different values: "))
if action == "f":
    for i in range(dataLen):
        inp = input()
        for j in range(int(inp[inp.find(" ") + 1:])):
            data.append(float(inp[:inp.find(" ")]))
else:
    for i in range(dataLen):
        data.append(float(input()))

# Find variance, mean and mode
data.sort()
mean = sum(data)/len(data)
for i in data:
    diffSquared.append((i - mean) ** 2)
    ct = data.count(i)
    if ct > 1:
        indcs.append(i)
        counts.append(ct)
mode = indcs[counts.index(sorted(counts)[-1])]
3
pVar = sum(diffSquared) / len(diffSquared)
sVar = sum(diffSquared) / (len(diffSquared) - 1)

# Find quartiles and IQR
term = (len(data) + 1)
q1 = (data[int(term / 4) - 1] + data[math.ceil(term / 4) - 1]) / 2 # subtracting 1 because of computer indexing
q2 = (data[int(term / 2) - 1] + data[math.ceil(term / 2) - 1]) / 2
q3 = (data[int(3 * term / 4) - 1] + data[math.ceil(3 * term / 4) - 1]) / 2
iqr = q3 - q1

# Find outliers
lowerFence = q1 - (1.5 * iqr)
higherFence = q3 + (1.5 * iqr)
for i in data:
    if (i < lowerFence or i > higherFence) and str(i) not in outliers:
        outliers += str(i) + ", "

# Display info
print("Mean: %.2f, Mode: %.2f" %(mean, mode))
print("Population- Variance: %.2f, Standard Deviation: %.2f" %(pVar, math.sqrt(pVar)))
print("Sample- Variance: %.2f, Standard Deviation: %.2f" %(sVar, math.sqrt(sVar)))
print("Quartiles: %.2f, %.2f, %.2f" %(q1, q2, q3))
print("IQR: %.2f, Semi IQR: %.2f " %(iqr, iqr / 2))
print("Lower fence: %.2f" %(lowerFence))
print("Higher fence: %.2f" %(higherFence))
if len(outliers) > 1:
    outliers = outliers[:-2]    
    print("Outliers: %s" %(outliers))
else:
    print("Outliers: None")
