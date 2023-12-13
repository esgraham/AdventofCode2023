lines = [[int(i) for i in s.split()] for s in open('Day9/testdata.txt').read().split('\n') if s.strip()]

def getDifference(numbers):
    if sum(i != 0 for i in numbers) == 0:
        return 0
    difference = [int(numbers[x+1])-int(numbers[x]) for x in range(len(numbers)-1)]
    
    return numbers[-1] + getDifference(difference)

total = []
total2 = []

for numbers in lines:
    total.append(getDifference(numbers))
    total2.append(getDifference(numbers[::-1]) )

print(sum(total))
print(sum(total2))

