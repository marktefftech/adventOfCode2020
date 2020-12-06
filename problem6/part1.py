import collections
import math

filename = 'problem6/p6_input.txt'

lines = [l.rstrip('\n') for l in open(filename, 'r')]

tmpSet = set()
runSum = 0

for line in lines:
    if len(line) == 0:
        runSum += len(tmpSet)
        tmpSet.clear()
        continue
    
    for char in line:
        tmpSet.add(char)

runSum += len(tmpSet)

print(runSum)