class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1: return [0]
        res, total = [], 0
        for i in range(n - 1):
            res.append(i + 1)
            total += i + 1
        return res + [-total]