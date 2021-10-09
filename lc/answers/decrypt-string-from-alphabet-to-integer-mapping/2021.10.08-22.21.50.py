"""
===== Initial Thoughts =====
use regex (!) to profit
"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        letters = "_abcdefghijklmnopqrstuvwxyz"
        final = ""
        regex = re.compile("(\d\d#)|(\d)")
        for left, right in regex.findall(s):
            final += letters[int(left[0:2] if left else right)]
        return final