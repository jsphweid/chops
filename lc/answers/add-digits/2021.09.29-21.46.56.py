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
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        num_zeros = math.floor(math.log10(num))
        return self.addDigits(sum([int(x) for x in str(num)])) if num_zeros else num