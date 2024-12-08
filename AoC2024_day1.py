import AoC2024_day1_data

ExampleList1_1 = [3,4,2,1,3,3]
ExampleList1_2 = [4,3,5,3,9,3]

ExampleList2_1 = [3,4,2,1,3,3,3,2,2,6,7,8,5,34,2,65,3,2,1,2,3,4,5,3,2,9,5,8,7,5,43,23,7,3,73,73,4,6,5,9,33,0,0,4]
ExampleList2_2 = [4,3,5,3,9,3,2,3,4,5,4,6,4,4,6,8,4,23,4,3,5,7,32,5,56,8,3,6,4,3,2,4,7,9,0,2,7,4,3,5,1,3,5,7]

def FindTotalDistance(List1, List2):
    if len(List1) != len(List2):
        return f"Error! Lists are not the same length: List1 Length: {len(List1)} | List2 Length: {len(List2)}"

    sortedList1 = List1.copy()
    sortedList2 = List2.copy()
    sortedList1.sort()
    sortedList2.sort()

    distance = 0

    for i in range(len(sortedList1)):
        distance += abs(sortedList1[i] - sortedList2[i])
        
    return distance

def CalculateSimilarityScore(List1, List2):
    if len(List1) != len(List1):
        return f"Error! Lists are not the same length: List1 Length: {len(List1)} | List2 Length: {len(List2)}"

    similarityScore = 0

    for i in range(len(List1)):
        anchorNumber = List1[i]
        appearanceCount = 0

        for number in List2:
            if number == anchorNumber:
                appearanceCount+=1
        
        similarityScore += anchorNumber * appearanceCount

    return similarityScore



distance = FindTotalDistance(ExampleList1_1, ExampleList1_2)

print(f"ExampleList1 Distance: {distance}")

distance = FindTotalDistance(AoC2024_day1_data.ExampleList3_1, AoC2024_day1_data.ExampleList3_2)

print(f"ExampleList3 Distance: {distance}")

similarityScore = CalculateSimilarityScore(ExampleList1_1, ExampleList1_2)

print(f"ExampleList1 Similarity Score: {similarityScore}")

similarityScore = CalculateSimilarityScore(AoC2024_day1_data.ExampleList3_1, AoC2024_day1_data.ExampleList3_2)

print(f"ExampleList3 Similarity Score: {similarityScore}")