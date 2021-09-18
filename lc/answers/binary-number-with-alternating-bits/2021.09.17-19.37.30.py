class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        parity = n & 1 == 1
        while n:
            # compare it with is_odd
            if not (n & 1 == parity):
                return False
            # shift
            n = n >> 1
            # invert
            parity = not parity
        return True