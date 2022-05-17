"""
===== Initial Thoughts =====


=== Brute Force Approach ===
wall = [
[1,2,2,1], => 2,4
[3,1,2], => 1,2,5
[1,3,2], => 2,3,5
[2,4], => 1,3,4,5
[3,1,2], => 1,2,5
[1,3,1,1]] => 2,3

=== Implemented Approach ===
go over the entire thing, in each row, add to some state
the presence of all crossings, then minimize that

or actually do this:

wall = [
[1,2,2,1], => 1,3,5
[3,1,2], => 3,4
[1,3,2], => 1,4
[2,4], => 2
[3,1,2], => 3,4
[1,3,1,1]] => 1,4,5

then maximize... then subtract from rows... i.e. 4 is most common
and it has 4 crossings. 6-4 => 2

~~Complexity Analysis
Time - O(m*n + n)
Space - O(n)

[0,3,1,3,4,2]
max is 4
N - 4 => 6 - 4 => 2
"""

from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        N = len(wall)
        open_spots = defaultdict(int)
        for i in range(N):
            acc = 0
            for j in range(len(wall[i]) - 1):
                acc += wall[i][j]
                open_spots[acc] += 1
        return N - max(open_spots.values()) if len(open_spots) else N
