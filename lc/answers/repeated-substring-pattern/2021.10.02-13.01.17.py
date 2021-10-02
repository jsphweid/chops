"""
=== Brute Force Approach ===
if odd length, return false (EDIT: NO)
iterate over the letters up to the half way 
for each one, get a substring from the beginning up to that point, and multiply it out to the length
if it's equal return true, 
if ya get to the end, return false

~~Complexity Analysis
Time - 
Space - 

I failed on "babbabbabbabbab" which is odd.

The reality is that odd numbers are fine unless they are prime...
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) // 2):
            substr = s[0: i + 1]
            if len(s) % (i + 1) == 0:
                repeated = len(s) // (i + 1)
                if (substr * repeated) == s:
                    return True
        return False
