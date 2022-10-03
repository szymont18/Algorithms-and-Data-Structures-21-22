import random

def Insertion_sort(T):
    n = len(T)
    for i in range(1,n):
        x = T[i]
        j = i - 1

        while j >= 0 and x < T[j]:
            T[j+1] = T[j]
            j -= 1

        T[j + 1] = x



test = [7,9,4,3,2]
Insertion_sort(test)
print("__________________")
print(test)