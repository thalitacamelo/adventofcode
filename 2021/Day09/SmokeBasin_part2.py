import sys

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
        return 0 <= row < imax and 0 <= col < jmax and heightmap[row][col] != '9'
    return [n for n in neighbors if valid(n)]

# Build of adjacency list for graph representation
graph = {}
for row in range(imax):
    for col in range(jmax):
        if heightmap[row][col] != '9':
            graph[row, col] = listneighbors(row, col)

# Implementation of depth-first search algorithm
def dfs(visited, graph, node):
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(visited, graph, neighbour)

# Build of basins list
basins = []
allnodes = set()
for node in graph.keys():
    if node not in allnodes:
        basin = set()
        dfs(basin, graph, node)
        basins.append(basin)
        allnodes.update(basin)

basins.sort(key=len,reverse=True)

answer = len(basins[0]) * len(basins[1]) * len(basins[2])

print(answer)