"""
=== Brute Force Approach ===
find every possible permutation of len/2 using only numbers in the list. Find the one that maximizes 
variety. I'm not even sure how that can be done.

~~Complexity Analysis
Time - not sure
Space - could just store the best winning number as it (hopefully) gets lower

=== Implemented Approach ===
use a frequency dict, then iterate over the values leaving 1 of each. The amount you take away from each
are summed. if this number is greater than or equal to the number we were supposed to take away, then return 
the number of keys in that dict. Else subtract from the amount still needed to be deleted the number of keys.
When we 'remove the key' count, we're essentially killing variety but we have to.

~~Complexity Analysis
Time - O(3n)
Space - O(2n))
"""
from collections import defaultdict
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        counts = defaultdict(int)
        total_candies = 0
        for t in candyType: 
            counts[t] += 1
            total_candies += 1
        target = total_candies // 2
        can_delete = 0
        for value in counts.values(): 
            can_delete += value - 1
        return len(counts) if can_delete >= target else min(len(counts), target)
        