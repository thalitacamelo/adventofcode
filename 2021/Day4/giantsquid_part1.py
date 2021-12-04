import sys

with open('sample.txt', 'r') as file:
    numbers = file.readline().strip().split(sep=',')
    file.readline()
    boards = file.read().split('\n\n')

coordinates = []
for board in boards:
    coordinate = {}
    i = -1
    for row in board.split('\n'):
        keys = row.split()
        i += 1
        j = 0
        for k in keys:
            coordinate[k] = (i,j)
            j += 1
    coordinates.append(coordinate)

row_columns = []
for i in range(len(boards)):
    row = [0] * 5
    column = [0] * 5
    row_columns.append((row,column))

flag = None
for number in numbers:
    for i in range(len(boards)):
        c = coordinates[i]
        rowscore, colscore = row_columns[i]
        if number in c:
            row, column = c[number]
            del c[number]
            rowscore[row] += 1
            colscore[column] += 1
            if 5 in rowscore or 5 in colscore:
                flag = [number, c]
                break
    if flag is not None:
        break

number, c = flag
sum = 0
for key in c:
    sum += int(key)
score = int(number) * sum
print(score)
