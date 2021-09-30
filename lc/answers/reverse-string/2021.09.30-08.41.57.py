"""
===== Initial Thoughts =====
I think we can easily just swap with two pointers. We could just use .reverse() as well?

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            a, b = s[left], s[right]
            s[left] = b
            s[right] = a
            left += 1
            right -= 1
