import random

def Comb_sort(T):
    n = len(T)
    swapped = False
    gap = n

    while gap > 1 or swapped:
        gap = max(int(gap/1.3), 1)

        top = n - gap
        swapped = False
        for i in range(0, top):
            j = i + gap
            if T[i] > T[j]:
                T[i], T[j] = T[j], T[i]
                swapped = True


test = [random.randint(1,1000) for _ in range(100)]
print(test)
Comb_sort(test)
print("__________________")
print(test)