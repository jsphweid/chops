arr = [6,2,3,1,5,4,9,8,7]

def quicksort(lst, a=0, b=None):
    if b is None:
        b = len(lst) - 1

    if b <= a or a < 0:
        return

    i = a - 1
    for j in range(a, b):
        if lst[j] < lst[b]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[b] = lst[b], lst[i+1]

    quicksort(lst, a, i)
    quicksort(lst, i + 2, b)

quicksort(arr)
print(arr)





