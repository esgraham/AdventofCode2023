fs = open('AdventofCode2023/Day8/data.txt', 'r')
Lines = fs.readlines()

instruction = []
nodes = {}

def RightLeft(instructions):
    for i in instructions:
        if i=="R":
            instruction.append(1)
        else:
            instruction.append(0)

def DefineNodes(inputNodes):
    for line in inputNodes:
        line = line.strip()
        key = line[:line.index(" =")]
        nodeSet = line[line.index("= ")+2:].replace("(", "").replace(")", "").split(",")
        nodes.update({key:nodeSet})
    
def step(currentNode, i):
    currentSet = list(nodes[currentNode])
    return currentSet[i].strip()
    
def getStepCount(start, end):
    currentNode = start
    stepCnt = 0
    while currentNode != end:
        for i in instruction:
            currentNode = step(currentNode, i)
            stepCnt = stepCnt+1
            if (currentNode==end):
                break
    
    return stepCnt
        

    


RightLeft(list(Lines[0].strip()))
DefineNodes(Lines[Lines.index("\n")+1:])
steps = getStepCount("AAA", "ZZZ")

print(steps)

