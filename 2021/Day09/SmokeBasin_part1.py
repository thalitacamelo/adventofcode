with open('input.txt', 'r') as file:
    heightmap = file.read().split('\n')

# i = row, j = column
imax = len(heightmap)
jmax = len(heightmap[0])

# A list of neighbors is build for each number
def listneighbors(i,j):
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    def valid(n):
        row, col = n
        return 0 <= row < imax and 0 <= col < jmax
    return [n for n in neighbors if valid(n)]

# If a number is lower than all his neighbors, we increase sumrisk with number + 1
sumrisck = 0
for i in range(imax):
    for j in range(jmax):
        neighbors = listneighbors(i, j)
        low = True
        for neighbor in neighbors:
            ni, nj = neighbor
            if heightmap[i][j] >= heightmap[ni][nj]:
                low = False
                break
        if low:
            sumrisck += int(heightmap[i][j]) + 1

print(sumrisck)