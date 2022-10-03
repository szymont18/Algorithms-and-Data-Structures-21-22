import queue

#Dijkstra Algorithms
def dijkstra(G, s, t):
    def w(v, u):
        nonlocal G
        for w in G[v]:
            if w[0] == u: return w[1]

    def relax(v, u, wage):
        nonlocal d, parent

        if d[u] > d[v] + wage:
            d[u] = d[v] + wage
            parent[u] = v


    V = len(G)
    parent = [None for _ in range(V)]
    d = [float('inf') for _ in range(V)]
    visited = [False for _ in range(V)]
    d[s] = 0

    QP = queue.PriorityQueue()
    QP.put((d[s],s)) #(0,s)

    while not QP.empty():
        prior, v = QP.get()

        visited[v] = True

        for el in G[v]:
            u, waga = el
            if not visited[u]:
                relax(v, u, waga)
                QP.put((d[u], u))

    print(d)
    path = []
    while t is not None:
        path.append(t)
        t = parent[t]
    path.reverse()
    return path

# G = [[[1,1],[2,2],[4,5]],
#      [[3,5],[5,1],[0,1]],
#      [[0,2],[5,2]],
#      [[1,5],[4,1]],
#      [[3,1],[0,5],[5,1]],
#      [[1,1],[2,2],[4,1]]]

# print(dijkstra(G,0,3))