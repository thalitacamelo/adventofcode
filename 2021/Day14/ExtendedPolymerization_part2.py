import sys

with open('input.txt', 'r') as file:
    template = file.readline().strip()
    file.readline()
    rules = [line.strip() for line in file.readlines() if line]
    rules = dict(line.split(' -> ') for line in rules)

count_elements = dict((value, 0) for value in rules.values())

count_pairs = dict((key, 0) for key in rules.keys())

def polymerization(template, rules, count_pairs, count_elements, steps):
    for i in range(len(template) - 1):
        count_pairs[template[i:i+2]] += 1

    for letter in template:
        count_elements[letter] += 1
        
    for i in range(steps):
        new_count_pairs = dict((key, 0) for key in rules.keys())
        for pair, count in count_pairs.items():
            insert = rules[pair]
            count_elements[insert] += count
            new_count_pairs[pair[0]+insert] += count
            new_count_pairs[insert+pair[1]] += count
        count_pairs = new_count_pairs          

polymerization(template, rules, count_pairs, count_elements, 40)

answer = max(count_elements.values()) - min(count_elements.values())
print(answer)