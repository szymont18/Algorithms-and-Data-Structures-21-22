#DFS
def DFS(G):
    def DFSVisit(G, u):
        nonlocal time, visited, parent
        time += 1
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                print("   Wchodze do:", v)
                parent[v] = u
                DFSVisit(G, v)


    V = len(G)

    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]

    time = 0

    for u in range(V):
        if not visited[u]:
            print("Start w:", u)
            DFSVisit(G,u)
