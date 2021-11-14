"""
===== Initial Thoughts =====
[[10,16],[2,8],[1,6],[7,12]]

[[1,6],[2,8],[7,12],[10,16]]
sort by last digit, fire at last digit, see how many it takes out
last_arrow=6 used=1
last_arrow=12 used=2

"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])
        used = 0
        last_arrow = None
        for x_start, x_end in points:
            if last_arrow and x_start <= last_arrow <= x_end:
                continue
            else:
                last_arrow = x_end
                used += 1
        return used