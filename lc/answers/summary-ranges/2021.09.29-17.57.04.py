"""
=== Implemented Approach ===
start on second item keep track of the last and an anchor.
when the current is more than 1 num away from the last, then write a new item to the list
reset anchor and last when this happens
at the end, write whatever item is at the anchor/last

~~Complexity Analysis
Time - O(n)
Space - O(1)
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not len(nums): return []
        ret = []
        last = anchor = nums[0]
        for i in range(1, len(nums)):
            if abs(last - nums[i]) > 1:
                ret.append(f"{anchor}->{last}" if abs(anchor - last) > 0 else str(anchor))
                anchor = nums[i]
            last = nums[i]
        ret.append(f"{anchor}->{last}" if abs(anchor - last) > 0 else str(anchor))
        return ret
