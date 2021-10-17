"""
===== Initial Thoughts =====
this problem again...
this problem is all about finding one number jumping to the next and what its difference is.
but if we find another difference that jumps off a previous known number, we need to increment
that overall distance by one. So for each number, we need to know the position and how much a diff
with the last.

So in [9,4,7,2,10]

index 0 -> index 1, diff is -5, and that length is 2 so far
index 0 -> index 2, diff is -2, and that length is 2 so far
index 0 -> index 3, diff is -7, and that length is 2 so far
index 0 -> index 4, diff is 1, and that length is 2 so far

index 1 -> index 2, diff is 3, and that length is 2 so far
index 1 -> index 3, diff is -2, and that length is 2 so far (index mismatch)
index 1 -> index 4, diff is 6, and that length is 2 so far

index 2 -> index 3, diff is -5, and that length is 2 so far (index mismatch)
index 2 -> index 4, diff is 3, and that length is 3 so far (MATCH)

index 3 -> index 4, diff is 8, and that length is 2 so far

3 is the highest...

I remember one solution storing everything in a dict where the key was the end index and the diff.
This allows you to find the previous run instantly. The value is the current progress. When you
write a new value, you add one to the previous run (if no run, defaults to 2 or 1 + 1)
"""

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                previous_run = d.get((i, diff))
                d[(j, diff)] = previous_run + 1 if previous_run else 2
        return max(d.values())
