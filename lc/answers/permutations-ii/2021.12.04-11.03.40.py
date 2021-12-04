class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if len(nums):
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]: continue
                self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)
        else:
            res.append(path)