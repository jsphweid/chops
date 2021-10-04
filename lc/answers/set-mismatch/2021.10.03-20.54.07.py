"""
===== Initial Thoughts =====
[1,2,2,4] -> [2, 3]
2 is there twice
3 is missing

=== Brute Force Approach ===
make a dict of all the counts
iterate over once more with an index. when you come across the number that is in there twice, record it (has count 2)
also use the `i` to find the missing -- it should not be in the dict

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""
from collections import defaultdict
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        for n in nums: counts[n] += 1
        ret = [0, 0]
        for i, n in enumerate(nums):
            expected = i + 1
            if n != expected and expected not in counts: ret[1] = expected
            if counts[n] == 2: ret[0] = n
        return ret