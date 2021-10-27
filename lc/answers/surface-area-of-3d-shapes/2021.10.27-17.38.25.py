class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total = 0
        n = len(grid)
        for i, row in enumerate(grid):
            for j, cube in enumerate(row):
                if cube:
                    # assuming it's in isolation
                    total += 2 + (cube * 4)

                    # remove left
                    if j > 0: 
                        total -= min(cube, row[j - 1])

                    # remove top
                    if i > 0:
                        total -= min(cube, grid[i - 1][j])

                    # remove right
                    if j < n - 1:
                        total -= min(cube, row[j + 1])

                    # remove bottom
                    if i < n - 1:
                        total -= min(cube, grid[i + 1][j])
        return total
