#Szymon Twardosz
'''
1)Tworzę tablicę vector w której umieszczam indeksy budynków z tablicy T. Następnie sortuje tą tablice według klucza
vector[i] < vector[j] wtw T[i][2] < T[j][2]
2)Tworzę dwie tablice pomocniczę - P, gdzie P(i) mówi, który pierwszy (względem vectora) budynek  mogę wybudować, tak aby
                                    budynki i i j na siebie nie nachodziły
                                 - F, gdzie F(i,x) to tablica która przechowuje na pierwszym indeksie maksymalną liczbę
                                    którą mogą pomieścić i - pierwszych budynków( względem vectora) i z ceną x. Na drugim
                                    informację potrzebne do odzyskania odpowiedzi(**)

3)Idąc po tablicy wpisuje kolejne elementy wg wzoru
F(i,x)=max(F(i-1,s), F(P[i], s - koszt[i]) + liczba_studentów[i]) w moim algorytmie z przesunięciem o jeden indeks

4)Korzystając z (**) znajduje odpowiedź i zwracam posortowaną listę

Złożność - O(nlogn + np)
'''



def select_buildings(T,p):
    n = len(T)
    vector = [i for i in range(n)]  # Indeksuje od 0
    vector.sort(key=lambda x: T[x][2])  # Lista służąca jako wskaźnik na indeksy

    P = [0 for i in range(n)]  # P(i) - który budynek j (j<i, j maksymalne) mogę wybudować, aby budynki nie nachodziły na siebie
    F = [[[0, -1] for i in range(p + 1)] for j in range(n + 1)]

    # Funkcja F(i,x) mówi ile maksymalnie mogę mieć studentów korzystając z pierwszysych i przedziałów(względem vector)
    # korzystając z maksymalnie x przedmiotów

    def price(T):
        return T[0] * (T[2] - T[1])

    def find_g(i):  # Można przerobić na algorytm binsearch
        nonlocal T, vector
        for j in range(i - 1, 0, - 1):
            if T[vector[j - 1]][2] < T[vector[i - 1]][1]:
                return j
        return 0

    def find_answer(i, j):
        nonlocal F, vector, T, P
        res = []

        while F[i][j][1] != -1:
            if F[i][j][1] == 1:
                i -= 1
            else:
                res.append(vector[i - 1])
                j -= T[vector[i - 1]][3]
                i = P[vector[i - 1]]

        return res

    # main
    for i in range(1, n + 1):
        first_price = T[vector[i - 1]][3]
        boundary = min(first_price, p + 1)

        for j in range(boundary):
            F[i][j][0] = F[i - 1][j][0]
            F[i][j][1] = 1  # Jeden oznacza ruch do góry( nie biorę liczby spod indeksu i

        prc = price(T[vector[i - 1]])
        g = find_g(i)
        P[vector[i - 1]] = g
        for j in range(boundary, p + 1):
            F[i][j][0] = F[i - 1][j][0]
            F[i][j][1] = 1  # Jeden oznacza ruch do góry( nie biorę liczby spod indeksu i

            if prc + F[g][j - T[vector[i - 1]][3]][0] > F[i][j][0]:
                F[i][j][0] = prc + F[g][j - T[vector[i - 1]][3]][0]
                F[i][j][1] = 2  # Dwa oznacza skok( biorę dany budynek)

    res = find_answer(n, p)
    res.sort()
    return res

