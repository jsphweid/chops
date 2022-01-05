"""
===== Initial Thoughts =====
- length of list has to be even
- at least half of the items are even

[2,2,2,4,4,4]
[1,3,4,2,6,8]
[4,3,1]
{1: 0, 3:0, 4:0, 2:0,  6: 1, 8:1}
{1:0, 3:0, 4:0, 2:0, 6:0, 8:0}
[1,3,4,2,6,8]
8 6 4 3 2 1

[1,3,4,2,6,8]
{1:0, 3:0, 4:0, 2:0, 6:0, 8:0}

[6,3,0,1]

{6:0, 3:0, 0:1, 1:1}


~~Complexity Analysis
Time - O(nlogn + n)
Space - O(n)

[1,3,4,2,6,8]
res=[1,3,4]
counts={1:0, 3:0, 4:0, 2:0, 6:0, 8:0}
[0,0]
{0: 0}

[4,4,16,20,8,8,2,10]
[2,4,4,8,8,10,16,20]
4:0, 16:1, 20:1, 8:1, 2:0, 10:1
[2, 4]
4,4
"""
from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        res, counts = [], Counter(changed)
        for num in sorted(changed):
            if num*2 in counts and counts[num] and counts[num*2]:
                res.append(num)
                counts[num] -= 1
                counts[num*2] -= 1
        if len(res)*2 == len(changed) and all([v == 0 for v in counts.values()]):
            return res
        return []


