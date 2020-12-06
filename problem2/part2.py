filename = 'problem2/p2_input.txt'

def organizeInput():
    with open(filename) as f:
        content = f.readlines()
        f.close()
    content = [x.strip().replace(':','') for x in content]
    return content

def findValidPasswords(file_input):
    validPasswordsCount = 0 

    for line in file_input:
        items = line.split()
        targetPositions = items[0].split('-')
        
        pw =  items[2]
        twoLetterValidation = pw[int(targetPositions[0])-1] + pw[int(targetPositions[1])-1]
        
        if twoLetterValidation.count(items[1]) == 1:
            validPasswordsCount+= 1
            
    return validPasswordsCount

file_input = organizeInput()
ans = findValidPasswords(file_input)
print(ans)

# 1-4 m: mrfmmbjxr