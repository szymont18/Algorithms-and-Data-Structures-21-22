import random


def partition(T, left, right):
    i = left - 1
    pivot = T[right]

    for j in range(left, right):
        if pivot >= T[j]:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i+1], T[right] = T[right], T[i+1]
    return i+1

def Quick_sort(T, left, right):
    if len(T) == 1:
        return

    while left < right:

        pi = partition(T, left, right)

        Quick_sort(T,left, pi-1)
        left = pi + 1




test = [random.randint(1,1000000) for _ in range(1000000)]

sprawdzaj =[]
for j in range(len(test)):
    sprawdzaj.append(test[j])
sprawdzaj.sort()

n = len(test)
Quick_sort(test,0,n-1)
print("__________________")
print(test)


flag = True
for i in range(len(test)):
    if test[i] != sprawdzaj[i]:
        flag = False
        print(i,test[i], sprawdzaj[i])
print(flag)

