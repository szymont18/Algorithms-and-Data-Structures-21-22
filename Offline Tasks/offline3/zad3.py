#Szymon Twardosz
'''
Wiedząc, że liczby w tablicy zawierają się w przedziale [1,N], tworzę N pojemników. Do I-tego pojemnika trafiają elementy
o wartościach należących do przedziału [i+1, i+2)
Następnie po podzieleniu elementów do pojemników, sortuje elementy w każdym pojemniku. Używam do tego Insertion Sorta
Po wszystkim scalam pojemniki, przepisując kolejno każdy element do tablicy o rozmiarze N
'''


def SortTab(T,P):
    def insertion_sort(T):
        n = len(T)
        for i in range(1, n):
            x = T[i]
            j = i - 1

            while j >= 0 and x < T[j]:
                T[j + 1] = T[j]
                j -= 1

            T[j + 1] = x

    def divide(tab):
        n = len(tab)

        buckets = [[] for _ in range(n)]

        for i in range(n):
            buckets[int(tab[i] - 1)].append(tab[i])

        return buckets

    def bucket_sort(tab):
        n = len(tab)
        max_el = max(tab)
        min_el = min(tab)


        buckets = [[] for _ in range(n)]

        for i in range(n):
            buckets[int((tab[i] -min_el)/(max_el - min_el + 1) * n)].append(tab[i])

        for b in buckets:
            if len(b) > 1:
                insertion_sort(b)

        res = []

        for i in range(n):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
        return res

    list_of_buckets = divide(T)

    for i in range(len(list_of_buckets)):
        if len(list_of_buckets[i]) > 1:
            list_of_buckets[i] = bucket_sort(list_of_buckets[i])

    res = []

    for i in range(len(list_of_buckets)):
        for j in range(len(list_of_buckets[i])):
            res.append(list_of_buckets[i][j])

    return res

