class Solution:
    def binaryGap(self, n: int) -> int:
        largest = 0
        current = -1
        while n:
            if current >= 0: current += 1
            if n & 1:
                largest = max(current, largest)
                current = 0
            n = n >> 1
        return largest
