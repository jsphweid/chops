"""
===== Initial Thoughts =====


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
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        copy = [row[:] for row in img]
        for y, row in enumerate(img):
            for x, _ in enumerate(row):
                total = 1
                sum = img[y][x]                
                
                # top right
                if x != len(row) - 1 and y != 0:
                    total += 1
                    sum += img[y - 1][x + 1]

                # right
                if x != len(row) - 1:
                    total += 1
                    sum += img[y][x + 1]

                # bottom right
                if x != len(row) - 1 and y != len(img) - 1:
                    total += 1
                    sum += img[y + 1][x + 1]

                # top
                if y != 0:
                    total += 1
                    sum += img[y - 1][x]

                # bottom
                if y != len(img) - 1:
                    total += 1
                    sum += img[y + 1][x]

                # top left
                if x != 0 and y != 0:
                    total += 1
                    sum += img[y - 1][x - 1]

                # left
                if x != 0:
                    total += 1
                    sum += img[y][x - 1]

                # bottom left
                if x != 0 and y != len(img) - 1:
                    total += 1
                    sum += img[y + 1][x - 1]

                copy[y][x] = int(sum / total)
        return copy
            