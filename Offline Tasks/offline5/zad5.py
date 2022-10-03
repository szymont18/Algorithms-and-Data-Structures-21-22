#Szymon Twardosz
'''
Korzystając z PriorityQueue zapisuje wartości objętości(oraz odpowiadające im położenie) ropy napotkanej
na trasie z 0 do n-1.
W momencie gdy zabraknie paliwa, to pobieram z PriorityQueue największą wartość ropy i "wlewam ją do baku".
W tym samym momencie aktualizuje zmienną path, która przechowuję przystanki.
Złożoność obliczeniowa to O(nlogn)
'''
import queue

def plan(T):
    n = len(T)
    fuel_queue = queue.PriorityQueue(n)

    fuel = T[0]
    place = 0
    path = [0]

    while place < n - 1:
        place += 1
        fuel -= 1
        fuel_queue.put((-T[place], place)) #Bo kolejka zwraca item o najmniejszym priorytecie

        if place == n - 1: break

        if fuel == 0:
            x_fuel, loc = fuel_queue.get()
            fuel = -x_fuel
            path.append(loc)

    path.sort()
    return path

