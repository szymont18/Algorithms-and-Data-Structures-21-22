#Euler Cycle
def euler_cycle(G):
    '''
    Idea: 1) Wykonuje DFS, niestosując pola visited ale usuwając krawędzie po których przeszliśmy
          2) Po przetworzeniu wierzchołka dopisuje go na początek cyklu
    '''
    def find_index(Ls, v):
        for i in range(len(Ls)):
            if Ls[i] == v:
                return i

    def DFS_visit(G, v, par_v):
        nonlocal ec

        for i in range(len(G[v])):
            if G[v][i] is not None:
                x = G[v][i]

                G[v][i] = None
                ind = find_index(G[x], v)
                G[x][ind] = None

                DFS_visit(G, x, v)
            if G[v][i] == par_v:
                G[v][i] = None
                continue



        ec.append(v)

    ec = []
    #Sprawdzanie czy każdy wierzchołek ma parzysty stopień
    for grade in G:
        n = len(grade)
        if n % 2 == 1: return None

    DFS_visit(G, 0, -1)

    #Sprawdzanie niespójności grafu
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] is not None: return None

    ec.reverse()
    return ec


G = [[1,2],
     [0,2,3,6],
     [0,1,4,5],
     [1,4],
     [2,3,5,6],
     [2,4],
     [1,4]]
print(euler_cycle(G))