from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        N = len(nums)
        for i in range(len(nums) - 2):
            l = i + 1
            r = N - 1
            while l < r:
                result = nums[i] + nums[l] + nums[r]
                if result > 0: r -= 1
                elif result < 0: l += 1
                else:
                    res.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    r -= 1
                    l += 1
        return [list(r) for r in res]
            
