import sys

with open('sample.txt', 'r') as file:
    template = file.readline().strip()
    file.readline()
    rules = [line.strip() for line in file.readlines() if line]
    rules = dict(line.split(' -> ') for line in rules)

def polymerization(template, rules, steps):
    polymer = template
    for j in range(steps):
        temp = ''
        for i in range(len(polymer) - 1):
            temp += polymer[i]
            temp += rules[polymer[i:i+2]]
        temp += polymer[-1]
        polymer = temp
    return(polymer)

polymer = polymerization(template, rules, 3)

countdict = {}
for element in polymer:
    if element in countdict:
        countdict[element] += 1
    else:
        countdict[element] = 1

answer = max(countdict.values()) - min(countdict.values())

print(answer)
print(len(polymer))
print(countdict)