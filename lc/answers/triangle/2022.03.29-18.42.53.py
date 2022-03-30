"""
===== Initial Thoughts =====
this seems like a decent solution, but I think DP is just gonna be way better
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = float("inf")
        seen = {}
        def recurse(i, j, total=0):
            nonlocal res
            curr = triangle[i][j]
            nxt = curr + total
            if (i, j) in seen and nxt >= seen[(i, j)]:
                return
            seen[(i, j)] = nxt
            if i + 1 == len(triangle):  # last row
                res = min(res, nxt)
            else:
                recurse(i + 1, j, nxt)
                recurse(i + 1, j + 1, nxt)
        recurse(0, 0)
        return res

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
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j, num in enumerate(triangle[i]):
                prev_row = triangle[i - 1]
                last_row_idx = len(triangle[i]) - 1
                prev = 0
                if j == 0: prev = prev_row[j]
                elif j == last_row_idx: prev = prev_row[j - 1]
                else: prev = min(prev_row[j], prev_row[j - 1])
                triangle[i][j] = num + prev
        return min(triangle[-1])


