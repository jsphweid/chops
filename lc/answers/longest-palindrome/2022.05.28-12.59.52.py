"""
abccccdd
a:1
b:1
c:4
D:2

failed on ccc
odds = 9
"""
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = False
        evens = 0
        for count in Counter(s).values():
            if count % 2 == 0:
                evens += count
            else:
                odds = True
                evens += count - 1
        return evens + odds
