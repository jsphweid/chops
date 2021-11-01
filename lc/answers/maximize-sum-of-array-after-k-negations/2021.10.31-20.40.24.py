"""
===== Initial Thoughts =====
so the interesting thing is that the max the result can be is if all the numbers are positive

I think the general strategy would be to order everything, find the k lowest numbers. Negate all the negatives so they are
positive. Use any additional negations on negating twice. If we have an odd number of negations, just pick the lowest number that
is positive to negate. I think we can use 0 as a dumping ground.

[4,2,3] k = 1
[2,3,4] -> [-2,3,4] => 5

[3,-1,0,2] k = 3
[-1,0,2,3] k = 3
[1,0,2,3] k = 2
0 is in there so we can dump it all there

[2,-3,-1,5,-4] k = 2
[-4,-3,-1,2,5]
[4,3,-1,2,5] => 13
"""

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if not k: break
            if nums[i] < 0:
                nums[i] *= -1
                k -= 1
        if k and k & 1 and 0 not in nums:
            nums.sort()
            nums[0] *= -1
        return sum(nums)
