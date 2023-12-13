fs = open('Day6/data.txt', 'r')
Lines = fs.readlines()

def calculateDistance(hold, time):
    speed = hold
    timeLeft = time-hold
    totalDistance = speed * timeLeft
    return totalDistance


def willBeatDistance(hold, time, distance):
    if (calculateDistance(hold, time))>distance:
        return True
    else:
        return False
    
def multiplyList(list):
     # Multiply elements one by one
    result = 1
    for x in list:
        result = result * x
    return result

#Part 1    
#times = re.findall(r'\d+', Lines[0])
#distances = re.findall(r'\d+', Lines[1])

#Part2
times = Lines[0][Lines[0].find(":")+1:].strip().replace(" ", "")
distances = Lines[1][Lines[1].find(":")+1:].strip().replace(" ", "")

#Converting to ints - Part 1
#times = [eval(i) for i in times]
#distances = [eval(i) for i in distances]

#Converting to ints - Part 2
times = int(times)
distances = int(distances)

#Part 1
#allRaceValues = []
#for raceNum in range(len(times)):
#    winningRaceCnt = 0
#    for holdTime in range(times[raceNum]):
#        if (willBeatDistance(holdTime, times[raceNum], distances[raceNum])):
#            winningRaceCnt = winningRaceCnt + 1
#    allRaceValues.append(winningRaceCnt)

#Part 2
winningRaceCnt = 0
for holdTime in range(times):
    if (willBeatDistance(holdTime, times, distances)):
        winningRaceCnt = winningRaceCnt + 1

print(winningRaceCnt)