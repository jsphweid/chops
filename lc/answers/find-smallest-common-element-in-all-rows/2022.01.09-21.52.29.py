from math import inf
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        pos = [0] * M
        while True:
            lo, hi = inf, -inf
            for i, j in enumerate(pos):
                if j == N:
                    return -1
                lo = min(lo, mat[i][j])
                hi = max(hi, mat[i][j])

            if lo == hi: # all items must have been the same
                return lo

            # adjust
            for i, j in enumerate(pos):
                if mat[i][j] != hi:
                    pos[i] += 1