filename = 'problem3/p3_input.txt'

fileInput = [line for line in open(filename,"rt").read().split()]

# parameter type annotations increased readability, but do no affect functionality
def count(inputArr:list,stepsRight:int,stepsDown:int)->int:
  width = len(inputArr[0])
  x = 0
  treeCount = 0
  for i in range(0,len(inputArr),stepsDown):
    if inputArr[i][x]=='#':
      treeCount += 1
    x = (x+stepsRight)%width
  return treeCount

print( count(fileInput,3,1) )

p = 1
for r,b in ((1,1),(3,1),(5,1),(7,1),(1,2)):
  p *= count(fileInput,r,b)
print( p )