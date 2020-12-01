filename = 'problem1/p1_input.txt'

def binary_search(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high: 
        mid = (high + low) // 2
        if arr[mid] < x: 
            low = mid + 1
        elif arr[mid] > x: 
            high = mid - 1
        else: 
            return mid 
    # If we reach here, then the element was not present 
    return -1

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
findPairAndPrintResult(input_list)

