"""
===== Initial Thoughts =====
should be possible with two pointers... one with the original, then the other scanning the larger str

=== Implemented Approach ===
start a pointer a 0 in s
loop over t
for each char, find the next letter in s starting with pointer at 0
if it can't be found in s, then return False
if it makes it to the end in t, then it must have worked

ahbgdc
abc

s index is 0
we're looping over abc
a -> looking at s, i=0, which is a, found! increment 1 and continue
b -> looking at s, i=1, which is h, not b, inner loop i=2, which is b, found! incrememnt 1 and continue
c -> looking at s, i=3, which is g, not c, inner loop i=4, which is d, not c, inner loop i=5

~~Complexity Analysis
Time - O(s + t) no need to repeat anything
Space - O(1)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not len(s): return True
        if not len(t): return False
        t_index = 0
        for char in s:
            while True:
                if t_index == len(t):
                    return False
                t_char = t[t_index]
                t_index += 1
                if char == t_char:
                    break
        return True