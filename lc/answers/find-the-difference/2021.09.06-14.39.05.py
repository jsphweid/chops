"""
just for the hell of it, we should use count here although it seems like it's not very efficient
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            if s.count(char) != t.count(char):
                return char