"""
===== Initial Thoughts =====
we should be able to do this in place by having two pointers.
We'll scan for the first incorrect one
then we'll send another pointer out ahead looking for another incorrect one
we'll swap them and increment the base pointer one ahead of the right positioned
one we swapped

~~Complexity Analysis
Time - O(n)
Space - O(1)

[648,831,560,986,192,424,997,829,897,843]
"""

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] % 2 != i % 2:
                j = i + 1
                while nums[j] % 2 == j % 2 or nums[j] % 2 == nums[i] % 2: j += 1
                other_wrong_one = nums[j]
                nums[j] = nums[i]
                nums[i] = other_wrong_one
            i += 1
        return nums