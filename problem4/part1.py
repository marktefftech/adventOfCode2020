filename = 'problem4/p4_input.txt'

f = open(filename).read().strip().split('\n\n')

validCriteria = ['iyr','ecl','pid','eyr','hcl','byr','hgt']
validCount = 0

for passport in f:
    if all(fields in passport for fields in validCriteria):
        validCount += 1 

print(validCount)