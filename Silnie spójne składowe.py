def sss(G):
    '''
    Program zwraca tablice silnie spójnych składowych
    '''
    def DFS_visit(G, v, visited):
        nonlocal s_tab, time, times

        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                DFS_visit(G, u, visited)

        time += 1
        times[v] = time
        s_tab.append(v)

    def create_rev_graph(G):
        V = len(G)
        GR = [[] for _ in range(V)]

        for i in range(V):
            for j in range(len(G[i])):
                GR[G[i][j]].append(i)
        return GR

    #Main
    V = len(G)
    times = [-1 for _ in range(V)]
    time = 0
    visited = [False for _ in range(V)]
    s_tab = []

    for v in range(V):
        if not visited[v]:
            visited[v] = True
            DFS_visit(G, v, visited)

    s_tab = []
    res = []
    visited2 = [False for _ in range(V)]
    GR = create_rev_graph(G)

    vector = [i for i in range(V)]
    vector.sort(key=lambda x: times[x], reverse=True)

    for i in range(V):
        if not visited2[vector[i]]:
            visited2[vector[i]] = True
            s_tab = []

            DFS_visit(GR, vector[i], visited2)

            res.append(s_tab)

    return res


G = [[1],
     [2],
     [0,3],
     [4,5],
     [5],
     [6],
     [3,4],
     [9],
     [7],
     [8],
     []]

print(sss(G))

