class Solution:
    def longestPalindrome(self, s: str) -> str:
        def _find_longest(i: int, j: int) -> str:
            while i - 1 > -1 and j + 1 < len(s) and s[i - 1] == s[j + 1]:
                i -= 1
                j += 1
            return s[i: j + 1]
        record = s[0]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                longest = _find_longest(i - 1, i)
                if len(longest) > len(record):
                    record = longest
            longest = _find_longest(i, i)
            if len(longest) > len(record):
                record = longest
        return record