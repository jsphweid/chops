"""
[100,-23,-23,404,100,23,23,23,3,404]
adj={} dupes={100:[0,4], -23:[1,2], 404:[3,9], 23:[5,6,7]}

loses on last problem

from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        new_arr = []
        for i, item in enumerate(arr):
            if len(new_arr) < 3:
                new_arr.append(item)
            elif new_arr[-1] == item and new_arr[-2] == item:
                continue
            else:
                new_arr.append(item)
        arr = new_arr

        adj, dupes = defaultdict(set), defaultdict(list)
        for i, val in enumerate(arr):
            dupes[val].append(i)
        for i, val in enumerate(arr):
            adj[i] |= set(dupes[val])
            if i > 0: adj[i].add(i - 1)
            if i < len(arr) - 1: adj[i].add(i + 1)

        queue, res, seen = deque([0]), -1, set()
        while queue:
            res += 1
            for _ in range(len(queue)):
                num = queue.popleft()
                
                if num in seen: continue
                seen.add(num)
                
                if num == len(arr) - 1:
                    return res
                for child in adj[num]:
                    queue.append(child)

[100,-23,-23,404,100,23,23,23,3,404]
  0   1    2   2   1  2  3  3 4 3


[100,-23,-23,404,100,23,23,23,3,404]
 0    1   2  1    4   5  6  7  8 9

DP solution TLEs
from math import inf
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        res = list(range(len(arr)))
        smallest_seen = {item: inf for item in arr}

        def update(i, steps):
            l, r = i - 1, i + 1
            while l >= 0 or r < len(arr):
                if l >= 0:
                    res[l] = min(res[l], steps+i-l)
                    smallest_seen[arr[l]] = min(smallest_seen[arr[l]], res[l])
                if r < len(arr):
                    res[r] = min(res[r], res[i]+r-i)
                    smallest_seen[arr[r]] = min(smallest_seen[arr[r]], res[r])
                l -= 1
                r += 1

        for i in range(1, len(arr)):
            if arr[i] in smallest_seen:
                seen = smallest_seen[arr[i]]
                res[i] = min(res[i], seen + 1)
                smallest_seen[arr[i]] = min(seen, res[i])
            else:
                smallest_seen[arr[i]] = res[i]
            update(i, res[i])
        return res[-1]

if it's in smallest_seen, then make current min of one in smallest_seen curr

[100,-23,-23,404,100,23,23,23,3,404]
{100:[0],-23:[1,2],404:[3,9],100:[4],23:[5,6,7],3:[8]}

"""


from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dupes = defaultdict(list)
        for i, val in enumerate(arr):
            dupes[val].append(i)

        queue, res, seen = deque([0]), -1, set()
        while queue:
            res += 1
            for _ in range(len(queue)):
                i = queue.popleft()
                if i == len(arr) - 1:
                    return res
                for j in [i+1, i-1] + dupes[arr[i]][::-1]:
                    if j >= 0 and j < len(arr) and j != i and j not in seen:
                        if j == len(arr) - 1: return res + 1
                        queue.append(j)
                        seen.add(j)
                dupes[arr[i]] = []





