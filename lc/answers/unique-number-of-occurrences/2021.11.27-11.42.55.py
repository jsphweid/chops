"""
===== Initial Thoughts =====
use counter module and set length

~~Complexity Analysis
Time - O(n)
Space - O(n)
"""
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr).values()
        return len(counts) == len(set(counts))