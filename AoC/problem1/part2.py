filename = 'problem1/p1_input.txt'

def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets

def getInputAndSort():
    with open(filename) as f:
        content = f.readlines()
    # remove unwanted text
    content = [x.strip() for x in content] 
    content = list(map(int, content))
    content.sort()
    return content

def findPairAndPrintResult(content):
    for x in content:
        desired = 2020 - x
        result  = binary_search(content, desired)
        if result != -1:
            print(x * content[result])
            break

input_list = getInputAndSort()
results = threeNumberSum(input_list, 2020)
print(results[0][0] * results[0][1] * results[0][2])

