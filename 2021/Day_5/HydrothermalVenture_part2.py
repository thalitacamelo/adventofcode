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
        if y1 < y2:
            ylist = [i for i in range(y1, y2+1)]
        else:
            ylist = [i for i in range(y2, y1+1)]
            ylist.sort(reverse=True)
        for i in range(len(ylist)):
            if (x1, ylist[i]) not in coordinates:
                coordinates[(x1, ylist[i])] = 1
            else:
                coordinates[(x1, ylist[i])] += 1
    elif y1 == y2:
        if x1 < x2:
            xlist = [i for i in range(x1, x2+1)]
        else:
            xlist = [i for i in range(x2, x1+1)]
            xlist.sort(reverse=True)
        for i in range(len(xlist)):
            if (xlist[i], y1) not in coordinates:
                coordinates[(xlist[i], y1)] = 1
            else:
                coordinates[(xlist[i], y1)] += 1
    else:
        if x1 < x2:
            xlist = [i for i in range(x1, x2+1)]
        else:
            xlist = [i for i in range(x2, x1+1)]
            xlist.sort(reverse=True)
        if y1 < y2:
            ylist = [i for i in range(y1, y2+1)]
        else:
            ylist = [i for i in range(y2, y1+1)]
            ylist.sort(reverse=True)
        for i in range(len(xlist)):
            if (xlist[i], ylist[i]) not in coordinates:
                coordinates[(xlist[i], ylist[i])] = 1
            else:
                coordinates[(xlist[i], ylist[i])] += 1

counts = list(coordinates.values())
resposta = len(counts) - counts.count(1)
print(resposta)