"""
=== Brute Force Approach ===
just reorder, get the diff between first two numbers, and assert it's 
same diff between other numbers... 

~~Complexity Analysis
Time - O(nlogn)
Space - O(1)

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True