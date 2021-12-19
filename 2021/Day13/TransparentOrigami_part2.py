with open('input.txt', 'r') as file:
    lines = list(filter(None, (line.rstrip() for line in file)))
    coordinates = []
    instructions = []
    for line in lines:
        if 'fold' in line:
            left, right = line.split('=')
            instructions.append((left[-1],int(right)))
        else:
            i, j = line.split(',')
            coordinates.append((int(i),int(j)))

coordinates = set(coordinates)

for instruction in instructions:
    axis, fold = instruction
    if axis == 'x':
        for point in list(coordinates):
            if point[0] > fold:
                x = 2 * fold - point[0]
                coordinates.add((x,point[1]))
                coordinates.remove(point)
    else:
        for point in list(coordinates):
            if point[1] > fold:
                y = 2 * fold - point[1]
                coordinates.add((point[0],y))
                coordinates.remove(point)

height = max([coordinate[1] for coordinate in coordinates]) + 1
width = max([coordinate[0] for coordinate in coordinates]) + 1

for i in range(height):
    for j in range(width):
        if (j, i) in coordinates:
            print('#', end='')
        else:
            print(' ', end='')
    print()