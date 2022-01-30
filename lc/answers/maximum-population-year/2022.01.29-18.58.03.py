"""
=== Brute Force Approach ===
iterate through ranges of all the people. Step through each year of their life accumulating some count for each year.
There's only 100 years of life and death here. And only 100 people. This makes a brute force seem reasonable.

~~Complexity Analysis
Time - N * 100 so O(N) (num of logs)
Space - 100 .. so constant?
"""
from collections import defaultdict
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        counts = defaultdict(int)
        for birth, death in logs:
            for i in range(birth, death):
                counts[i] += 1
        best_count, best_year = 0, 1950
        for i in range(1950, 2051):
            if counts[i] > best_count:
                best_count = counts[i]
                best_year = i
        return best_year