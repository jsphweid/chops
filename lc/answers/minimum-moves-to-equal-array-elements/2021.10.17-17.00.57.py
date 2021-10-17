"""
===== Initial Thoughts =====
123
233
343
444 (3 moves)

1223
2333
3443
4544
5555 (4 moves)

1333
2443
3454
4555
5665
6676
7777 (6 moves)

1113
2223
3333 (2 moves)

distance of every num to minimum
"""

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = min(nums)
        return sum([n - m for n in nums])
        