"""
===== Initial Thoughts =====
like making change for a dollar

[2,3,6,7], 7

fn(0,7,[])
    fn(0,5,[2])
        fn(0,3,[2,2])
            fn(0,3,[2,2])
            fn(1,3,[2,2])
            fn(2,3,[2,2])
            fn(3,3,[2,2])
        fn(1,2,[2,3])
        fn(2,-,[2]) -> Nope
        fn(3,-,[2]) -> Nope
    fn(1,4,[3])
    fn(2,1,[6])
    fn(3,0,[7]) -> add it

"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.combos = []
        self.recurse(0, target, [])
        return self.combos

    def recurse(self, i, curr, path):
        if curr == 0:
            self.combos.append(path)
        if curr > 0:
            for j in range(i, len(self.candidates)):
                cand = self.candidates[j]
                self.recurse(j, curr - cand, path + [cand])
