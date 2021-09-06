"""
general strategy here is to iterate over the `t` and "using up" the letters in `s`
as we go along. If s is not all used up by the time the loop is over, it's not a subsequence.

Only advance the pointer in `s` if we come across the same value in `t`

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            # s has some length, but t does not, for sure it's false
            return False
        s_index = 0
        for char in t:
            if s[s_index] == char:
                s_index += 1
                if s_index == len(s):  # it went through the entire `s`
                    return True
        return False
