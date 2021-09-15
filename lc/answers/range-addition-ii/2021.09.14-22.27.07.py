class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m * n
        return min([a[0] for a in ops]) * min([a[1] for a in ops])