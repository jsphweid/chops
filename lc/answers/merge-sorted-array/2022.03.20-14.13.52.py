"""
===== Initial Thoughts =====
Go backwards

nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
m=1 n=-1

[1,2,2,3,5,6]
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m, n = m - 1, n - 1
        for i in range(len(nums1) - 1, -1, -1):
            if m >= 0 and n >= 0:
                if nums1[m] > nums2[n]:
                    nums1[i] = nums1[m]
                    m -= 1
                else:
                    nums1[i] = nums2[n]
                    n -= 1
            elif m < 0:
                nums1[i] = nums2[n]
                n -= 1
            else:
                nums1[i] = nums1[m]
                m -= 1

        