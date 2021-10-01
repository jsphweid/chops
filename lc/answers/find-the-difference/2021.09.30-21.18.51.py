"""
=== Implemented Approach ===
since it's random, the only viable solution I can think of is making a catalog of the numbers and their counts
then scanning through the new string, subtracting off the count as we go along. When we try to pull a count
off that doesn't exist, that must be the number

~~Complexity Analysis
Time - O(2n)
Space - O(n)
"""
from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = defaultdict(int)
        for char in s: counts[char] += 1
        for char in t:
            if char in counts:
                if counts[char] == 0: return char
                else: counts[char] -= 1
            else:
                return char