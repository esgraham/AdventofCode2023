import re

fs = open('Day3/data.txt', 'r')
Lines = fs.readlines()

cols = len(Lines[0].strip())
rows = len(Lines)
grid = []
numberPositions = []
gearPosition={}

gears = {}

row = 0

def getNumberIndexes(line):
    indexes = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
    numbers = re.findall(r'\d+', line)
    return [indexes, numbers]

def setGears(currentRow, currentCol, num):
    gear = str(currentRow) + "," + str(currentCol)
    gearCnt = 0
    if gear in gears:
        gearCnt = gears[gear]
    gears.update({gear : gearCnt+1})
    return [gear, num]
   

def getGridValue(currentRow, indexes, number):
    values = []
    gearsList = []

    startCol = indexes[0]
    endCol = indexes[1]

    #Check current row
    if (startCol!=0):
        if (grid[currentRow][startCol-1]=="*"):
            values.append(grid[currentRow][startCol-1])
            gearsList.extend(setGears(currentRow, startCol-1, number))
    if (endCol!=cols):
        if (grid[currentRow][endCol]=="*"):
            values.append(grid[currentRow][endCol])
            gearsList.extend(setGears(currentRow, endCol, number))

    #Set default values to get the right amount of chars in rows
    if (startCol==0):
        startCol=startCol+1
    if (endCol==cols):
        endCol = endCol-1
    
    #Range starts at value given and stops and value given-1
    #Check row above 
    if (currentRow!=0):
        values.extend([grid[currentRow-1][i] for i in range(startCol-1, endCol+1)])
        gear = [[currentRow-1, i] for i in range(startCol-1, endCol+1) if grid[currentRow-1][i] =="*"]
        if (len(gear)>0):
            gearsList.extend(setGears(gear[0][0], gear[0][1], number))

    #Check row below
    if (currentRow!=rows-1):
        values.extend([grid[currentRow+1][i] for i in range(startCol-1, endCol+1)])
        gear = [[currentRow+1, i] for i in range(startCol-1, endCol+1) if grid[currentRow+1][i] =="*"]
        if (len(gear)>0):
             gearsList.extend(setGears(gear[0][0], gear[0][1], number))
    
    return gearsList

def findGear(validGears):
    allGears = []
    #Loop 
    for gearKey in gears:
        amount = 1
        if gears[gearKey]==2:
            gearList = [item[1] for item in validGears if item[0]==gearKey]
            for item in gearList:
                amount = amount * int(item)
            
            allGears.append(amount)
        if gears[gearKey]>2:
            a = "Ahh!"
        
    return allGears


def findSymbols():
    validNumbers=[]
    for indexes in numberPositions:
        currentRow = indexes[1]
        index = indexes[0][0]
        numbers = indexes[0][1]
        for i in range(len(index)):
            values = getGridValue(currentRow, index[i], numbers[i])
            #l = [item for item in values if item!="." and not item.isdigit()]
            if (len(values)>0):
                validNumbers.append(values)

    g = findGear(validNumbers)
    return g
           



#Create grid
for line in Lines:
    line = line.strip()
    grid.append([line[i] for i in range(cols)])

    #Determine numbers per line
    indexes = getNumberIndexes(line)
    if (len(indexes[0])>0):
        numberPositions.append([indexes, row])

    row = row + 1

#Search for symbols nearby
validNums = findSymbols()

#Add the numbers together
totalNum = sum(validNums)


print(totalNum)