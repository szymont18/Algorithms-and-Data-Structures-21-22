import queue
#BFS
def BFS(G, s):
    V = len(G) #Ile jest wierchołków

    visited = [False for _ in range(V)]
    d = [float('inf') for _ in range(V)] #Odległość od punktu s
    parent = [None for _ in range(V)]

    visited[s] = True
    d[s] = 0

    Q = queue.Queue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()

        for v in G[u]:

            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.put(v)

