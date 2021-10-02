"""
=== Brute Force Approach ===
have a perimeter counter = 0
iterate through each rol/col
add 4 - num_neighbor to perimeter

~~Complexity Analysis
Time - O(m*n) where m/n are dimensions of list
Space - O(1)
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i, row in enumerate(grid):
            for j, land in enumerate(row):
                if land:
                    num = 4

                    # if top
                    if i != 0 and grid[i - 1][j]:
                        num -= 1
                    # if bottom
                    if i != (len(grid) - 1) and grid[i + 1][j]:
                        num -= 1
                    # if left
                    if j != 0 and grid[i][j - 1]:
                        num -= 1
                    # if right
                    if j != (len(row) - 1) and grid[i][j + 1]:
                        num -= 1

                    perimeter += num
        return perimeter