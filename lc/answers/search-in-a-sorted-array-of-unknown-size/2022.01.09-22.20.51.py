"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        MAX = (2 ** 31) - 1
        l, r = 0, MAX
        while l < r:
            mid = (l + r) // 2
            num = reader.get(mid)
            if num == target:
                return mid
            if num > target:
                r = mid
            else:
                l = mid + 1
        return -1








