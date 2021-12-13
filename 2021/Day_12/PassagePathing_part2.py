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

nodes = list(graph.keys())

def list_path_iterative(start, end, lower=None):
    stack = [(start, tuple(), set(), 0)]
    paths = []

    while stack:
        (current, path, visited, repeat_count) = stack.pop()

        path = path + (current,)
        
        if current.islower():
            if current != lower:
                visited = visited.union({current})
            else:
                repeat_count += 1
                if repeat_count > 1:
                    visited = visited.union({current})

        if current == end:
            if lower is None or repeat_count > 1:
                paths.append(path)
            continue

        for n in graph[current]:
            if n not in visited:
                stack.append((n, path, visited, repeat_count))

    return paths

paths = list_path_iterative('start', 'end')
for n in nodes:
    if n not in ('start', 'end') and n.islower():
        paths.extend(list_path_iterative('start', 'end', n))

print(len(paths))