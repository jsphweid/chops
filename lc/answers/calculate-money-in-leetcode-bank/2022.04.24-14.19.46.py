"""
===== Initial Thoughts =====
simulation

Time - O(n)
Space - O(1)
"""

class Solution:
    def totalMoney(self, n: int) -> int:
        res, curr, week = 0, 1, 7
        for _ in range(n):
            res += curr
            if curr == week:
                curr -= 6
                week += 1
            curr += 1
        return res