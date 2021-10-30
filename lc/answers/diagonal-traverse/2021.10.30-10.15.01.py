"""
===== Initial Thoughts =====
I wonder if there's a different way to solve this. What if we could solve it
by moving over one by one instead of getting whole diagonals and reversing some... I 
think this is the answer in solutions. It seems like it's much more efficient because
it's driven by pure logic. It's just going to be tricky to get the logic just right.
Granted it was difficult to do the logic the other way as well.

=== Implemented Approach ===
pure logic

~~Complexity Analysis
Time - O(m * n)
Space - O(1)
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        going_up = True
        h, w = len(mat), len(mat[0])
        i, j = 0, 0
        res = []
        for _ in range(w * h):
            # add current point
            res.append(mat[i][j])
            
            # move to next point
            if going_up: 
                if i != 0 and j != (w - 1): # try up right diag
                    i -= 1
                    j += 1
                elif j != (w - 1): # else try right (and flip)
                    j += 1
                    going_up = False
                else: # else down (if last doesn't matter) (and flip)
                    i += 1
                    going_up = False

            else:
                if i != (h - 1) and j != 0: # try down left diag
                    i += 1
                    j -= 1
                elif i != (h - 1): # else try down (and flip)
                    i += 1
                    going_up = True
                else: # else right (and flip)
                    j += 1
                    going_up = True
        return res