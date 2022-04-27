"""
===== Initial Thoughts =====
simulation

~~Complexity Analysis
Time - O(n)
Space - O(n)

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""
from collections import defaultdict
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counts = defaultdict(int)
        for num in range(lowLimit, highLimit + 1):
            key = sum([int(char) for char in str(num)])
            counts[key] += 1
        return max(counts.values())