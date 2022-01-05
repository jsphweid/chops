"""
~~Complexity Analysis
Time - O(n2*m)

    def maxPoints(self, points: List[List[int]]) -> int:
        for i in range(len(points) - 1):
            nxt_row = points[i + 1][:]
            for j, top in enumerate(points[i]):
                for k, bottom in enumerate(points[i + 1]):
                    nxt_row[k] = max(nxt_row[k], top + bottom - abs(j - k))
            for j in range(len(nxt_row)):
                points[i + 1][j] = nxt_row[j]
        return max(points[-1])

that TLE'ed

After looking up the answer (*sigh*) the fast thing to do is to preprocess each row to spread
the points of each row. We want to find the maximum it can do to the next row so in 1-2 passes
we can get the max strength of each value in the row. After that, we can just add the values with
the next row.


"""

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        for i in range(m - 1):
            for j in range(n - 2, -1, -1):
                points[i][j] = max(points[i][j], points[i][j + 1] - 1)
            for j in range(n):
                points[i][j] = max(points[i][j], points[i][j - 1] - 1 if j else 0)
                points[i + 1][j] += points[i][j]
        return max(points[-1])