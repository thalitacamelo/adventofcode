import queue

with open('input.txt', 'r') as file:
    risks = [[int(a) for a in line.strip()] for line in file] 
    
imax = len(risks)
jmax = len(risks[0])

# Function to build a list of neighbors
def listneighbors(i,j):
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    def valid(n):
        row, col = n
        return 0 <= row < imax and 0 <= col < jmax
    return [n for n in neighbors if valid(n)]

# Build of adjacency list for graph representation
graph = {}
for row in range(imax):
    for col in range(jmax):
        graph[row, col] = listneighbors(row, col)


#Implementation of the A* algorithm
def heuristic(i, j):
   return abs(i - imax - 1) + abs(j - jmax - 1)

frontier = queue.PriorityQueue()
came_from = dict()
cost_so_far = dict()

frontier.put((heuristic(0,0), (0,0)))
came_from[(0,0)] = None
cost_so_far[(0,0)] = 0

while not frontier.empty():
    _, current = frontier.get()

    if current == (imax - 1, jmax - 1):
        break
   
    for next in graph[current]:
        ni, nj = next
        new_cost = cost_so_far[current] + risks[ni][nj]
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost + heuristic(ni, nj)
            frontier.put((priority, next))
            came_from[next] = current

lowest_total_risk = cost_so_far[(imax - 1, jmax - 1)]

print(lowest_total_risk)