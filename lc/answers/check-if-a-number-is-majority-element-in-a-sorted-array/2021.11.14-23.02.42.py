# 3,5,5,5,7,8 target=5

# 3,5,5,5

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        count = 0
        while (len(nums) != l + count) and nums[l + count] == target:
            count += 1
        return count > (len(nums) / 2)