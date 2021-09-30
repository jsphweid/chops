"""
===== Initial Thoughts =====
should be easy if you sort it

=== Brute Force Approach ===
for each num in the list, iterate over all the others and tally which ones are lower

~~Complexity Analysis
Time - O(n^2)
Space - O(n)

=== Implemented Approach ===
sort the list first
create a dict then iterate over it twice. 
once to build the dict -> each item adds to the dict the index.
    if you encounter a duplicate, ignore
again in the order of the list, essentially just spitting out the values in the map

~~Complexity Analysis
Time - O(3nlog(n))
Space - O(2n)
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        d = {}
        for i, num in enumerate(sorted_nums):
            if num not in d:
                d[num] = i
        return [d[num] for num in nums]