def partition(A,p,r):
    x = A[r]
    i = p - 1

    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def select(A, p, k, r):
    if p == r: return A[p]

    if p < r:
        q = partition(A, p, r)
        if q == k: return A[q]
        elif q < k: return select(A, q + 1,k, r)
        else: return select(A, p, k, q-1)

nums = [2,8,9,2,12,5,6,84,5,15,56,8]
a = select(nums,0,4,len(nums) - 1)
b = select(nums,0,2,a)
print(b,a)
print(nums)
