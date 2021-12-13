import sys

with open('sample.txt', 'r') as file:
    lines =  file.readlines()
    lines_coordinates = []
    for line in lines:
        and1, and2 = line.strip().split(sep='->',)
        and1 = and1.split(',')
        and2 = and2.split(',')
        lines_coordinates.append((and1,and2))

coordinates = {}
for line in lines_coordinates:
    x1, y1 = map(int,line[0])
    x2, y2 = map(int,line[1])
    if x1 == x2:
        y1, y2 = sorted([y1, y2])
        for i in range(y1, y2 +1):
            if (x1, i) not in coordinates:
                coordinates[(x1, i)] = 1
            else:
                coordinates[(x1, i)] += 1
    if y1 == y2:
        x1, x2 = sorted([x1, x2])
        for i in range(x1, x2+1):
            if (i, y1) not in coordinates:
                coordinates[(i, y1)] = 1
            else:
                coordinates[(i, y1)] += 1

counts = list(coordinates.values())
resposta = len(counts) - counts.count(1)
print(resposta)

