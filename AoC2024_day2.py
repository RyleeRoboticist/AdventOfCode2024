import os

def OpenFileToArray(dataFile):
    fileArray = [[0] * 5] * 1
    fileIndex = 0

    for line in dataFile:
        lineArray = [0] * 1
        lineArray.pop(0)
        charToConvert = ""
        for char in line:
            if not char == ' ':
                charToConvert+=char
            elif char == ' ':
                lineArray.append(int(charToConvert))
                charToConvert = ""
        lineArray.append(int(charToConvert))

        fileArray.append(lineArray)
        fileIndex+=1

    fileArray.pop(0)
    return fileArray

def CheckForSafeReport(Report):
    reportShouldBePositive = (Report[0] - Report[1]) > 0
    for point in range(len(Report)-1):
        pointDiff = Report[point] - Report[point + 1]
        if pointDiff < 0 and reportShouldBePositive:
            return False
        elif pointDiff > 0 and not reportShouldBePositive:
            return False
        elif pointDiff == 0:
            return False
        elif abs(pointDiff) > 3:
            return False
        
    return True

#A Problem Dampener would technically be something that makes the problem damp...
#like by putting it in water...
#Technically it should be a Problem Damper, but I like to keep my nomenclature nicely lined up
# #mechanicalEngineersInSoftware
def CheckForSafeReport_WithDampener(Report):
    if CheckForSafeReport(Report) == True:
        return True    
    
    isSafe = False
    for level in range(len(Report)):
        report = Report[:level] + Report[level+1:]    
        if CheckForSafeReport(report):
            isSafe = True
            break

    return isSafe


testDataFile = open(f"/home/rylee/Documents/AdventOfCode2024/Day_2/AoC2024_day2_testData.txt", "r")
testDataFileArray = OpenFileToArray(testDataFile)

safeReports = 0

for report in testDataFileArray:
    safeReports+=CheckForSafeReport(report)

print(f"Without Dampener: {safeReports}")

safeReports = 0

for report in testDataFileArray:
    safeReports+=CheckForSafeReport_WithDampener(report)

print(f"With Dampener: {safeReports}")

dataFile = open(f"/home/rylee/Documents/AdventOfCode2024/Day_2/AoC2024_day2_data.txt", "r")
dataFileArray = OpenFileToArray(dataFile)

safeReports = 0

for report in dataFileArray:
    safeReports+=CheckForSafeReport(report)

print(f"Without Dampener: {safeReports}")

safeReports = 0

for report in dataFileArray:
    safeReports+=CheckForSafeReport_WithDampener(report)

print(f"With Dampener: {safeReports}")

