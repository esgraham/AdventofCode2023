import itertools

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
        nodeSet = line[line.index("= ")+2:].replace("(", "").replace(")", "").split(", ")
        nodes.update({key:nodeSet})
    
        
def getStepCount(node):
    steps = 0
    for direction in itertools.cycle(instruction):
        steps += 1
        next_node = nodes[node][direction]
        node = next_node
        if node.endswith('Z'):
            return steps

    


RightLeft(list(Lines[0].strip()))
DefineNodes(Lines[Lines.index("\n")+1:])

startNodes = [k for k, v in nodes.items() if k.endswith("A")]
steps = [getStepCount(node) for node in startNodes]

from math import lcm

print({lcm(*steps)})


