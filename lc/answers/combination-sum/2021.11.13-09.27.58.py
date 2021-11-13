"""
tracing
candidates = [2,3,6,7], target = 7

recurse([2],2)
    recurse([2,2],4)
        recurse([2,2,2],6)
            recurse([2,2,2,2],8) -> None
            recurse([2,2,2,3],9) -> None
            recurse([2,2,2,6],12) -> None
            recurse([2,2,2,7],13) -> None
        recurse([2,2,3],7) -> [2,2,3]
        recurse([2,2,6],10) -> None
        recurse([2,2,7],11) -> None
    recurse([2,3],5)
        recurse([2,3,2],7) -> [2,3,2] -> None
        recurse([2,3,3],8) -> None
        recurse([2,3,6],11) -> None
        recurse([2,3,7],12) -> None
    recurse([2,6],8) -> None
    recurse([2,7],9) -> None
recurse([3],3)
    recurse([3,2],5)
        recurse([3,2,2],7) -> [3,2,2] -> None
        recurse([3,2,3],) -> None
        recurse([3,2,6],) -> None
        recurse([3,2,7],) -> None
    recurse([3,3],6) -> None (eventually)
    recurse([3,6],9) -> None
    recurse([3,7],10) -> None
recurse([6],6)
recurse([7],7) -> [7]
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def recurse(lst, x):
            if x == target:
                lst.sort()
                if lst not in res:
                    res.append(lst)
                return
            if x > target:
                return
            for candidate in candidates:
                recurse(lst + [candidate], x + candidate)
        for candidate in candidates:
            recurse([candidate], candidate)
        return res
