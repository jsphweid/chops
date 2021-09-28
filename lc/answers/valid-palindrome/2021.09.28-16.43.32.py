"""
===== Initial Thoughts =====
let's do a very efficient two pointer approach...

=== Implemented Approach ===
start a pointer at beginning and end. find first alpha on each side (may have to skip over a bit)
and assert lowercase is the same. then find next alpha (may have to skip over a bit) and do the same
until the pointers are crossed (?)

~~Complexity Analysis
Time - O(n)
Space - O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        left, right = 0, len(s) - 1
        while left < right:

            # find next left
            while not s[left].isalnum() and left < right:
                left += 1

            # find next right
            while not s[right].isalnum() and left < right:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
