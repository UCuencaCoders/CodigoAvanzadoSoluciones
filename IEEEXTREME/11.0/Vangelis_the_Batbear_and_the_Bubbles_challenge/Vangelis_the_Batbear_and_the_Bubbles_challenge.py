def dfs(neighbors, visited, start, last_visited):
    #print(f"start: {start}, last_visited: {last_visited}, visited: {visited}")
    if start in visited:
        return True
    
    visited.add(start)
    for neighbor in neighbors[start]:
        if neighbor != last_visited:
            if dfs(neighbors, visited, neighbor, start):
                return True
    return False

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    edges = list(map(str, input().split()))
    neighbors = {}

    for i in range(m):
        a = edges[2*i]
        b = edges[(2*i)+1]

        if a not in neighbors:
            neighbors[a] = []
        if b not in neighbors:
            neighbors[b] = []

        neighbors[a].append(b)
        neighbors[b].append(a)
    
    find_loop = False
    
    for node in set(edges):
        visited = set()
        if dfs(neighbors, visited, node, None):
            find_loop = True
            break
    
    print(1 if find_loop else 0)