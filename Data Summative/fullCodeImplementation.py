# Name: Yusra Hassan
# Date: December 2nd-8th, 2021
# Description: Code for data management summative
# Purpose: Ease in testing
# Notes: Check for coords accuracy

# Set-up
import math, pandas as pd, matplotlib.pyplot as plt

# Read files
mDf = pd.read_csv('murder_per_100000_people.csv')
hDf = pd.read_csv('hapiscore_whr.csv')
fDf = pd.read_csv('food_supply_kilocalories_per_person_and_day.csv')
pDf = pd.read_csv('corruption_perception_index_cpi.csv')
#iDf = pd.read_csv('income_per_person_gdppercapita_ppp_inflation_adjusted.csv') # this one doesn't actually have to do with the topic, it's a tester
files = [fDf, pDf, hDf, mDf]
cols = ["Country", "Food Supply", "Percieved Non-Corruption", "Happiness", "Murder Rate"]

# Functions
def pairsInfo(xVals, yVals):
    # Variables
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
    
    # Set proper values for the sum values
    for i in range(n):
        sumXSquared += (xVals[i]) ** 2
        sumYSquared += (yVals[i]) ** 2
        sumXY += (xVals[i]) * yVals[i]
    
    # Proper values for coefficient and relation-type
    corrCoeff = ((n * sumXY) - (sumX) * (sumY))/(math.sqrt((n * sumXSquared) - (sumX) ** 2) * math.sqrt((n * sumYSquared) - (sumY) ** 2))
    cc = round(abs(corrCoeff), 2)
    
    if cc == 0:
        corrType = corrType[0]
    elif cc < (1 / 3) and cc > 0:
        corrType = corrType[1]
    elif cc < (2 / 3) and cc >= (1 / 3):
        corrType = corrType[2]
    elif cc < 1 and cc >= (2 / 3):
        corrType = corrType[3]
    else:
        corrType = corrType[4]
    
    if corrCoeff < 0:
        corrSign = "negative"
    elif corrCoeff == 0:
        corrSign = ""
    
    # Linear regression real values
    lstSqrsA = (n * (sumXY) - (sumX * sumY)) / ((n * sumXSquared) - (sumX) ** 2)
    lstSqrsB = (sumY / n) - (lstSqrsA * (sumX / n))
    lstSqrsLn = "y = %.5fx + %.5f" %(lstSqrsA, lstSqrsB)
    
    return corrCoeff, corrType, corrSign, lstSqrsA, lstSqrsB, lstSqrsLn

def kHandle(data):
    lst = list(data)
    for i in range(len(lst)):
        if "k" in lst[i]:
            lst[i] = float(lst[i].replace("k", "")) * 1000
    return pd.Series(lst, index = data.keys()).astype(float)  

def drawGraph(ind, dep):
    allData.plot(kind = "scatter", x = ind, y = dep)
    fcRelInfo = pairsInfo(allData[ind].tolist(), allData[dep].tolist())
    fcRelInfo = list(fcRelInfo)
    print(fcRelInfo)
    x = sorted(allData[ind].tolist()) # largest value on the x-axis of data
    plt.plot([x[0], x[-1]], [(fcRelInfo[3] * x[0]) + fcRelInfo[4], (fcRelInfo[3] * x[-1]) + fcRelInfo[4]], label = fcRelInfo[5])
    plt.legend()
    plt.show()

# Variables
cntrs = []
allCntrs = []
fullRowInfo = []

# Clean data
for i in range(len(files)):
    files[i] = pd.Series(list(files[i]["2011"]), index = list(files[i]["country"])) # chose 2011 because it seems to have a good amount of data for each set
    files[i].dropna(inplace = True)

#files[4] = kHandle(files[4]) # manually handle "k" in income data

# Choose countries that will work for all data sets
for i in files:
    allCntrs.append(i.keys())
for i in allCntrs:
    for j in i:
        cntrs.append(j)

valids = dict.fromkeys(cntrs)
for i in dict.fromkeys(cntrs):
    if cntrs.count(i) < len(allCntrs):
        valids.pop(i)
valids = list(valids)

# Make new datasets with only those countries, create and save dataframe
for i in valids:
    add = [i]
    for j in files:
        add.append(j[i])
    fullRowInfo.append(add)
    
allData = pd.DataFrame (fullRowInfo, columns = cols)
allData.to_csv("healthAndSafety.csv")

# Display
drawGraph(cols[4], cols[1])
drawGraph(cols[2], cols[4])
drawGraph(cols[1], cols[4])
# Conclusion: Happiness and Percieved Non-Corruption are strong, Happiness and murder are weak, everything else is moderate
