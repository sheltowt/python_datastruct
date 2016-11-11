# depth first search
# search all elements to the fullest first
# fo all the way to a leaf node first
# go back to the nearest ancestor

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            # print stack
            stack.extend(graph[vertex] - visited)
            # print stack
        print visited
    return visited

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited

print dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}