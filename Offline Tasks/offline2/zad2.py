#Szymon Twardosz
'''
Algorytm
1)Na początku sortuje daną w zadaniu tablicę wg klucza(x,y to przedziały x[0],x[1] to odpowiednio początek i koniec
przedziału) x > y wtedy i tylko wtedy gdy: x[0] > y[0] lub (x[0] == y[0] i x[1] < y[1])
2)Następnie tworzę nową tablicę(intervals) w której zapisuje indeksy potencjalnych największych przedziałów(*),
oraz liczniki, które liczą ile przedziałów zawiera się w wyżej wymienionych przedziałach(*).
3)Ostatni krok to znalezienie w tablicy intervals najwiekszego liczniki i zwrócenie jego wartosci

Złożoność czasowa mojego algorytmum to O(nlogn). W pesymistyczym przypadku jest to jednak O(n*n)
'''



def depth(L):
    def partition(tab,left,right):
        i = left - 1
        pivot = tab[right]

        for j in range(left, right):
            if tab[j][0] < pivot[0] or (tab[j][0] == pivot[0] and tab[j][1] > pivot[1]):
                i += 1
                tab[j], tab[i] = tab[i], tab[j]

        tab[i+1], tab[right] = tab[right], tab[i+1]
        return i + 1


    def Quick_sort(tab,left,right): # Quick Sort z while'em zaproponowany na wykładzie
        while left < right:

            pi = partition(tab,left,right)

            Quick_sort(tab,left, pi - 1)
            left = pi + 1

    n = len(L)
    Quick_sort(L, 0, n-1)
    # Przygotowanie do szukania
    max_level = 0
    intervals = [[0,0]] #First is of ,,natural series", second count how long is that index
    for i in range(1, n):
        k = len(intervals)
        flag = True
        for j in range(k):
            if L[intervals[j][0]][1] >= L[i][1]:
                intervals[j][1] += 1

                j += 1
                while j < k:
                    intervals[j][1] += 1
                    j += 1

                flag = False
                break

        if flag:
            intervals.append([i, 0])

    for k in range(len(intervals)):
        max_level = max(max_level, intervals[k][1])

    return max_level
