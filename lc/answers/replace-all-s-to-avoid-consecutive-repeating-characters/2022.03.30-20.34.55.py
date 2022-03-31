"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

def find_safe(a, b):
    for char in "abcd":
        if char != a and char != b:
            return char

class Solution:
    def modifyString(self, s: str) -> str:
        N = len(s)
        res = list(s)
        for i in range(N):
            if res[i] == "?":
                l = res[i - 1] if i else None
                r = res[i + 1] if i < N - 1 else None
                res[i] = find_safe(l, r)
        return "".join(res)

