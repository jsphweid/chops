"""
recurse([2], 2)
    recurse([2,3,7], [2,2], 4)
        recurse([2,3,7], [2,2,2], 6) -> None (eventually)
        recurse([3,7], [2,2,3], 7) -> ANSWER
        recurse([7], [2,2,7], 11) -> None
    recurse([3,7], [2,3], 5)
        recurse([3,7], [2,3], 5)
    recurse([7], [2,7], 9) -> None
recurse([3], 3)
recurse([7], 7) -> ANSWER
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def recurse(cand, lst, x):
            if x == target:
                res.append(lst)
                return
            if x > target:
                return
            for i in range(len(cand)):
                recurse(cand[i:], lst + [cand[i]], x + cand[i])
        recurse(candidates, [], 0)
        return res
