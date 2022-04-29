"""
===== Initial Thoughts =====
seems pretty simple. If it is sorted increasing, then if we diff
everything, there should only be 1 number that is negative

Got it wrong the first time because I didn't consider [1,1,1]
i.e. no negatives. I had return negatives == 1, it should be
return negatives <= 1, since 0 negatives is a valid case
"""

class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        negatives = 0
        for i in range(len(nums)):
            # in python nums[-1] is the last index which is perfect for that edge case
            negatives += (nums[i] - nums[i - 1] < 0)
        return negatives <= 1