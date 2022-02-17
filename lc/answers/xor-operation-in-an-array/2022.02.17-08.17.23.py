class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(start, n * 2 + start, 2):
            res ^= i
        return res