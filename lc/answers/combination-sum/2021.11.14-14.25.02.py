"""
candidates = [2,3,6,7], target = 7
dfs([2,3,6,7], 7, [], [])
    dfs([2,3,6,7], 5, [], [2])
        dfs([2,3,6,7], 3, [], [2,2])
        dfs([3,6,7], 2, [], [2,3])
        dfs([6,7], -1, [], [2,6])
        dfs([7], -7, [], [2,7])
    dfs([3,6,7], 4, [], [3])
    dfs([6,7], 1, [], [6])
    dfs([7], 0, [], [7])
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, res, [])
        return res

    def dfs(self, candidates, target, res, path):
        if target == 0:
            res.append(path)
        elif target > 0:
            for i, candidate in enumerate(candidates):
                self.dfs(candidates[i:], target - candidate, res, path + [candidate])