"""
===== Initial Thoughts =====
finding the sequence is a matter of finding whichever element appears more than once
or whose absolute value is the lowest (either, but we have to rely on the second method
for list of length 3).

Once we know that number, we can start at the beginning and try to continue along the
sequence with the list -- when there is a discrepancy, then that's the value to return.

It's a two pass solution.

~~Complexity Analysis
Time - O(n)
Space - O(1)

tracing

[5,7,11,13]
lowest = (2, 2)
return 9

[15,13,12]
lowest = (1, -1)
return 14

FAILED on [0,0,0,0,0]
didn't consider edge case...

"""

from math import inf
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        lowest = (inf, 0)
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            lowest = min(lowest, (abs(diff), diff))
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff != lowest[1]:
                return lowest[1] + arr[i-1]
        return arr[0]