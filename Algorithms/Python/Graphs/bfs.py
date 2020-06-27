# there is no need for visisted array if the graph is an acyclic graph


def bfs(visited, graph, node):
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
        queue.append(neighbour)