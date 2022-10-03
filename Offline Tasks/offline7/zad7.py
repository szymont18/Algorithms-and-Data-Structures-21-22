'''

Szymon Twardosz
Każde miasto otoczone jest murem, w którym znajdują się dwie bramy ---> Każde miasto ma swoje dwie bramy: Północną i
południową. Dlatego traktuje miasta jako wierzchołki a drogi między nimi jako krawędzie.
1) Zaczynam z wierzchołka nr 0 i bramy reprezentowanej przez 0
2) Rekurencyjnie sprawdzam, czy idąc do sąsiada wierzchołka, którego aktualnie rozpatruje, jestem w stanie utworzyć cykl,
    który zawiera wszystkie miasta(na bieżąco sprawdzam które bramy mogę używać)
3) Jeżeli znajdę cykl to konczę rekurencję. W przeciwym przypadku zwracam None
Złożność O(n!)

'''

def droga( G ):

    def exist_path(G, v, u, gate, destinate_gate):
        '''
        Funkcja sprawdza czy wyjeźdzając z wierzchołka v z bramy o indeksie gate, jestem w stanie dojechać do
        wierzchołka u wjeżdzając do bramy destinate_gate
        :return: True/False
        '''

        flag1 = False
        flag2 = False
        for w in G[v][gate]:
            if w == u:
                flag1 = True
                break

        for w in G[u][destinate_gate]:
            if w == v:
                flag2 = True
                break

        if flag1 and flag2: return True
        return False

    def find_gate(G, u, v):
        '''
        Funckja zwraca do których bram można wjechać jadać z u do v
        :return: tablica bram
        '''
        gates = []
        for w in G[v][0]:
            if w == u:
                gates.append(0)
                break

        for w in G[v][1]:
            if w == u:
                gates.append(1)
                break
        return gates


    def BFS_H(G, v, gate, ile):
        '''
        :param v: wierzchołek, do którego właśnie wjechałem
        :param gate: brama którą wjechałem do wierzchołka v
        :param ile: ile wierzchołków użyłem
        :return: Zwraca reprezentację cyklu oraz flagę, która mówi czy takowy cykl został znaleziony
        '''
        nonlocal visited, Cycle, n, dest_gate

        if ile == n: #Użyto wszystkich wierzchołków
            if exist_path(G, v, 0, 1 - gate, dest_gate):
                return Cycle, True
            return [], False

        dep_gate = 1 - gate

        for w in G[v][dep_gate]:
            if not visited[w]:
                Cycle.append(w)
                visited[w] = True
                arrival_gates = find_gate(G, v, w)

                for g in arrival_gates:
                    pot_res, rec_flag = BFS_H(G, w, g, ile + 1)

                    if rec_flag:
                        return pot_res, True

                #Nic nie znaleziono
                visited[w] = False
                Cycle = Cycle[:-1] #Usuwam ostatni element

        return [], False #Zwracam, że się nie udało

    n = len(G)
    visited = [False for _ in range(n)]

    visited[0] = True
    Cycle = [0]

    dest_gate = 1
    res, flag = BFS_H(G, 0, dest_gate, 1)

    if flag:
        return res

    return None


