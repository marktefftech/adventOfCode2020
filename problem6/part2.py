import collections
import math

filename = 'problem6/p6_input.txt'

lines = [l.rstrip('\n') for l in open(filename, 'r')]

charCount = {}
groupSize = 0
allAnswers = 0

def addGroupAnswersToTotal(groupAnswersDict, groupSize):
    grpAns = 0
    for question, numAnswers in groupAnswersDict.items():
        if numAnswers == groupSize:
            grpAns += 1
    return grpAns

for line in lines:
    if len(line) == 0:
        allAnswers += addGroupAnswersToTotal(charCount, groupSize)
        charCount.clear()
        groupSize = 0
        continue

    groupSize += 1
    for char in line:
        if char not in charCount.keys():
            charCount[char] = 1
        else:
            charCount[char] += 1 

allAnswers += addGroupAnswersToTotal(charCount, groupSize)

print(allAnswers)

# for each group, throw the count of letters in a dictionary
# keep track of the number of ppl in group
# see which letters in dic have len = num of ppl in group