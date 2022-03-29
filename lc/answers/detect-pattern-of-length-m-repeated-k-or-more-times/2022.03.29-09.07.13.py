"""
===== Initial Thoughts =====


=== Brute Force Approach ===
have a counts dict that tuplifies known length subsequence

~~Complexity Analysis
Time - O(nm)
Space - O(nm)

from collections import defaultdict
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        d = defaultdict(int)
        for i in range(len(arr) - m + 1):
            d[tuple(arr[i: i+m])] += 1
        for count in d.values():
            if count >= k:
                return True
        return False

This failed because I misunderstood the question.

The patterns must be consecutive.

=== Implemented Approach ===
keep track of a streak and when we reach m*k, return True

~~Complexity Analysis
Time - O(n)
Space - O(1)

[1,2,4,4,4,4]
 1 1 1 

failed on [3,2,2,1,2,2,1,1,1,2,3,2,2]
m=3 k=2    1 2 3 1

from collections import defaultdict
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        streak = 0
        for i in range(len(arr) - 1, -1, -1):
            if i < m or arr[i] == arr[i - m]:
                streak += 1
            else:
                streak = 1
            if streak >= m * k:
                return True
        return False

but this fails
[1,2,4,4,4,4]
I'm just going to do the brute force for now...
"""
from collections import defaultdict
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m + 1):
            pattern = arr[i: i + m]
            if pattern * k == arr[i:i+m*k]:
                return True
        return False

