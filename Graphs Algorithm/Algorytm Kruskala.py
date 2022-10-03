
#Kurskal Algorithm 
class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)

    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y: return  # Już są połączone

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def cmp(a):
    return a[2]


def kruskal(G):
    #Zakładam że G jest w postaci listy krawędzi
    G.sort(key =lambda x: cmp(x))
    V = 0

    for el in G:
        V = max(V,el[0], el[1])

    forest = [Node(i) for i in range(V + 1)] #Las zbiorów rozłącznych
    A = []

    for edge in G:
        v1, v2, val = edge

        x = find(forest[v1])
        y = find(forest[v2])

        if x != y: #Nie ma cyklu
            A.append(edge[:-1:])
            union(x, y)

    return A

G = [[[1,1],[2,2]],
     [[0,1],[3,1],[4,3]],
     [[0,2],[3,3]],
     [[1,1],[2,3],[4,1],[5,2]],
     [[1,3],[3,1],[5,4]],
     [[3,2],[4,4],[6,1],[7,5]],
     [[5,1],[7,2]],
     [[5,5],[6,2]]]

def change(G):
    GR = []
    for i in range(len(G)):
        for el in G[i]:
            GR.append([i] + el)
    return GR

G = change(G)
print(kruskal(G))



