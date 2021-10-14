"""
=== Brute Force Approach ===
use two pointers to swap every combination and see if it equals the original

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

=== BETTER ===
we can put everything in a map... wwait

basic the strings have to be equal, except for exactly 2 or 0 spots.
if it's 2, then left of one should be the right of the other and visa versa
aaa bbb -> bad
abc acb -> good

if it's 0, that means there has to be at least one letter that is in there twice.
aab aab -> good
ab ab -> bad

tracing:
ab  ba 

a!=b and b!=a
diffs=[0, 1]

"""
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        existing = set()
        at_least_two_same = False
        diffs = []
        for i in range(len(s)):
            if s[i] in existing: at_least_two_same = True
            existing.add(s[i])
            if s[i] != goal[i]: diffs.append(i)
        if not len(diffs): return at_least_two_same
        if not len(diffs) == 2: return False
        return s[diffs[0]] == goal[diffs[1]] and s[diffs[1]] == goal[diffs[0]]

