class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        for i in range(8, -1, -1):
            power = k ** i
            divisor = n // power
            res += divisor
            n -= divisor * power
        return res
