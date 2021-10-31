"""
=== Implemented Approach ===
should be very easy. we have an outer loop that iterates over the length of the strings then an inner loop
that goes runs over that 'position' in each word. we could start on the second index and always do a compare
with the last. if each character isn't the same or increasing, then we break out of that loop and add one to
some counter

["cba","daf","ghi", "zzz"]

for each, we'll iterate 1,2,3
col=0
d < c nope
g < d nope
z < g nope

col=1
a < b TRUE
h < a nope
z < h nope

col=2
f < a nope
i < f nope
z < i nope

answer should be 1

~~Complexity Analysis
Time - O(N * str_length)
Space - O(1)
"""

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    count += 1
                    break
        return count