"""
===== Initial Thoughts =====
first thought is to add each 1 to some row and column dict
[1,0,0]
[0,0,1]
[1,0,0]
rows={0: 1, 1: 1, 2: 1}
cols={0: 2, 1: 0, 2: 1}
iterate through all ones... (0,0) (1,2) (2,0)

~~Complexity Analysis
Time - O(mn)
Space - O(mn)
"""
from collections import defaultdict
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols, ones = defaultdict(int), defaultdict(int), []
        for i, row in enumerate(mat):
            for j, item in enumerate(row):
                if item:
                    rows[i] += 1
                    cols[j] += 1
                    ones.append((i, j))
        return sum([rows[i] == 1 and cols[j] == 1 for i, j in ones])
