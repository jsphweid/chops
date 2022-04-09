class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = 0
        d = {}
        for i, char in enumerate(s):
            if char in d:
                res = max(res, i - d[char])
            else:
                d[char] = i
        return res - 1