"""
I think we should be able to just iterate over the list with a jump of 2k.
For the last one we need a bit of special logic
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ret = ""
        for i in range(0, len(s), 2 * k):
            left_exclusive = i - 1 if i else None
            if len(s) - i < k:
                ret += s[-1: left_exclusive: -1]
            else:
                ret += s[i + k - 1: left_exclusive: -1]
                ret += s[i + k: i + (2 * k)]
        return ret