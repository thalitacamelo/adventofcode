import sys

with open('input.txt', 'r') as file:
    segments = file.read().split('\n')

segments_dic = {}
for i in segments:
    key, value = i.split('|')
    segments_dic[key.strip()] = value.strip()

total = 0
for key, value in segments_dic.items():
    list_patterns = key.split()
    list_digts = value.split()
    zerosixnine = []
    twothreefive = []
    for p in list_patterns:
        if len(p) == 7:
            eight = frozenset(p)
        elif len(p) == 2:
            one = frozenset(p)
        elif len(p) == 3:
            seven = frozenset(p)
        elif len(p) == 4:
            four = frozenset(p)
        elif len(p) == 6:
            zerosixnine.append(frozenset(p))
        elif len(p) == 5:
            twothreefive.append(frozenset(p))
    a = frozenset(seven) - frozenset(one)
    for p in twothreefive:
        if seven.issubset(p):
            three = p
    for p in zerosixnine:
        if four.issubset(p):
            nine = p
    e = eight - nine
    for p in twothreefive:
        if e.issubset(p):
            two = p
        elif p != three:
            five = p
    six = five.union(e)
    for p in zerosixnine:
        if p != nine and p != six:
            zero = p
    numbers = {zero:'0', one:'1', two:'2', three:'3', four:'4', five:'5', six:'6', seven:'7', eight:'8', nine:'9'}
    number = ''.join(numbers[frozenset(d)] for d in list_digts)
    total += int(number)

print(total)