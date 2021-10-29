"""
===== Initial Thoughts =====
two pointers. we just need to control them carefully
"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if j == 0: return False
                if typed[j] != typed[j - 1]: return False
                j += 1
        if j < len(typed):
           return typed[j:] == name[i - 1] * (len(typed) - j)
        return i == len(name)