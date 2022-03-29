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
[1,3,5,6]
"""
from collections import defaultdict
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        mod_index = 0
        for i in range(1, len(rounds)):
            if rounds[i] + (n * mod_index) < rounds[i - 1]:
                mod_index += 1
            rounds[i] += n * mod_index
        rounds[-1] +=1  # deal with exclusive
        counts = defaultdict(int)
        for i in range(1, len(rounds)):
            start, end = rounds[i - 1], rounds[i]
            for val in range(start, end):
                counts[val % n if val % n != 0 else n] += 1
        best = max(counts.values())
        return sorted([k for k, v in counts.items() if v == best])