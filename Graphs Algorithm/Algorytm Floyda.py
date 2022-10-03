
#Floyd-Warshall algorithm
def floyd_warshall(G):
    #Zakładam że nie ma ujemnych cykli, ale czy tak jest? - Trzeba sprawdzać
    #Jeżeli wyjdzie, że z wierzchołka A do A da się dojść szybciej niż kosztem 0 => Istnieje ujemny cykl

    V = len(G)
    d = [[float('inf') for _ in range(V)] for i in range(V)]
    parent = [[None for _ in range(V)] for i in range(V)]

    #Wstępne wypełnianie
    for i in range(V):
        d[i][i] = 0

        for e in G[i]:
            u, w = e
            d[i][u] = w
            parent[i][u] = i

    for k in range(1, V):
        for v in range(V):
            for u in range(V):
                if d[v][k] + d[k][u] < d[v][u]:
                    d[v][u] = d[v][k] + d[k][u]
                    parent[v][u] = k

    return d, parent


# G = [[(1,2),(2,-4)],
#      [(2,3),(3,3)],
#      [(3,-1),(4,-4)],
#      [(4,2)],
#      [(0,4)]]

# G =[[(1, 5),(3, 8),(2,4)],
#     [(0,-4),(2,-2),(4,5)],
#     [(3,5),(4,2)],
#     [(4,-1),(1,2),(0,-1)],
#     [(2,4),(3,2)]]

# d, parent = floyd_warshall(G)
# print("D")
# for el in d:
#     print(el)

# print("_____________")
# print("Parent")
# for el in parent:
#     print(el)