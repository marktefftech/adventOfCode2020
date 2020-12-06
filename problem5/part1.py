import collections
import math

filename = 'problem5/p5_input.txt'

lines = [l.rstrip('\n') for l in open(filename, 'r')]

# part 1 in comments:
#maxSeat = 0
allSeats = set()
for line in lines:
    line = line.replace('F', '0')
    line = line.replace('B', '1')
    line = line.replace('L', '0')
    line = line.replace('R', '1')
    num = int(line, 2)
    #maxSeat = max(num, maxSeat)
    allSeats.add(num)

#print(maxSeat)
for i in range(128 * 8):
    if i not in allSeats and i+1 in allSeats and i-1 in allSeats:
        print(i)