"""
[1,2,3]
dfs([1,2,3], [], {})
    dfs([2,3], [1], {})
        dfs([3], [1,2], {})
        dfs([2], [1,3], {})
    dfs([1,3], [2], {})
        dfs([3], [2,1], {})
        dfs([1], [2,3], {})
    dfs([1,2], [3], {})
        dfs([2], [3,1])
        dfs([1], [3,2])
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        self.dfs(nums, [], res)
        return [list(r) for r in res]

    def dfs(self, nums, path, res):
        if len(nums):
            for i, n in enumerate(nums):
                new_nums = nums[:i] + nums[i + 1:]
                self.dfs(new_nums, path + [n], res)
        else:
            res.add(tuple(path))
