from array import *

filename = 'problem3/p3_input.txt'

def getInputAndSort():
    parentlist = [[]]
    with open(filename) as f:
        for line in f:
            line = list(line.rstrip())
            parentlist.append(line)
    parentlist.pop(0)
    return parentlist


file_input = getInputAndSort()
#treeCount = count_trees(file_input,3,1)
print(file_input)
