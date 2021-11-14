class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        def dfs(idx, tar, path):
            if tar == 0:
                res.add(tuple(path))
            elif tar > 0:
                for i in range(idx, len(candidates)):
                    if i > idx and candidates[i] == candidates[i - 1]:
                        continue
                    cand = candidates[i]
                    dfs(i + 1, tar - cand, path + [cand])
        dfs(0, target, [])
        return [list(t) for t in res]