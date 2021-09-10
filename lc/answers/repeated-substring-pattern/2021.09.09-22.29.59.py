"""
Since the substring MUST contain at least the beginning of the string, we can start at the beginning
and incrementally create a substring. When we find a character that is the same as the first char,
we check to see if that substring length divides evenly with the length of the string. If it does, we
repeat it by the evenly divided amount and compare if that string is equal to the string in the arg.
If it's true, then we return True! If it's not we just continue the search for the substring up to 
half the length of the string. If we never found anything, we can return False.
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        for i in range(1, (len(s) // 2) + 1):
            if s[i] == s[0]:
                if len(s) % i == 0:
                    if s[0:i] * (len(s) // i) == s:
                        return True
        return False