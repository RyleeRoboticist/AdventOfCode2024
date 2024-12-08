import re

exampleInput = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def CleanMemoryString(memString):
    return re.findall("mul\([0-9]+,[0-9]+\)", memString)

def BuildMultiplyList(memList):
    multipleList = []
    for mulCommand in memList:
        numbers = [0,0]
        firstNum = re.search("[0-9]+,", mulCommand).group()
        firstNum = firstNum[0:len(firstNum)-1]                     
        numbers[0] = int(firstNum)

        secondNum = re.search(",[0-9]+", mulCommand).group()
        secondNum = secondNum[1:len(secondNum)]  
        numbers[1] = int(secondNum)

        multipleList.append(numbers)
        
    return multipleList

def ComputeMultipleListTotal(numList):
    total = 0
    for numbers in numList:
        total += (numbers[0] * numbers[1])
    
    return total

def CleanMemoryAndCalculate(memString):
    memoryCommands = CleanMemoryString(memString)
    numList = BuildMultiplyList(memoryCommands)
    return ComputeMultipleListTotal(numList)

def FindAllMulCommandLocations(memString):
    
    while (re.search("mul\([0-9]+,[0-9]+\)", memString)):
        False
        
        
def FindValidMulRanges(memString):
    startPoint = re.search("don't\(\)",memString).span()
    validRanges = memString[:startPoint[0]]
    memString = memString[startPoint[1]:]
    while (len(memString)>500):
        startRange = re.search("do\(\)",memString).span()
        stopRange = re.search("don't\(\)",memString).span()
        validRanges+= memString[startRange[1]: stopRange[0]]
        memString = memString[stopRange[1]:]
    
    return validRanges
    

print(CleanMemoryAndCalculate(exampleInput))

memoryFile = open("/home/rylee/Documents/AdventOfCode2024/Day_3/AoC2024_day3_data.txt", 'r')

total = 0
for line in memoryFile:
    total += CleanMemoryAndCalculate(line)

print(total)

memoryFile = open("/home/rylee/Documents/AdventOfCode2024/Day_3/AoC2024_day3_data.txt", 'r')

longAssString = ""
for line in memoryFile:
    longAssString+=line

validRanges = FindValidMulRanges(longAssString)

cleanedOutput = CleanMemoryAndCalculate(validRanges)

print(cleanedOutput)