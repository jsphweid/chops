"""

"""
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def fn(num):
            if num == 1: return 0
            if num & 1: return 1 + fn(3 * num + 1)
            return 1 + fn(num // 2)
        return sorted([(fn(i), i) for i in range(lo, hi+1)])[k-1][1]