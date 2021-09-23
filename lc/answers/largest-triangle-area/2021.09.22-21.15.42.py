"""
===== Initial Thoughts =====
Going real deep on triangles here...

=== Brute Force Approach ===
takes every possible combination of three points and gives us the area of all of them, then returns
the max

3 points -> 1 possibility
4 points -> 4 possibilities
5 points -> 10 possibilities
6 points -> 19 possibilities

-- 123
    -> 1 possibility

-- 1234
123
124
134
234 -> 4 possibilities

-- 12345
123, 124, 125
134, 135, 145, 
234, 235, 245
345 -> 10 possibilities

-- 123456
123, 124, 125, 126
134, 135, 136, 145
146, 234, 235, 236
245, 246, 256, 345
346, 356, 456 ->> 19 possibilities

There must be some insight... Those are unique permutations. I don't think 
we can cache / solve via DP.

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    xa, ya = points[i]
                    xb, yb = points[j]
                    xc, yc = points[k]
                    area = max(area, 0.5 * abs(((xa - xc) * (yb - ya)) - ((xa - xb) * (yc - ya))))
        return area
