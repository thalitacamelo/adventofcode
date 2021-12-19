with open('input.txt', 'r') as file:
    instructions = []
    for line in file:
        comand, number = line.split()
        instructions.append((comand,number))

horizontal = 0
depth = 0
aim = 0
for comand, number in instructions:
    if comand == 'forward':
        horizontal += int(number)
        depth += int(number) * aim
    elif comand == 'up':
        aim -= int(number)
    elif comand == 'down':
        aim += int(number)

result = horizontal * depth

print(result)