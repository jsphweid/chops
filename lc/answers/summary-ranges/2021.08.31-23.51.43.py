"""
I think we can solve this recursively fairly easily...

But I'm not sure what the benefit is because I don't think it's going to simplify anything
conceptually.

On second thought, I think it might
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not len(nums):
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        i = 1
        while True:
            if nums[i] - nums[i - 1] != 1:
                what_we_have = [str(nums[0])] if i == 1 else [f"{nums[0]}->{nums[i - 1]}"]
                return what_we_have + self.summaryRanges(nums[i:len(nums)])
            elif i + 1 == len(nums):
                return [f"{nums[0]}->{nums[i]}"]
            else:
                i += 1
        # return whatever_i_have_now + summaryRanges(nums[whereILeftOff:len(nums)])