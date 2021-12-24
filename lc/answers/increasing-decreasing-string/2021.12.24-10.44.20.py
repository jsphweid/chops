"""
===== Initial Thoughts =====
[1,2,3,2,1,2,3,2,1,]

aaaabbbbcccc
{'a', 'b', 'c'}
['a', 'b', 'c']
{'a': 50, 'b': 1, 'c': 1}

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""
from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        sorted_chars = sorted(set(s))
        counts = Counter(s)
        while True:
            for char in sorted_chars + sorted_chars[::-1]:
                if counts[char]:
                    res += char
                    counts[char] -= 1
            if len(res) == len(s):
                return res[:len(s)]

