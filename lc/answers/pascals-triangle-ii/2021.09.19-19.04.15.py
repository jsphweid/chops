"""
I wanted to solve this problem with Dynamic Programming techniques.
It's a perfect use case for it since the problem can be simply defined in a recursive manner
and then optimized.
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cache = {}
        def get_num(r, c):
            key = f"{r},{c}"
            if key in cache: return cache[key]
            if r < 2: return 1
            if c == 0: return 1
            if r == c: return 1
            left = get_num(r - 1, c)
            right = get_num(r - 1, c - 1)
            cache[key] = left + right
            return cache[key]

        # since we know the i-th row will have i + 1 columns...
        return [get_num(rowIndex, i) for i in range(rowIndex + 1)]