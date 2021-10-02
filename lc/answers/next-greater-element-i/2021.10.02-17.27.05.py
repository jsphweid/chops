"""
===== Initial Thoughts =====
dang i don't remember solving this one

=== Brute Force Approach ===
iterate over nums1. find the digit in nums2 (can dictify positions for fast retrieval)
then do an expensive search in all the elements of the list after that, find one that is larger
and return it, if there are none, right down -1

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_positions = {}
        for i, num in enumerate(nums2): nums2_positions[num] = i

        output = []
        for num in nums1:
            nums2_i = nums2_positions[num]
            greater = [n for n in nums2[nums2_i + 1:] if n > num]
            output.append(greater[0] if len(greater) else -1)
        return output