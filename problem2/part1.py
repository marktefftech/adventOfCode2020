filename = 'problem2/p2_input.txt'

def getInputAndSort():
    with open(filename) as f:
        content = f.readlines()
        f.close()
    content = [x.strip().replace(':','') for x in content]
    return content

def findValidPasswords(file_input):
    validPasswordsCount = 0 

    for line in file_input:
        items = line.split()
        charCount = items[2].count(items[1])
        limits = items[0].split('-')
        if charCount >= int(limits[0]) and charCount <= int(limits[1]):
            validPasswordsCount+= 1
    return validPasswordsCount


file_input = getInputAndSort()
validPasswords = findValidPasswords(file_input)

print(validPasswords)

