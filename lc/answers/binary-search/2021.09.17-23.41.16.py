class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while True:
            mid_index = (left + right) // 2
            num = nums[mid_index]
            if target == num:
                return mid_index
            if right - left == 1:
                return -1
            if num < target:
                left = mid_index
            else:
                right = mid_index
