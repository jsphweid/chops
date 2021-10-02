"""
=== Brute Force Approach ===
start with [the num, 1]
then iterate over numbers up to sqrt searching for better matches
if a better match exist override the starting values
"""

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        best = [area, 1]

        for i in range(2, int(area ** 0.5) + 1):
            if area % i == 0:
                best = [area // i, i]

        return best