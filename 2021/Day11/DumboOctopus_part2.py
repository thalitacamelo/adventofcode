with open('input.txt', 'r') as file:
    energylevels = [list(map(int, line)) for line in file.read().split('\n')]


imax = len(energylevels)
jmax = len(energylevels[0])


def listneighbors(i,j):
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    def valid(n):
        row, col = n
        return 0 <= row < imax and 0 <= col < jmax
    return [n for n in neighbors if valid(n)]


def flash(i,j):
    energylevels[i][j] = 0
    neighbors = listneighbors(i, j)
    for n in neighbors:
        ni, nj = n
        if energylevels[ni][nj] != 0:
            energylevels[ni][nj] += 1
            if energylevels[ni][nj] > 9:
                flash(ni,nj)


for step in range(10000):
    for i in range(imax):
        for j in range(jmax):
            energylevels[i][j] += 1
    for i in range(imax):
        for j in range(jmax):
            if energylevels[i][j] > 9:
                flash(i,j)
    totalsum = sum([sum(line) for line in energylevels])
    if totalsum == 0:
        print(step + 1)
        break