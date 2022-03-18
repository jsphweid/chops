"""
=== Implemented Approach ===
visualize the problem as a guessing game where we're guessing the answer
a number too low fails
a number too high succeeds
it creates
[F,F,F,F,F,T,T] for example... we want to find the first true
we can do that quickly using binary search

In example 1
    **Input:** nums = [7,2,5,10,8], m = 2
    **Output:** 18
...15,16,17 should all be false
18,19,20... should all be true

We just need to frame the question... what logic can we write so that 
it creates `m` OR LESS groups

our min and max can easily be max(nums) as min, sum(nums) as max

The fn to asses if we're on the right answer or not is O(n)
The space we have to search through is sum(nums) - max(nums), say `k`

~~Complexity Analysis
Time - O(nlogk)
Space - O(1)

[7,2,5,10,8], m = 2
max_num=10
groups_made = 1
curr = 9
[7,2,5]
"""

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
    	def succeeds(max_num: int):
    		groups_made = 0
    		curr = 0
    		for num in nums:
    			if curr + num > max_num:
    				groups_made += 1
    				curr = num
    			else:
    				curr += num
    		groups_made += curr != 0
    		return groups_made <= m

    	l, r = max(nums), sum(nums)
    	while l < r:
    		mid = (l + r) // 2
    		if succeeds(mid):
    			r = mid
    		else:
    			l = mid + 1
    	return l

















