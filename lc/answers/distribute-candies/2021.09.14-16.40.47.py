"""
Brute force solution here is to get the quantities of each integer
and then loop over a list of those quantities, finding the maximum quantity,
then reducing it by 1 until n/2 has been eliminated.

A more clever strategy would be to just decimate every number greater than 1 to
1. If you still need more room, then the answer is the result of subtracting
the number of types by the remaining number to delete.
"""

from collections import defaultdict

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        counts = defaultdict(int)
        total_num_candies = 0
        for c in candyType:
            counts[c] += 1
            total_num_candies += 1
        num_easily_eliminated = 0
        for val in counts.values():
            num_easily_eliminated += (val - 1)
        if num_easily_eliminated >= len(counts.keys()):
            return len(counts.keys())
        else:
            return len(counts.keys()) - ((total_num_candies // 2) - num_easily_eliminated)
            