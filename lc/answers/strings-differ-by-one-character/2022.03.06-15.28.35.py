"""
===== Initial Thoughts =====
["cccc","abcd","abyd","abab"]

=== Brute Force Approach ===
just compare every string with every string and get the diff. If there is any with diff of 1, return true.

~~Complexity Analysis
Time - O(m*n^2) (m for each comparison and there are n^2 comparisons)
Space - O(1)

This TLEs.

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        for i in range(len(dict) - 1):
            for j in range(i + 1, len(dict)):
                diff = 0
                for idx, char in enumerate(dict[i]):
                    diff += char != dict[j][idx]
                if diff == 1:
                    return True
        return False

=== Implemented Approach ===
after looking at the hints, I'm going to try the "*" approach

~~Complexity Analysis
Time - 
Space - 
"""
from collections import defaultdict
class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        counts = defaultdict(int)
        for word in dict:
            for i in range(len(word)):
                counts[word[:i] + "*" + word[i+1:]] += 1
        for count in counts.values():
            if count > 1:
                return True
        return False
