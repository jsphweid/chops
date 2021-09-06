"""
probably going to use odd / even number palindrome theory here

we probably want all even and the highest odd number (if there is one)
1,1,4,2
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        num = 0
        odd_used = False
        for char in set(s):
            char_count = s.count(char)
            if char_count & 1:
                num += (char_count - 1)
                if not odd_used:
                    num += 1
                odd_used = True
            else:
                num += char_count
        return num
