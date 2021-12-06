import sys

with open('sample.txt', 'r') as file:
    initial = map(int, file.readline().split(','))

numberscount = {}
for i in range(9):
    numberscount[i] = 0

for n in initial:
    numberscount[n] += 1

for i in range(256):
    temp = dict((i, numberscount[(i+1) % 8]) for i in range(9))
    temp[6] += numberscount[0]
    numberscount = temp

total = 0
for key, value in numberscount.items():
    total += value
print(total)