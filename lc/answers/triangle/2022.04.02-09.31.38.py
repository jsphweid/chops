"""
let's try recursion... again
dfs(0, 0) -> 11
    dfs(1, 0) -> 9
        dfs(2, 0) -> 7
            dfs(3, 0) -> 4
            dfs(3, 1) -> 1
        dfs(2, 1) -> 6
            dfs(3, 1) -> 1
            dfs(3, 2) -> 8
    dfs(1, 1) etc
"""

class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            if i + 1 == len(A): return A[i][j]
            return min(A[i][j] + dfs(i+1, j), A[i][j] + dfs(i+1, j+1))
        return dfs(0, 0)