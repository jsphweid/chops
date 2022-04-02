"""
binary search the answer?

or just order?

[0,4,3,0,4]
[0,0,3,4,4]
[4,4,3,0,0]
[55, 44, 33]
[5,3]

failed on [3,6,7,7,0]
[7,7,6,3,0]

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if i + 1 > nums[i]:
                return i if i and nums[i] != i else -1
        return len(nums)
