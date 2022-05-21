"""
===== Initial Thoughts =====
can't think of much more than the brute force at this moment

=== Brute Force Approach ===
just keep counts of p and when it has the same as current s substring counts, then mark index as a start

~~Complexity Analysis
Time - O(p * s)
Space - O(p)

from collections import Counter

def has_same_counts(d1, d2):
    # assumes they are both the same length
    for char, count in d2.items():
        if char not in d1 or d1[char] != count:
            return False
    return True


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counts = Counter(p)
        s_counts = Counter(s[:len(p)])
        res = []
        skip = 0
        for i in range(len(s) - len(p) + 1):
            if i != 0:
                char_to_subtract = s[i - 1]
                char_to_add = s[i + len(p) - 1]
                s_counts[char_to_subtract] -= 1
                s_counts[char_to_add] += 1
                if char_to_add not in p_counts:
                    skip = len(p)
            if skip > 0:
                skip -= 1
            elif has_same_counts(s_counts, p_counts):
                res.append(i)
        return res


cbaebabacd 8 iterations 10 - 3 + 1
"""
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counts = Counter(p)
        matching = 0
        res = []
        for i, char in enumerate(s):
            if i >= len(p):
                char_to_eject = s[i - len(p)]
                if char_to_eject in counts:
                    counts[char_to_eject] += 1  # return to counts
                    if counts[char_to_eject] > 0:
                        matching -= 1
            if char in counts:
                counts[char] -= 1  # take from counts
                if counts[char] >= 0:
                    matching += 1

            if matching == len(p):
                res.append(i - len(p) + 1)
        return res

