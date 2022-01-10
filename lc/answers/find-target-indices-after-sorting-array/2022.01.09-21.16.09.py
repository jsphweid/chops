"""
def targetIndices(self, nums: List[int], target: int) -> List[int]:
    nums.sort()
    l = bisect.bisect_left(nums, target)
    if l == len(nums) or nums[l] != target:
        return []
    r = bisect.bisect_right(nums, target)
    return list(range(len(nums)))[l:r]

apparently this can be done in O(n)... so I'mma try that
I think we just need to count the number of targets and the number
less than the targets in one pass and then we can output the result
"""

import bisect
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lesser, num_targets = 0, 0
        for num in nums:
            if num < target:
                lesser += 1
            elif num == target:
                num_targets += 1
        return list(range(lesser, lesser + num_targets))
