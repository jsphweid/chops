from collections import Counter
from insertionsort import insertion_sort2


# not sure if this is really bucket sort...
def bucket_sort(lst):
    counts = Counter(lst)
    res = []
    for bucket in [1,2,6]:
        for _ in range(counts[bucket]):
            res.append(bucket)
    return res

def bucket_sort2(lst):
    # nums range from 1-5
    buckets = [[] for _ in range(4)]
    for num in lst:
        i = int(num) - 1
        buckets[i].append(num)
    res = []
    for i in range(len(buckets)):
        insertion_sort2(buckets[i])
    for bucket in buckets:
        for item in bucket:
            res.append(item)
    return res


if __name__ == "__main__":
    arr = [1,2,6,2,2,6,1,6,2,6,6,1,2,6,6,2,6]
    print(bucket_sort(arr))

    floats = [1.2, 2.3, 2.6, 2.1, 3, 3.1, 3.001, 4.8, 4.6]
    print(bucket_sort2(floats))

