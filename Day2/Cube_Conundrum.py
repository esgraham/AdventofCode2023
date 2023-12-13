# Using readlines()
fs = open('Day2/data.txt', 'r')
Lines = fs.readlines()

maxNumRed = 12
maxNumGreen = 13
maxNumBlue = 14

gameTotal = 0

for line in Lines:
    isValidGame = True

    gameNum = line.split(":")[0]
    games = line[line.find(":") + 1:].strip().split(";")

    colorCount = {"blue": 0, "green": 0, "red": 0}

    for game in games:
        cubes = game.split(",")

        for cube in cubes:
            cubeInfo = cube.strip().split(" ")
            currentCount = colorCount[cubeInfo[1]]
            if (currentCount<int(cubeInfo[0])):
                colorCount.update({cubeInfo[1]: int(cubeInfo[0])})
        
        #if (colorCount["blue"]>maxNumBlue) or (colorCount["red"]>maxNumRed) or (colorCount["green"]>maxNumGreen):
        #    isValidGame = False
    
    powerValue = colorCount["blue"]*colorCount["green"]*colorCount["red"]

    gameTotal = gameTotal + powerValue

    #if (isValidGame):
    #    gameTotal = gameTotal + int(gameNum.split(" ")[1])

print(gameTotal)