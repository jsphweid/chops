"""
=== Implemented Approach ===
iterate over values, adding to set as we go along... if num exists in set, early exit

~~Complexity Analysis
Time - O(n)
Space - O(n)

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False