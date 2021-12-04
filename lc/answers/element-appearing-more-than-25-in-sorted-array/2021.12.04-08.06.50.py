"""
===== Initial Thoughts =====
O(n) solution is probably unacceptable, but let's try it real quick

from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        best = (0, None)
        for k, v in Counter(arr).items():
            best = max(best, (v, k))
        return best[1]

=== Implemented Approach ===
Honestly, if we divide the list into like 4 or 5 chunks, we could just look for the
number that appears twice

[1,2,2,6,6,6,6,7,10]
9/4=2.25... round down... 2
for i in range(0, 9, 2):
0 - 1
2 - 2
4 - 6
6 - 6
8 - 10

what about other cases
[1,2,3,4,4]
would still find it

FAILED ON [1]

~~Complexity Analysis
Time - 
Space - 
"""

from collections import defaultdict
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        for i in range(0, len(arr), len(arr) // 10 or 1):
            counts[arr[i]] += 1
        best = (0, None)
        for value, count in counts.items():
            best = max(best, (count, value))
        return best[1]
