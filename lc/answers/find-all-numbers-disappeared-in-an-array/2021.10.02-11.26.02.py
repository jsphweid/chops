"""
===== Initial Thoughts =====
the len of list determines max num. for every num missing, there will be a duplicate.

=== Brute Force Approach ===
keep another list [1..n] sorted. Whenever we find a num, mark it as None.
Then finally filter that list so only nums remain.

~~Complexity Analysis
Time - O(n)
Space - O(n)

I'm not immediately sure how to do this more efficiently. I'll try something differnet
next time most likely.
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ordered_nums = list(range(1, len(nums) + 1))
        for num in nums: ordered_nums[num - 1] = None
        return [n for n in ordered_nums if n != None]