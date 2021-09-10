"""
A decent starting solution here would be to iterate over everthing. Then we're going to check up down left
right to determine if there are any 1's. Any 1's we find for that square we subtract from 4 since that's the
default number of edges (surrounded by water).
"""

def is_land(grid, i, j):
    if i < 0 or j < 0:
        return 0
    try:
        return grid[i][j]
    except Exception:
        return 0

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for i, row in enumerate(grid):
            for j, land in enumerate(row):
                if land:
                    edges = 4
                    edges -= is_land(grid, i - 1, j)  # if one above
                    edges -= is_land(grid, i, j - 1)  # if one left
                    edges -= is_land(grid, i, j + 1)  # if one right
                    edges -= is_land(grid, i + 1, j)  # if one below
                    count += edges
        return count
