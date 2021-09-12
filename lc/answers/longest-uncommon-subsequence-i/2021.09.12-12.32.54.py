"""
brute force would be to find every subsequence of EACH string. Remove the ones in common. The find
the one with the longest length between them. But it's pretty complicated to do that and it would take a
long time.

after playing with a few examples, it appears the longest substring is the length of the longest string
unless they are equal
"""

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))