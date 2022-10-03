import random

def Select_sort(T):
    n = len(T)

    for i in range(0,n-1):
        index = i

        for j in range(i, n):
            if T[index] > T[j]:
                index = j
        T[i], T[index] = T[index], T[i]

test = [random.randint(1,1000) for _ in range(100000)]
print(test)
Select_sort(test)
print("__________________")
print(test)