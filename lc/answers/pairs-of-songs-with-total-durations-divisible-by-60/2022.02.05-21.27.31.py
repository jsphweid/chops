"""
===== Initial Thoughts =====
very obvious brute force

=== Implemented Approach ===
why don't we do a lookup based on remainder

the trick becomes not double counting

~~Complexity Analysis
Time - 
Space - 
"""
from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res, d = 0, defaultdict(int)
        for t in time:
            reduced = t % 60
            compliment = (60 - reduced) if reduced else 0
            res += d[compliment]
            d[reduced] += 1
        return res