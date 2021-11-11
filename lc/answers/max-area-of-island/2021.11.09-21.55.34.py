"""
===== Initial Thoughts =====
iterate over each item in the matrix... if we find a land, we'll break
out and find other joined land squares. We'll add these all to a new set.

Then we'll proceed on the normal path again. If we run into another land mass,
then we'll check all our sets first to see if it has already been explored. If it has
then just go down the normal path again. If it hasn't been explored, create a new set
and apply that land hunting algorithm to it.

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
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def fn(i, j, s):
            # assume everything passed in here is valid land

            s.add((i, j))

            # for each one, if it's land, recurse

            # check up
            if i != 0 and grid[i - 1][j] and (i - 1, j) not in s:
                fn(i - 1, j, s)
            # check down
            if i != (len(grid) - 1) and grid[i + 1][j] and (i + 1, j) not in s:
                fn(i + 1, j, s)
            # check left
            if j != 0 and grid[i][j - 1] and (i, j - 1) not in s:
                fn(i, j - 1, s)
            # check right
            if j != (len(grid[0]) - 1) and grid[i][j + 1] and (i, j + 1) not in s:
                fn(i, j + 1, s)

        sets = []
        for i, row in enumerate(grid):
            for j, land in enumerate(row):
                if land:
                    # does it exist in a set?
                    found = False
                    for s in sets:
                        if (i, j) in s:
                            found = True
                            break
                    if not found:
                        new_set = set()
                        fn(i, j, new_set)
                        sets.append(new_set)
        return max(map(len, sets)) if len(sets) else 0
