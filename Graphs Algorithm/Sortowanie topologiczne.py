
#Topological Sort
def topological_sort(G):
    '''
    Idea: Uruchomić DFS na dowolnym wierzchołku.
    Po jego przetworzeniu dodać do listy posortowanym topologicznie
    Jeżeli nie wszstkie zostały przetworzone to zaczynaj od innego nieprzetworzonego jeszcze wierzchołka
    '''
    #Graf G - Implementacja listowa

    def DFS_visit(G, v):
        nonlocal colors, ts

        colors[v] = 0

        for u in G[v]:
            if colors[u] == -1:
                DFS_visit(G, u)

        colors[v] = 1
        ts.append(v)

    n = len(G)
    colors = [-1 for _ in range(n)]
    '''
    colors określa w jakim stanie aktualnie jest wierzchołek
    a) -1 wierzchołek wogóle nie został jeszcze odwiedzony
    b) 0 wierzchołek jest w trakcie przetwarzania
    c) 1 wierzchołek przetworzony
    '''

    ts = [] #topological sorted array

    for v in range(n):
        if colors[v] == -1:
            DFS_visit(G, v)

    ts.reverse()
    return ts


# G = [[1, 2, 5],
#      [2, 4],
#      [],
#      [],
#      [3, 6],
#      [4],
#      []]
# print(topological_sort(G))