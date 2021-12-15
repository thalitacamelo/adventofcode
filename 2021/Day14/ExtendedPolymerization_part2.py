import sys

with open('input.txt', 'r') as file:
    template = file.readline().strip()
    file.readline()
    rules = [line.strip() for line in file.readlines() if line]
    rules = dict(line.split(' -> ') for line in rules)

count_elements = {}
for value in rules.values():
    if value not in count_elements:
        count_elements[value] = 0

count_pairs = {}
for key in rules.keys():
    if key not in count_pairs:
        count_pairs[key] = 0

def polymerization(template, rules, count_pairs, count_elements, steps):
    for i in range(len(template) - 1):
        count_pairs[template[i:i+2]] += 1
    for i in range(len(template)):
        count_elements[template[i]] += 1
    for i in range(steps):
        temp = count_pairs.copy()
        for key in temp.keys():
            j = temp[key]
            pair = key
            insert = rules[key]
            count_elements[insert] += 1 * j
            count_pairs[key] -= 1 * j
            count_pairs[pair[0]+insert] += 1 * j
            count_pairs[insert+pair[1]] += 1 * j           

polymerization(template, rules, count_pairs, count_elements, 40)

answer = max(count_elements.values()) - min(count_elements.values())
print(answer)