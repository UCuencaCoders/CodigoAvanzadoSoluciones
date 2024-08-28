def dfs(visited, graph, node, anterior):
    if node in visited:
        return 1 
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour != anterior:  

            if dfs(visited, graph, neighbour, node):
                return 1
    return 0  

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ramas = list(map(int, input().split()))
    total = set(ramas)
    grafo = {}
    for i in range(m):
        r1 = ramas[2*i]
        r2 = ramas[2*i+1]
        if r1 not in grafo:
            grafo[r1] = [r2]
        else:
            grafo[r1].append(r2) 

        if r2 not in grafo:
            grafo[r2] = [r1]
        else:
            grafo[r2].append(r1) 
    visited = set()
    resultado = 0
    for j in grafo.keys():
        if resultado == 1:
            break
        if j not in visited:
            resultado = dfs(visited, grafo, j, -1)
    print(resultado)