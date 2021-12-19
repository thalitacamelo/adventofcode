with open('input.txt', 'r') as file:
    report = [line.rstrip() for line in file]

gama = ''
epsilon = ''

for i in range(len(report[0])):
    ones = 0
    zeros = 0
    for j in range(len(report)):
        if report[j][i] == '0':
            zeros += 1
        else:
            ones += 1
    if ones > zeros:
        gama += '1'
        epsilon += '0'
    else:
        gama += '0'
        epsilon += '1'

power = int(gama, 2) * int(epsilon, 2)

print (power)
