"""
[1,0,0,0,1,0,1]
person=True
0 1 left=0 middle=0 right=0 acc=0 person=True
1 0 left=0 middle=0 right=1 acc=1 person=True
2 0 left=0 middle=0 right=2 acc=2 person=True
3 0 left=0 middle=0 right=3 acc=3 person=True
4 1 left=0 middle=3 right=0 acc=0 person=True
5 0 left=0 middle=3 right=1 acc=1 person=True
6 1 left=0 middle=3 right=0 acc=0 person=True
"""

from math import ceil
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left, middle, right, acc, person = 0, 0, 0, 0, False
        for seat in seats:
            if seat:
                person = True
                right = 0
                middle = max(middle, acc)
                acc = 0
            else:
                if not person: left += 1
                acc += 1
                right += 1
        return max(left, ceil(middle/2), right)