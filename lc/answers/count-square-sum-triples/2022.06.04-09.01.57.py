"""
===== Initial Thoughts =====


=== Brute Force Approach ===
just look through all combos but only count one way
3 4 5
but don't look for 4 3 5

~~Complexity Analysis
Time - O(N^2)
Space - O(1)

1 - 1 2 3 4 5
2 - 2 3 4 5
3 - etc.
4
5
"""

class Solution:
    def countTriples(self, n: int) -> int:
        total = 0
        for a in range(1, n + 1):
            for b in range(a, n + 1):
                c = ((a**2) + (b**2)) ** 0.5
                if c <= n and int(c) == c:
                    total += 2
        return total
