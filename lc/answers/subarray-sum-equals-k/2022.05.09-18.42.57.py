"""
===== Initial Thoughts =====
did this one with brian, basically got it just in 
30 minutes, but needed his guidance a bit

[1,2,3]
[0,1,3,6] k=3

[1]
0
[0,1] k=0

[-1,-1,1] k=0
[0,-1,-2,-1]

[1,2,3] k=3
curr=6
total=2
counts={0:1, 1:1, 3:1}

"""

from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = Counter([0])
        curr = total = 0
        for num in nums:
            curr += num
            total += counts[curr - k]
            counts[curr] += 1
        return total
