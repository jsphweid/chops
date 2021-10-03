"""
=== Brute Force Approach ===
if m*n != r*c return `mat`
validate first
then stretch everything into one list
the chunk things back up

~~Complexity Analysis
Time - O(m*n * 2?)
Space - O(m*n)
"""

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c: return mat
        lst = []
        for row in mat:
            for item in row:
                lst.append(item)
        final = []
        for i in range(r): final.append(lst[i * c: (i * c) + c])
        return final