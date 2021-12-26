class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums, res = set(arr), 0
        for item in arr:
            if item + 1 in nums:
                res += 1
        return res
