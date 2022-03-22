def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        while j >= 0 and lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
            j -= 1
            i -= 1


def insertion_sort2(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key

if __name__ == "__main__":
    arr = [5,2,1,3,7,9,2]
    insertion_sort2(arr)
    print('arr', arr)