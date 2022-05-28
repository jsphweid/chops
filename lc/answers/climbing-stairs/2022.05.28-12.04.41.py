"""
===== Initial Thoughts =====
recursively is easy, then we can just cache

~~Complexity Analysis
Time - O(2^n)
Space - O(n)

=== Implemented Approach ===
add cache and it's O(n) time I believe

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def count(i):
            if i < 0: return 0
            if i == 0: return 1
            return count(i - 1) + count(i - 2)
        return count(n)

How could we solve this bottom up? well it's fibb
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def count(i):
            if i < 0: return 0
            if i == 0: return 1
            return count(i - 1) + count(i - 2)
        return count(n)