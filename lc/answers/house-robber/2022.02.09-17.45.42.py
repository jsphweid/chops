"""
===== Initial Thoughts =====
the solutions for these seem trivial and lead you to believe you get the odds and evens and then max
those two totals
[1,2,3,1] (i.e., it's either max(sum([1,3]), sum([2,1]))) => 4
[2,7,9,3,1] (i.e., it's either max(sum([2,9,1]), sum([7,3]))) => 12

But that won't work, because we might need to skip more than every other
[9,26,1,9,1,9] => max should be 27
I think this is similar to step stones problem.
We want to check two steps ahead and pick the best one

or we can just solve this like a graph problem... pretty simple

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

[2,7,9,3,1]
[]
res=2
seen = {
    0: 2
    1: 7
    2: 11
    3: 10
    4: 8
}

failed on [1,2,3,1]
queue=[(1,0),(2,1)]
total=1
i=0
res=1
seen = {
    
}
oops, `if i not in seen or seen[i] <= total:` should be `if i in seen and seen[i] <= total:`

[6,6,4,8,4,3,3,10]
queue=[(6,1),(10,2),(14,3)]
(6,0)
res=6
seen = {
    0: 6
}
"""
from collections import deque
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: return max(nums)
        seen, queue, res = {}, deque([(nums[0], 0), (nums[1], 1)]), -float("inf")
        while queue:
            total, i = queue.popleft()
            res = max(res, total)
            if i in seen and total <= seen[i]:
                continue
            seen[i] = total
            if i + 2 < len(nums):
                queue.append((total + nums[i + 2], i + 2))
            if i + 3 < len(nums):
                queue.append((total + nums[i + 3], i + 3))
        return res
