import re
fs = open('Day5/testdata.txt', 'r')
Lines = fs.readlines()

mapValues = {}
locationMap = {}

def getCategories():
    categoryList = [x.strip() for x in Lines if x.strip().endswith("map:")]
    return categoryList

def getRanges(category):
    categoryIndex = Lines.index(category + "\n")
    nextCategoryIndex = Lines.index("\n", categoryIndex)
    r = []
    for i in range(categoryIndex+1, nextCategoryIndex):
        numbers = re.findall(r'\d+', Lines[i])
        r.append([int(x)for x in numbers])
    
    return {category:r}

def findLocation(ranges, fromItem):
    toItem = fromItem
    for x in ranges:
        source = x[1]
        destination = x[0]
        rangeLength = x[2]
        if (fromItem in range(source, source + rangeLength)):
            toItem = (destination-source) + fromItem
        
    return toItem

#Part 2
def MapRangetoCategory(fromItem, toItem, itemRanges):
    allRanges=[]
    category = ("{0}-to-{1} map:").format(fromItem, toItem)

    for items in itemRanges:
        for x in mapValues[category]:
            valueList=[]
            a=int(x[0])-int(x[1])
            sourceRange = range(int(x[1]), int(x[1])+int(x[2]))

            if (items.start in sourceRange):
                valueList.append(items.start+a)
                if (items.stop in sourceRange):
                    valueList.append(items.stop+a)
                else:
                    valueList.append(sourceRange.stop+a)
            elif (items.stop in sourceRange):
                valueList.append(sourceRange.start+a)
                if (items.stop in sourceRange):
                    valueList.append(items.stop+a)
                else:
                    valueList.append(sourceRange.stop+a)
            
            if (len(valueList)>0):
                allRanges.append(range(valueList[0], valueList[1]))
        
        if (len(valueList)==0):
            allRanges.append(range(items.start, items.stop))
    
    return allRanges

def mapValuestoCategory(fromItem, toItem, items):
    category = ("{0}-to-{1} map:").format(fromItem, toItem)
    valueList = []
    for i in items:
        valueList.append(findLocation(mapValues[category], int(i)))

    return valueList



categoryList = getCategories()
seeds = re.findall(r'\d+', Lines[0])

for category in categoryList:
    mapValues.update(getRanges(category))

#Part 2
itemMap = []
locationMap = []
for i in range(0, len(seeds), 2):
    seed = range(int(seeds[i]), int(seeds[i])+int(seeds[i+1]))
    #itemMap = MapRangetoCategory("seed", "soil", [seed])
    itemMap2 = mapValuestoCategory("seed", "soil", list(seed))
    #itemMap = MapRangetoCategory("soil", "fertilizer", itemMap)
    itemMap2 = mapValuestoCategory("soil", "fertilizer", itemMap2)
    #itemMap = MapRangetoCategory("fertilizer", "water", itemMap)
    itemMap2 = mapValuestoCategory("fertilizer", "water", itemMap2)
    #itemMap = MapRangetoCategory("water", "light", itemMap)
    itemMap2 = mapValuestoCategory("water", "light", itemMap2)
    #itemMap= MapRangetoCategory("light", "temperature", itemMap)
    itemMap2 = mapValuestoCategory("light", "temperature", itemMap2)
    #itemMap = MapRangetoCategory("temperature", "humidity", itemMap)
    itemMap2 = mapValuestoCategory("temperature", "humidity", itemMap2)
    locationMap.extend(mapValuestoCategory("humidity", "location", itemMap2))
    

print(min(locationMap)+1)
    