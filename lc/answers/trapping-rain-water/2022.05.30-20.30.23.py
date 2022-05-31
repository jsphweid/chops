"""
===== Initial Thoughts =====
After thinking for 5 minutes, I think we just need to know at every point
where the highest point is to the left and right. We can raise that bar
up to the point that it doesn't exceed the highest left and right

~~Complexity Analysis
Time - O(n) I think
Space - O(n) I think

[0,1,0,2,1,0,1,3,2,1,2,1]
[0 0 1 1 2 2 2 2 3 3 3 3] left
[3 3 3 3 3 3 3 2 2 2 1 0] right
[0 0 1 1 2 2 2 2 2 2 1 0] min
[0,1,0,2,1,0,1,3,2,1,2,1]
     1   1 2 1     1  

Seems to work and make sense.

[5,2,3,0,2,4]
[0,5,5,5,5,5]

[4,2,0,3,2,5]
[0 4 4 4 4 4]
[5 5 5 5 5 0]
[0 4 4 4 4 0] maxes
[4,2,0,3,2,5]
[0 2 4 1 2 0] res => 9
"""

def highest(heights):
    highest = 0
    res = []
    for h in heights:
        res.append(highest)
        highest = max(h, highest)
    return res

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = highest(height), highest(height[::-1])[::-1]
        maxes = [min(l, r) for l, r in zip(left, right)]
        return sum([m - h if m > h else 0 for m, h in zip(maxes, height)])
