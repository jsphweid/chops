"""
===== Initial Thoughts =====
[0,3,7,2,5,8,4,6,0,1]
0 1 2   3 4 5   6 7 8

[100,4,200,1,3,2]
1 2 3 4

100:1, 4;1, 200:1, 1:1, 3:1, 2:1

2 2 2 2 2

I didn't get anything down because I didn't understand that sequence
meant n, n + 1, n + 2, etc.

saw StefanPochmann's answer, going to replicate that...
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, nums = 0, set(nums)
        for num in nums:
            if num - 1 not in nums:
                nxt = num + 1
                while nxt in nums:
                    nxt += 1
                res = max(res, nxt - num)
        return res
