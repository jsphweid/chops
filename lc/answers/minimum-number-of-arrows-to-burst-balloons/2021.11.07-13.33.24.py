"""
===== Initial Thoughts =====
[[10,16],[2,8],[1,6],[7,12]]
[[1,6],[2,8],[7,12][10,16]]

[[1,2],[3,4],[5,6],[7,8]]

[[1,2],[2,3],[3,4],[4,5]]

[[1,99],[3,6],[3,7],[7,88]]
[[3,6],[3,7],[7,88],[1,99],]

=== Brute Force Approach ===
order by the x-end
for each x-end,eliminate all relevant balloons,repeat

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

[]
count = 2
left_point_end_x=6
left_point_end_x=12

[[3,6],[3,7],[7,88],[1,99]]

count=2
[]
left_point_end_x=10


def findMinArrowShots(points):
    points.sort(key=lambda x: x[1])
    count = 0
    while len(points):
        left_point_end_x = points.pop(0)[1]
        count += 1
        while len(points) and points[0][0] <= left_point_end_x <= points[0][1]:
            points.pop(0)
    return count

after looking at the answers... let's do it without .pop()'ing
[[1,2],[3,4],[5,6],[7,8]]
"""

class Solution:
    def findMinArrowShots(self,points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 0
        last_arrow = float("inf") * -1
        for point in points:
            if point[0] > last_arrow:
                count += 1
                last_arrow = point[1]
        return count
