"""
3 7 => (2) 3 -- both odd, increase by 1
4 7 => (1.5) 2 -- one odd one even, round up
5 8 => (1.5) 2 -- one odd one even, round up
6,8 => (1) 1

if at least one odd number... integer divide and add one
"""

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        add_one = low & 1 or high & 1
        return high - low // 2 + add_one