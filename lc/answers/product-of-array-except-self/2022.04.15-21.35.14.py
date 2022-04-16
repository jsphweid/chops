"""
[1, 2, 3, 4 ]
[1, 2, 6, 24]
[24,24,12,4 ]

[1,1,2,6]
[24,12,4,1]

[24,12,8,6]

[-1,1,0,-3,3]
[1,-1,-1,0,0]
[0,0,-9,3,1]

had to look up the answer I did years ago. I was close to getting it but
was off by index on each side -- should've been obvious.
[1,2,3,4]
[3,2,1,0]

[1, 2, 3, 4 ]
[1, 1, 2, 6]
[24,12,4, 1]

[1,2,3,4]
[1,2,3] = i
[2,1,0] = j
l=[1,1,1,1]
r=[1,1,1,1]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        l, r = [1] * N, [1] * N
        for i, j in zip(range(1, N), range(N-2, -1, -1)):
            l[i] *= l[i-1] * nums[i-1]
            r[j] *= r[j+1] * nums[j+1]
        return [a * b for a, b in zip(l, r)]