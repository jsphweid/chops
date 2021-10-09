"""
===== Initial Thoughts =====
how can we solve this with regex?
"Test1ng-Leet=code-Q!"
"Qedo1ct-eeLg=ntse-T!"

TestngLeetcodeQ
QedocteeLgntseT -is backwards

find replace every other one as some special char? and then go through it?

=== Brute Force Approach ===
use regex to find all letters
use regex to replace all relevant chars with 'a'
iterate over all letters, filling in "a" with next .pop()
"""
import re
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = re.findall(r"[a-zA-Z]", s)
        output = ""
        for char in s: output += letters.pop() if char.isalpha() else char
        return output