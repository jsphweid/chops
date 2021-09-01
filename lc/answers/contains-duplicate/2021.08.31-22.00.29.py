class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        already_exists = set()
        for num in nums:
            if num in already_exists:
                return True
            already_exists.add(num)
        return False