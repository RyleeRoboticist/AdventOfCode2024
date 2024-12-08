from TextFileUtils import *

SearchString = "MAS"

def BuildArrayToCheck(array, startIndex):
    charsToCheck = len(SearchString)
    index = startIndex

    charsToCheckX = 0
    charsToCheckY = 0 

    if index[1] + charsToCheck < len(array[index[0]]):
        charsToCheckX = charsToCheck
    else:
        charsToCheckX = len(array[index[0]]) - index[1] - 1

    if index[0] + charsToCheck < len(array):
        charsToCheckY = charsToCheck
    else:
        charsToCheckY = len(array) - index[0]

    dispArray = [[0]*charsToCheckX] * charsToCheckY

    for i in range(charsToCheckY):
        intermediateArray = [0] * charsToCheckX
        for y in range(charsToCheckX):
            intermediateArray[y] = array[(index[0]+i)][(index[1]+y)]
        dispArray[i] = intermediateArray

    return dispArray

def PrintTestArray(testArray):
    for i in range(len(testArray)):
        print(testArray[i])

def GenerateDirList(testArray, XMAS_MODE):
    horzOk = False
    vertOk = False
    dirs = []
    if not len(testArray) < len(SearchString):
        if not XMAS_MODE:
            dirs += [[0,1]]
            dirs += [[0,-1]]
        vertOk = True
    if not len(testArray[0]) < len(SearchString):
        if not XMAS_MODE:
            dirs += [[1,0]]
            dirs += [[-1,0]]
        horzOk = True
    if horzOk and vertOk:
        dirs += [[1,1]]
        dirs += [[-1,1]]
        dirs += [[1,-1]]
        dirs += [[-1,-1]]
        
    return dirs

def GenerateStartIndex(testArray, dir):
    arraySize = [len(testArray[0])-1, len(testArray)-1]

    startIndex = [0,0]

    if(dir[0]<0):
        startIndex[1] = arraySize[0]
    if(dir[1]<0):
        startIndex[0] = arraySize[1]

    return startIndex

def CheckDirection(testArray, startIndex, dir):
    charsToCheck = len(SearchString)
    matchesFound = 0

    index = startIndex
    checkString = ""
    while charsToCheck > 0:
        checkString += str(testArray[index[0]][index[1]])
        index[0]+=dir[1]
        index[1]+=dir[0]
        charsToCheck-=1

    if checkString == SearchString:
        matchesFound+=1
            
    return matchesFound

def CheckBlock(array, startIndex, XMAS_MODE):
    matchesFound = 0
    
    testArray = BuildArrayToCheck(array, startIndex)

    dirs = GenerateDirList(testArray, XMAS_MODE)
    
    for dir in dirs:
        matchesFound += CheckDirection(testArray, GenerateStartIndex(testArray, dir), dir)
    
    if XMAS_MODE:
        if matchesFound != 0 and matchesFound % 2 == 0:
            return 1
        return 0
    else:
        return matchesFound

def CheckPuzzle(array, XMAS_MODE):
    matches = 0
    for yPosition in range(len(array)):
        for xPosition in range((len(array[0]))-1):
            #print(f"X,Y: {xPosition},{yPosition}")
            matches += CheckBlock(array, [yPosition, xPosition], XMAS_MODE)
            #print(matches)
    return matches


SearchString = "XMAS"
XMAS_MODE = False
array = ConvertFileTo2DArray(PromptOpenFile())
print(f"Word Search Mode: {CheckPuzzle(array, XMAS_MODE)}")

SearchString = "MAS"
XMAS_MODE = True
print(f"X-MAS Mode:       {CheckPuzzle(array, XMAS_MODE)}")