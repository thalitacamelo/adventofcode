with open('input.txt', 'r') as file:
    initial = map(int, file.readline().split(','))

final = initial
for i in range(80):
    temp = []
    new = 0
    for n in final:
        if n == 0:
            new += 1
            temp.append(6)
        else:
            temp.append(n-1)
    for i in range(new):
        temp.append(8)
    final = temp

print(len(final))