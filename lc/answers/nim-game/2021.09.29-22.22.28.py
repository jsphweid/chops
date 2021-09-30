"""
===== Initial Thoughts =====
honestly I know this is pretty easily solved with math, but we can also use dynamic programming I think
let's try that

=== Brute Force Approach ===
get every possible permutation/sequence. If you can win in at least 1 route, the answer is true. wait that's not really correct.
I might need to draw this one out. I'm at Shakes... I'll have to revist this... For now, let's answer with math (again).

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===
Math... If divisible by 4 return False

~~Complexity Analysis
Time - O(1)
Space - O(1)
"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4