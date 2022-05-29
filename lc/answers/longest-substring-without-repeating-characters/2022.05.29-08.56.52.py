"""
curr{a}
abcabcbb
 i
j
best=1
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        curr = set(s[0])
        j = 0
        best = 1
        for i in range(1, len(s)):
            char = s[i]
            while char in curr:
                curr.remove(s[j])
                j += 1
            curr.add(char)
            best = max(best, len(curr))
        return best
