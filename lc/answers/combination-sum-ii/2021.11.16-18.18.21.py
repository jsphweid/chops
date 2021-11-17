"""
[3,4,4,5,6,6,6,8] target=12
[3,4,  5] a possible solution
[3,  4,5] a possible solution but shouldn't be because of duplicates
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, res, target, [])
        return res

    def dfs(self, candidates, res, target, path):
        if target == 0:
            res.append(path)
        elif target < 0:
            return
        else:
            for i in range(len(candidates)):
                if i != 0 and candidates[i] == candidates[i - 1]:
                    continue
                else:
                    self.dfs(candidates[i + 1:], res, target - candidates[i], path + [candidates[i]])
