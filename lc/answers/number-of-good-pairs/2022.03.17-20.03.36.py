"""
===== Initial Thoughts =====
we just need the counts, then we can use math to get the final results

[1,1,1,1] how many pairs?
6 (3 + 2 + 1)

[1,1,1,1,1] how many pairs?
10 (4 + 3 + 2 + 1)

Is there a faster way of calculating this?
for now we can just do some recursive fn and cache

nums = [1,2,3,1,1,3]
{1: 3, 2: 1, 3: 2}
1,2,3
res = add(0) + add(1) + add(2) => 4

The formula I was missing was 
def add(num):
	num * ((num - 1) // 2)

~~Complexity Analysis
Time - O(n)
Space - O(n)
"""

from collections import Counter

@cache
def add(num):
	return 0 if num < 1 else num + add(num - 1)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts, res = Counter(nums), 0
        for value in counts.values():
        	res += add(value - 1)
        return res
