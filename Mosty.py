
#Finding bridges
def bridge(G):
    def DFS_visit(G, v):
        nonlocal d, color, low, parent,time
        time += 1
        d[v] = time
        low[v] = d[v]

        for u in G[v]:
            if color[u] == -1:
                parent[u] = v
                color[u] = 0

                DFS_visit(G, u)

                low[v] = min(low[v], low[u])
            elif color[u] == 0 and parent[v] != u:
                low[v] = min(low[v], d[u])

            else: continue

        color[v] = 1 #Wierzchołek przetworzony



    V = len(G)
    d = [float('inf') for _ in range(V)]
    low = [float('inf') for _ in range(V)]
    color = [-1 for _ in range(V)]
    parent = [None for _ in range(V)]
    '''
    color == a) -1 wierzcholek nieodwiedzony
             b) 0 wierzchołek w trakcie przetwarzania
             c) wierzchołek po przetworzeniu
    '''
    time = 0
    color[0] = 0
    DFS_visit(G, 0)

    #Sprawdzanie czy graf spójny

    for el in color:
        if el == -1: return None
        '''
        Jakiś wierzchołek nie został odwiedzony więc należy zwrócić None
        '''

    bridges = []
    for i in range(1, V):
        if d[i] == low[i]:
            bridges.append((i,parent[i]))

    return bridges

# G = [[1,4],
#      [2,0],
#      [3,1],
#      [2,5],
#      [5,0],
#      [3,4]]
# print(bridge(G))