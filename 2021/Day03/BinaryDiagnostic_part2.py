with open('input.txt', 'r') as file:
    report = [line.rstrip() for line in file]

oxygen = list(report)
for i in range(len(report[0])):
    ones = 0
    zeros = 0
    for j in range(len(oxygen)):
        if oxygen[j][i] == '0':
            zeros += 1
        else:
            ones += 1
    if ones >= zeros:
        oxygen = [e for e in oxygen if e[i] == '1']
    elif zeros > ones:
        oxygen = [e for e in oxygen if e[i] == '0']
    if len(oxygen) == 1:
        break

carbon = list(report)
for i in range(len(report[0])):
    ones = 0
    zeros = 0
    for j in range(len(carbon)):
        if carbon[j][i] == '0':
            zeros += 1
        else:
            ones += 1
    if ones >= zeros:
        carbon = [e for e in carbon if e[i] == '0']
    elif zeros > ones:
        carbon = [e for e in carbon if e[i] == '1']
    if len(carbon) == 1:
        break

life_support = int(oxygen[0], 2) * int(carbon[0], 2)

print(life_support)