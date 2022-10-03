'''
Szymon Twardosz
Algorytm dla każdej krawędzi( zakłada wtedy że posiada ona najmniejszą wagę) wywołuje algorytm Kruskala do szukania MST
Zwraca najmniejszą różnicę między największym i najmniejszym elementem z znalezionych MST
'''

def highway( A ):
    # Dla Kruskala:
    #Find Union

    class Node():
        def __init__(self, val):
            self.parent = self
            self.rank = 0
            self.val = val

    def find(x):
        if x != x.parent:
            x = find(x.parent)
        return x.parent

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y: return None

        if x.rank > y.rank:
            y.parent = x

        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1

    #End Find Union

    def d(a, b):
        xa,ya = a
        xb,yb = b

        odl = ((xa - xb)**2 + (ya - yb)**2)**0.5

        if odl - int(odl) == 0: return int(odl)

        return int(odl + 1)


    def kruskal_MST(G,V, Nodes,sp):
        #1. G jest posortowane elegancko
        nonlocal res
        E = len(G)
        max_prior = 0
        min_prior = float('inf')
        MST_edges = 0 #Nie interesuje mnie droga, lecz czy stworzyłem MST

        for e in range(sp, E):
            if find(Nodes[G[e][0]]) != find(Nodes[G[e][1]]):
                union(Nodes[G[e][0]], Nodes[G[e][1]])
                MST_edges += 1
                max_prior = max(max_prior, G[e][2])
                min_prior = min(min_prior, G[e][2])

            if MST_edges == V - 1: #Udało się stworzyć MST
                return max_prior - min_prior

            if max_prior - min_prior > res:
                break

        return -1

    def cmp(e):
        return e[2]

    G = []
    V = len(A)

    if V < 2: return 0

    for v in range(V):
        for u in range(v + 1, V):
            G.append([v, u, d(A[v], A[u])])

    G.sort(key = lambda e: cmp(e)) #Sortuje RAZ po wagach
    Nodes = [Node(i) for i in range(V)]
    prev = -1

    E = len(G)
    res = float('inf')
    for e in range(E - V + 2): #Bo musi być minimalnie (V - 1) krawędzi żeby było MST
        if prev == G[e][2]: #Dla startowych o tych samych wagach będzie taki sam wynik kruskal_MST
            continue

        if G[e + V - 2][2] - G[e][2] > res: #Lepszego wyniku niż to nie uzyskam za tym obiegiem
            continue

        for i in range(V):
            Nodes[i].parent = Nodes[i]
            Nodes[i].rank = 0

        x = kruskal_MST(G, V, Nodes, e)
        if x >= 0:
            res = min(res, x)
        prev = G[e][2]

    return res

