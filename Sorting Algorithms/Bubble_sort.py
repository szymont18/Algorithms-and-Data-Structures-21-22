import random

def Bubble_sort(T):
    n = len(T)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if T[j] > T[j+1]:
                T[j+1], T[j] = T[j], T[j+1]


test = [random.randint(1,10) for _ in range(5)]
print(test)
Bubble_sort(test)
print("__________________")
print(test)