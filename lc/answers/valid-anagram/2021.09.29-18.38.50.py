from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = defaultdict(int)
        t_counts = defaultdict(int)
        for char in s: s_counts[char] += 1
        for char in t: t_counts[char] += 1
        if s_counts.keys() != t_counts.keys(): return False
        for char, count in s_counts.items():
            if t_counts[char] != count:
                return False
        return True