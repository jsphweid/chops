class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        max_area = 0

        def _explore(i: int, j: int) -> int:
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or (i, j) in seen or not grid[i][j]:
                return 0
            seen.add((i, j))
            total = 1
            total += _explore(i - 1, j)
            total += _explore(i + 1, j)
            total += _explore(i, j - 1)
            total += _explore(i, j + 1)

        for i, row in enumerate(grid):
            for j, land in enumerate(row):
                area = _explore(i, j)
                max_area = max(max_area, area)
        return max_area
