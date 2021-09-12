"""
we should probably sort nums2
a brute force approach would just iterate through nums1. find the index of that num in nums2
and get the next num (index + 1) else -1.

Actually no... you can't just reorder it because the order is important for proper indices...

Instead, we can find index of a partial array where nums2[foundNum + 1:]
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for num in nums1:
            i = nums2.index(num)
            output.append(next(filter(lambda x: x > num, nums2[i + 1:]), -1))
        return output
