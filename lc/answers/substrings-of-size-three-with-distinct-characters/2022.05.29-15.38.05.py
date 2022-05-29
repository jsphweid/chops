
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(2, len(s)):
            a, b, c = s[i - 2], s[i - 1], s[i]
            count += a != b and b != c and a != c
        return count