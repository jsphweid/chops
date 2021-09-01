"""
I need to understand what an anagram is. length of str must be identical. 
Also number of each char must be the same in both?
It looks like yes, it's strict. I'm going to assume spaces are important initially.
"""
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        for char in s:
            s_count[char] += 1
        for char in t:
            t_count[char] += 1
        for key, val in s_count.items():
            if t_count[key] != val:
                return False
        return True
