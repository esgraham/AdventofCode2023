import re

def text2int(textnum, numwords):

    output = ""

    #Split into numbers and text
    for text in re.split('(\d+)', textnum):
        replaced_text = {}
        for word, value in numwords.items():
            if (word in text):
                allInstances = [i for i in range(len(text)) if text.startswith(word, i)]
                for index in allInstances:
                   replaced_text.update({index: value})
        
        #If the value was a number
        if (len(replaced_text)==0):
            output = output + text
        else:
            #sort the numbers and add them in order
            for number in dict(sorted(replaced_text.items())):
                output = output + str(replaced_text[number])

    return output

# Using readlines()
fs = open('Day1/data.txt', 'r')
Lines = fs.readlines()

#Configure words to numbers
units = ["one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine"]

numwords={}
for idx, word in enumerate(units):  numwords[word] = (1 + idx)

#Total Values
total = 0
 
# Strips the newline character
for line in Lines:

    #Convert word to number
    numeric_line = text2int(line.strip(), numwords)

    #Index all numbers
    idxs = [i for i in range(0, len(numeric_line)) if numeric_line[i].isdigit()]

    num = numeric_line[idxs[0]] + numeric_line[idxs[len(idxs)-1]]

    total = total + int(num)

    #Print first and last
    print(numeric_line[idxs[0]] + numeric_line[idxs[len(idxs)-1]])

print(total)