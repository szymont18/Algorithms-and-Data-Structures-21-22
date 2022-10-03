#Szymon Twardosz
'''
ALGORYTM
Początkowe ify to obłsuga skrayjnych przypadków

Funkcję heapify oraz build_heap służą odpowiednio do naprawiania i budowania stosu. Są one wywoływane w funckji sort, która
korzystająć z struktury stosu przepina nody na odpowiednie miejsca


1)Do tablicy pointers zapisuje pierwsze k + 1 elementów. Wiadomo wówczas że wsród nich jest element który powinien znaleźć
się na miejscu pierwszym.
2)Cały czas przepinam najmniejszy element z tablicy do wskaźnika sortLL, który służy do obługiwania posortowanej Linked List'y.
Oprócz tego(jeżeli jest to możliwe) dodaje jeszcze nie wykorzystane elementy z pierwotnej LL do tablicy(stosu) na miejsce
o indeksie i naprawiam stos za pomocą funckji heapify
3)Gdy elementy z pierwotnej listy zostaną wyczerpane, wtedy postępuję jak wyżej, tylko już bez dodawania elementu
4)Funkcja sort zwraca wskazanie na poprzednika posortowanej listy
5)Ostatecznie otrzymuje posortowaną Linked Listę

#ZLOŻONOŚĆ
Złożoność czasowa mojego algorytmu w notacji duzego O to O(n,k) = nlogk, dla k != 1 i k!=0 podanego w zadaniu i O(n,k) = n
dla k = 1
'''



def SortH(p,k):
    if k == 0:
        return p
    if k == 1:
        guard = Node()
        guard.next = p
        q = guard
        while p is not None and p.next is not None:
            if p.next.val < p.val:
                tmp = p.next.next
                p.next.next = p
                q.next = p.next
                p.next = tmp

            q = p
            p = p.next
        return guard.next

    # Funkcje na później

    def heapify(tab, n, i):  # Naprawianie stosu, tab = tablica, n = długość tablicy, i = zepsuty element
        l = 2 * i +1
        r = 2 * i +2
        wanted = i

        if l < n and tab[l].val < tab[wanted].val:
            wanted = l

        if r < n and tab[r].val < tab[wanted].val:
            wanted = r

        if wanted != i:
            tab[wanted], tab[i] = tab[i], tab[wanted]
            heapify(tab, n, wanted)

    # end Heapify

    def build_heap(tab, n): #Budowa stosu/ tab = tablica, n = rozmiar tab
        par = (n-2) // 2

        for i in range(par, -1, -1):
            heapify(tab, n, i)

    def sort(tab, n, p):
        build_heap(tab,n)

        sortLL = Node()
        guard = Node()
        guard.next = sortLL

        while p is not None:
            sortLL.next = tab[0]
            sortLL = sortLL.next
            #tab[0].next = None
            tab[0] = p
            p = p.next

            heapify(tab, n, 0)

        for i in range(n-1, -1, -1):
            tab[0], tab[i] = tab[i], tab[0]

            sortLL.next = tab[i]
            tab[i].next = None
            sortLL = sortLL.next

            heapify(tab,i,0)
        return guard.next

    pointers = [None for i in range(k+1)]

    cnt = 0
    while p is not None and k + 1 > 0:
        pointers[cnt] = p
        p = p.next
        cnt += 1
        k -= 1

    return sort(pointers, cnt, p).next

