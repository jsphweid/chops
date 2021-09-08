class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_nums = set(range(1, len(nums) + 1))
        for num in nums:
            if num in all_nums:
                all_nums.remove(num)
        return list(all_nums)