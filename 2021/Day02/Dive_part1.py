import sys

with open('input.txt', 'r') as file:
    instructions = []
    for line in file:
        comand, number = line.split()
        instructions.append((comand,number))

horizontal = 0
depth = 0
for comand, number in instructions:
    if comand == 'forward':
        horizontal += int(number)
    elif comand == 'up':
        depth -= int(number)
    elif comand == 'down':
        depth += int(number)

result = horizontal * depth

print(result)
