def merge(tab1, tab2):
    n1 = len(tab1)
    n2 = len(tab2)
    res = [0 for _ in range(n1 + n2)]

    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2:
        if tab1[i] <= tab2[j]:
            res[k] = tab1[i]
            i += 1
        else:
            res[k] = tab2[j]
            j += 1

        k += 1

    while i < n1:
        res[k] = tab1[i]
        k += 1
        i += 1

    while j < n2:
        res[k] = tab2[j]
        j += 1
        k += 1

    return res


def merge_sort(tab):
    if len(tab) <= 1:
        return tab

    middle = len(tab) // 2

    Left = tab[:middle]
    Right = tab[middle:]

    Left = merge_sort(Left)
    Right = merge_sort(Right)

    return merge(Left,Right)


nums = [1,8,523,6,92,82,8962,82,1,0,5]
print(merge_sort(nums))


