import sys

with open('sample.txt', 'r') as file:
    edges = [tuple(line.split('-')) for line in file.read().split('\n')]

graph = {}
for edge in edges:
    (paths, b) = edge
    if paths not in graph:
        graph[paths] = list()
    if b not in graph:
        graph[b] = list()

    graph[paths].append(b)
    graph[b].append(paths)

def list_paths_recursive(start, end, visited=None):

    if start == end:
        return [(end,)]

    if visited is None:
        visited = set()

    if start.islower():
        visited.add(start)

    paths = []
    for n in graph[start]:
        if n not in visited:
            for path in list_paths_recursive(n, end, set(visited)):
                paths.append((start,) + path)
    return paths

paths = list_paths_recursive('start', 'end')

print(len(paths))
