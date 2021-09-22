"""
===== Initial Thoughts =====
I think this would be a fine candidate to practice Dynamic Programming.

On second thought I think a primitive brute force solution is the same. There is no explosion of possibilities
that would result in exponential time.

=== Brute Force Approach ===
For every item in the matrix, if one down and one right is a valid spot AND is a different number then return False.

~~Complexity Analysis
Time - O(m*n), maybe more precisely O((m-1)(n-1))
Space - O(1)

=== Implemented Approach ===
Brute force above, I think it's good as a first pass.
"""

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[i]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True