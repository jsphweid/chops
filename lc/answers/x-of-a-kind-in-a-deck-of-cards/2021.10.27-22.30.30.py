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
import math
from collections import defaultdict
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2: return False
        d = defaultdict(int)
        for card in deck: d[card] += 1
        
        vals = sorted(list(d.values()))
        gcd = vals[0]
        for i in range(1, len(vals)):
            gcd = math.gcd(gcd, vals[i])
        if gcd == 1: return False
        for val in d.values():
            if val % gcd != 0: return False
        return True