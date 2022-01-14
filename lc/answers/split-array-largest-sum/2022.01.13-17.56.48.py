"""
===== Initial Thoughts =====
[7,2,5,10,8]
l=0 r=32
m=16 -- 14, 10, 8 too many groups
m=20 -- 14, 18 good amount of groups
m=18 -- 14, 18 good amount of groups
m=17 -- 14, 10, 8, too many groups, 18 is the magic number
but we don't care about that (although it happens to be the answer?)

1,2,3,4,5 l=0 r=15
m=7 -- 6,4,5 too many groups
m=10 -- 10, 5 good amount of groups
m=8 -- 6, 4, 5 too many groups
m=9 -- 6, 9 return

1,4,4 l=0 r=9
m=4 1 4 4 

min has to be largest single int
max can be the sum, but it can probably become more optimal

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            acc, groups = 0, 1
            for num in nums:
                acc += num
                if acc > mid:
                    acc = num
                    groups += 1
            if groups <= m:
                r = mid
            else:
                l = mid + 1
        return l

