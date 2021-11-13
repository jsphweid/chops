class Prev:
    def __init__(self):
        self.d = {}
    def exists(self, lst):
        curr = self.d
        for num in lst:
            if num in curr:
                curr = curr[num]
            else:
                return False
        return "*" in curr
    def add(self, lst):
        curr = self.d
        for num in lst:
            if num in curr:
                curr = curr[num]
            else:
                curr[num] = {}
                curr = curr[num]
        curr["*"] = True

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        prev = Prev()
        def recurse(lst, x):
            if x == target:
                lst.sort()
                if not prev.exists(lst):
                    res.append(lst)
                    prev.add(lst)
                return
            if x > target:
                return
            for candidate in candidates:
                recurse(lst + [candidate], x + candidate)
        for candidate in candidates:
            recurse([candidate], candidate)
        return res