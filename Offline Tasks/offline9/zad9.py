'''
Szymon Twardosz
Opis: Mój algorytm polega na wywołaniu dla każdej pary wierzchołków algorytmu Edmonda - Karpa. Zwraca najlepszy przepływ
Złożoność: O(V^3 * E^2)
'''

import collections

def maxflow( G,s ):

    def find_V(G):
        max_verticle = 0
        for edge in G:
            max_verticle = max(max_verticle, edge[0], edge[1])

        return max_verticle + 1  # Indeksowanie jest od zera

    def make_residual_network(G,V):
        '''
        vector to macierz która mówi gdzie w listach sąsiedztwa znajduje się dana krawędź
        '''
        Rn =[[] for _ in range(V + 1)] #O jeden większy,gdyż potrzebuje jeszcze wierzchołka supersink
        vector = [[-1 for _ in range(V + 1)] for i in range(V + 1)]
        for edge in G:
            start,finish, flow = edge

            Rn[start].append([finish, flow])
            Rn[finish].append([start, 0])

            vector[start][finish] = len(Rn[start]) - 1
            vector[finish][start] = len(Rn[finish]) - 1

        for i in range(V):
            Rn[i].append([V, 0])
            Rn[V].append([i, 0])

            vector[i][V] = len(Rn[i]) - 1
            vector[V][i] = len(Rn[V]) - 1

        return Rn, vector

    def karp_BFS(RN, s, t, parent, vector):
        '''
        Zwraca listę parent jeżeli istniej ścieżka powiększająca, bądź pustą listę w przeciwnym wypadku
        '''

        visited = [False for _ in range(len(RN))]
        Q = collections.deque()

        Q.append(s)
        visited[s] = True

        while len(Q) > 0:
            v = Q.popleft()

            for edge in RN[v]:
                u, flow = edge

                if not visited[u] and flow > 0: #Nie usuwam krawędzi w innych funkcjach, tylko jak nie da się nimi przejchać to mają wartość 0
                    visited[u] = True
                    parent[u] = (v, flow, vector[v][u], vector[u][v])

                    if u == t: return parent #Dochodzę do ujścia

                    Q.append(u)

        return []

    def enlarging_value(parent, s, t):
        value = float('inf')

        while t != s:
            value = min(value, parent[t][1])
            t = parent[t][0]

        return value

    def rn_update(RN, parent, s, t, e_value):

        while t != s:

            RN[parent[t][0]][parent[t][2]][1] -= e_value
            RN[t][parent[t][3]][1] += e_value

            t = parent[t][0]


    def edmond_karp(RN, s, t, vector):
        parent = [(None, None) for _ in range(len(RN))]
        parent = karp_BFS(RN, s, t, parent, vector)
        flow = 0
        while len(parent) > 0:
            plus_flow = enlarging_value(parent, s, t)

            rn_update(RN, parent, s, t, plus_flow)
            flow += plus_flow

            parent = karp_BFS(RN, s, t, parent, vector)

        return flow



    V = find_V(G)

    #Teraz mam wierzchołki od 0 do V(włącznie), bo jeszcze super sink
    residual_network, vector = make_residual_network(G, V)
    best_flow = 0


    for v in range(0, V):
        for u in range(V - 1, v, -1):

            if v == s or u == s or u == v: continue

            RN = []
            for i in range(len(residual_network)):
                RN.append([])
                for el in residual_network[i]:
                    RN[i].append(el.copy())

            #Dla v
            RN[v][len(RN[v]) - 1][1] = float('inf')

            #Dla u
            RN[u][len(RN[u]) - 1][1] = float('inf')

            actual_flow = edmond_karp(RN, s, V, vector)

            best_flow = max(best_flow, actual_flow)

            #Delete
            RN[v][len(RN[v]) - 1][1] = 0
            RN[u][len(RN[u]) - 1][1] = 0

    return best_flow


