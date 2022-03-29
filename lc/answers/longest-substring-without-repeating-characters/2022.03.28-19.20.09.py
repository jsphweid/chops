"""
===== Initial Thoughts =====
did this problem with brian. Got it right in 25 minutes

this is how I did it with for Brian
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        seen = set()
        longest = 0
        while j < len(s):
            if s[j] in seen:
                seen.remove(s[i])
                i += 1
            else:
                seen.add(s[j])
                j += 1
            longest = max(longest, len(seen))
        return longest

=== Implemented Approach ===
However, we can use a dict a be slightly faster...

~~Complexity Analysis
Time - O(n)
Space - O(1)

tetast
{t: 0}
i=0
j=0
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        longest, i = 0, 0
        for j, char in enumerate(s):
            if char in seen and seen[char] >= i:
                i = seen[char] + 1
            seen[char] = j
            longest = max(longest, j - i + 1)
        return longest




