from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts, t_counts = Counter(s), Counter(t)
        if len(s_counts) != len(t_counts):
            return False
        if len(s) != len(t):
            return False
        for char, count in s_counts.items():
            if t_counts[char] != count:
                return False
        return True