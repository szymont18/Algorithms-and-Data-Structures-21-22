import queue
#Prim's Algorithm
def prim(G):
    #G jest w postaci list wierhołków

    Q = queue.PriorityQueue()

    wages = [float('inf') for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    visited = [False for _ in range(len(G))]

    Q.put((0, 0)) #(priorytet,wierzchołek)


    while not Q.empty():
        prior, v = Q.get()
        print("Prior = ", prior, "v = ", v)

        visited[v] = True

        for el in G[v]:
            u, w = el
            if not visited[u]:
                if wages[u] > w:
                    wages[u] = w
                    parent[u] = v
                    Q.put((wages[u], u))


    res = []
    for i in range(len(parent)):
        if parent[i] is not None:
            res.append((i,parent[i]))

    return res



G = [[[1,1],[2,2]],
     [[0,1],[3,1],[4,3]],
     [[0,2],[3,3]],
     [[1,1],[2,3],[4,1],[5,2]],
     [[1,3],[3,1],[5,4]],
     [[3,2],[4,4],[6,1],[7,5]],
     [[5,1],[7,2]],
     [[5,5],[6,2]]]
print(prim(G))