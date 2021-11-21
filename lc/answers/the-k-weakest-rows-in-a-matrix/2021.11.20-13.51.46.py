"""
===== Initial Thoughts =====
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],

(2, 0)
(4, 1)
(1, 2)
(2, 3)
(5, 4)
(1, 2), (2, 0), (2, 3)

~~Complexity Analysis
Time - O(mn + mlogm)
Space - O(m)

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

[1,1,1,0]
0,3 m=1
2,3 m=2
3,3

[0,0,0,0]
0,3 m=1
0,1 m=0
0,0

[1,1,1,1]
0,3 m=1
2,3 m=2
3,3

def count_ones(row, length):
    l, r = 0, length - 1
    while l < r:
        mid = (l + r) // 2
        if row[mid]:
            l = mid + 1
        else:
            r = mid
    return l + row[l] if l == length - 1 else l

somehow the binary search was slower... :thinking-face:
"""

def count_ones(row):
    count = 0
    for item in row:
        count += item
        if not count: break
    return count
    

import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_length = len(mat[0])
        mapped = [(count_ones(r), i) for i, r in enumerate(mat)]
        heapq.heapify(mapped)
        return [heapq.heappop(mapped)[1] for _ in range(k)]