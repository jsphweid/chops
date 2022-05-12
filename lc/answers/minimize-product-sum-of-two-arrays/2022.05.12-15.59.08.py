"""
[5,3,4,2], nums2 = [4,2,2,5]
one=[0,0,0,0,1,1]
two=[0,0,2,0,0,0]
res=2
l=0, r=5
10 12 8 10
"""

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        one, two = [0] * 101, [0] * 101
        for x, y in zip(nums1, nums2):
            one[x] += 1
            two[y] += 1
        res = 0
        l, r = 0, len(two) - 1
        for _ in range(len(nums1)):
            while one[l] == 0:
                l += 1
            while two[r] == 0:
                r -= 1
            one[l] -= 1
            two[r] -= 1
            res += l * r
        return res