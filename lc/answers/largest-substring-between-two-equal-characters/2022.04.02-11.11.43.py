class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        seen = dict()
        for i, char in enumerate(s):
            if char in seen:
                res = max(res, i - seen[char] - 1)
            else:
                seen[char] = i
        return res