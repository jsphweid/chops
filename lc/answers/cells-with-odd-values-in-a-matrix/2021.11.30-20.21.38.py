"""
===== Initial Thoughts =====
can be done with simulation fairly easily
but it can also probably be done with sheer insight
not sure I have that today though...

=== Brute Force Approach ===
simulate the thing

~~Complexity Analysis
Time - O(m*n*i)? worse case, every indices has [1,1] which means op applied to m and n, i times
Space - O(m*n)

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 


tracing
m = 2, n = 3, indices = [[0,1],[1,1]]
[[1,3,1],[1,3,1]]

"""

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = []
        for _ in range(m):
            matrix.append([0] * n)
        for r, c in indices:
            for i in range(n):
                matrix[r][i] += 1
            for i in range(m):
                matrix[i][c] += 1
        odd_count = 0
        for row in matrix:
            for item in row:
                odd_count += item & 1
        return odd_count




