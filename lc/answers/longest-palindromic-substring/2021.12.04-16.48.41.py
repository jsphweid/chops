"""
=== Brute Force Approach ===
iterate over each char... try to widen the palindrome. when you find a longer one, save it

~~Complexity Analysis
Time - O(n*2)
Space - O(n)

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = (0, "")
        for i in range(len(s)):
            l, r = i, i
            longest = max(longest, self._find_longest(s, i, i))
            if i > 0 and s[i] == s[i - 1]:
                longest = max(longest, self._find_longest(s, i - 1, i))
        return longest[1]

    def _find_longest(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return (r - l, s[l + 1: r])
