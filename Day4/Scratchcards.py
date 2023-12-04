import re

fs = open('Day4/data.txt', 'r')
Lines = fs.readlines()

points = 0
scratchCards = {}
copies = []

def findWinningNumberCount(winningNums, nums):
    numCnt = 0
    for win in winningNums:
        if (win in nums):
            numCnt = numCnt + 1

    return numCnt
    
def calculateWinnings(count):
    totals = 0
    for i in range(count):
        if (i==0):
            totals = 1
        else:
            totals = totals + totals
    return totals

def createCopies(index, count):
    if (count>0):
        for i in range(count):
            copies.append(Lines[index+i])

def copyScratchcards(game, count):
    if (game in scratchCards):
        scratchCards.update({game: scratchCards[game]+1})
    else:
        scratchCards.update({game: 1})


def processCards(gameText):
    points = 0
    game = gameText.split(":")[0]
    gameNumber = int(game.split()[1].strip())
    winningNums = gameText[len(game)+1:].split("|")[0]
    nums = gameText.strip().split("|")[1]

    count = findWinningNumberCount(winningNums.strip().split(), nums.strip().split())
    points = points + calculateWinnings(count)
    createCopies(gameNumber, count)
    copyScratchcards(gameNumber, count)

for line in Lines:
    processCards(line)

while (len(copies)>0):
    currentCopy = copies.pop(0)
    processCards(currentCopy)


total = [x[1] for x in scratchCards.items()]

print(sum(total))