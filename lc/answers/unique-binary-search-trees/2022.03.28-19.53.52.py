"""
===== Initial Thoughts =====
1 - 1
2 - 2
3 - 5
"""

class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def recurse(num):
            if num < 3:
                return num
            nums_above = n - num
            nums_below = num - 1
            return recurse(nums_below) + recurse(nums_above)

        return sum([recurse(i) for i in range(1, n + 1)])