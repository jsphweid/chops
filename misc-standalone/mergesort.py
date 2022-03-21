arr = [6,2,3,1,5,4,9,8,7]

def merge(L, R):
    res, i, j = [], 0, 0
    for _ in range(len(L) + len(R)):
        if i < len(L) and j < len(R):
            if L[i] < R[j]:
                res.append(L[i])
                i += 1
            else:
                res.append(R[j])
                j += 1
        elif i < len(L):
            res.extend(L[i:])
            break
        else:
            res.extend(R[j:])
            break
    return res

def merge_sort(lst):
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    L = merge_sort(lst[:mid])
    R = merge_sort(lst[mid:])
    return merge(L, R)
    
res = merge_sort(arr)
print(res)
