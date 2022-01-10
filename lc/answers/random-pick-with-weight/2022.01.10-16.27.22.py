"""
===== Initial Thoughts =====

=== Brute Force Approach ===
[1,3] -> [0,1,1,1]
but that would not work as the values of the list can be very large and it would
end up using an exorbitant amount of memory (list with 1,000,000,000 items)

=== Implemented Approach ===
Although that number is smaller than an int32 (even if python can have arbitrary large numbers)
I wonder if we were to choose a number from 0->3 then somehow compute which index it would be on
in a billion length arr. Or maybe the starts...

[1,3,7,2,1,9]
[0,1,4,11,13,14] 22
l=0 r=5 mid=2
l=3 r=5 mid=4
l=4 r=5 mid=4
l=5 r=5 mid



~~Complexity Analysis
Time - O(n) for init
Space - O(logn) for query

[14, 1, 7]
[0,14,15,22]
0 -> 21
val=2
l=0 r=2 mid=1
l=0 r=1 mid=0
"""
import random
class Solution:

    def __init__(self, w: List[int]):
        self.lst = [0]
        for num in w:
            self.lst.append(self.lst[-1] + num)

    def pickIndex(self) -> int:
        val = random.randint(1, self.lst[-1])
        l, r = 0, len(self.lst) - 1
        while l < r:
            mid = (l + r) // 2
            if self.lst[mid] < val:
                l = mid + 1
            else:
                r = mid
        return l - 1
