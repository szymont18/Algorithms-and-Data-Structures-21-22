#Belman-Ford Algorithm
def bellman_ford(G, s): 
    def relax(v, u, w):
        nonlocal d, parent
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u

    def ver(G, d):
        for v in range(len(G)):
            for e in G[v]:
                u, w = e
                if d[u] > d[v] + w: return False
        return True


    V = len(G)
    d = [float('inf') for _ in range(V)]
    parent = [None for _ in range(V)]

    d[s] = 0

    for _ in range(V - 1):
        for v in range(V):
            for e in G[v]:
                u, w = e
                relax(u, v, w)

    flag = ver(G, d)

    return flag, d, parent


# G = [[(1, 5)],
#      [(3,3),(4,9)],
#      [(0,3), (1, -4)],
#      [(4,3), (5, 2)],
#      [(2, -1), (5, -5)],
#      [(0, 9), (2, 8)]]

# G = [[(1, -2), (2, 3)],
#      [(3, -1)],
#      [(3,5)],
#      [(0, -1)]]
# print(bellman_ford(G , 0))


