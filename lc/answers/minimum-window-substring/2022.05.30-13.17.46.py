"""
===== Initial Thoughts =====
ADOBECODEBANC ABCC
ajsdkflaskjdflkajs asd

=== Brute Force Approach ===
get all substrings

~~Complexity Analysis
Time - O(n^3)
Space - O(1)

=== Implemented Approach ===
about the only thing that immediately comes to mind is get counts of t
and then subtract and add/subtract counts as we move through string
just do a sliding window approach

~~Complexity Analysis
Time - O(n)
Space - O(t)
"""
from collections import Counter

"""
ADOBECODEBANC ABC
0123456789abc
i=9 j=12 best=6 counts={"A":0, "B":0, "C":-1}
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        counts = Counter(t)
        best = (float("inf"), "")
        positives = sum(counts.values())
        for j, char in enumerate(s):
            if char in counts:
                if counts[char] > 0:
                    positives -= 1
                counts[char] -= 1
                while i < j and (s[i] not in counts or counts[s[i]] < 0):
                    if s[i] in counts:
                        if counts[s[i]] > 0:
                            positives += 1
                        counts[s[i]] += 1
                    i += 1
                if counts[char] <= 0 and positives == 0:
                    best = min(best, (j - i + 1, s[i:j+1]))
        return best[1]


