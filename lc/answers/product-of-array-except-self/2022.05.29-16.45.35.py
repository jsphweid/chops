"""
===== Initial Thoughts =====
[1,2,3,4]
1  2  6  24
24 24 12 4
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        l, r = nums[:], nums[:]
        for i in range(1, N):
            l[i] *= l[i-1]
        for i in range(N - 2, -1, -1):
            r[i] *= r[i+1]
        res = []
        for i, n in enumerate(nums):
            if i == 0:
                res.append(r[i+1])
            elif i == N - 1:
                res.append(l[i-1])
            else:
                res.append(l[i-1] * r[i+1])
        return res
