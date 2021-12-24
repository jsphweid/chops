"""
===== Initial Thoughts =====
[3,  7],
[9, 11],
[15,16]

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        res, transposed = [], list(zip(*matrix))
        for i in range(M):
            min_num = min(matrix[i])
            for j in range(N):
                if matrix[i][j] == min_num:
                    if max(transposed[j]) == min_num:
                        res.append(min_num)
        return res

