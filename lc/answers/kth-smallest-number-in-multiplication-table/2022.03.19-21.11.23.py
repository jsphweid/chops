"""
=== Brute Force Approach ===
expand the whole multiplication table out into 1-d
then get that number

~~Complexity Analysis
Time - O(mn + mnlog(mn))
Space - O(mn)

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lst = []
        for i in range(1, m + 1):
            lst.extend(list(range(i, i * n + 1, i)))
        lst.sort()
        return lst[k - 1]

memory limit exceeded

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(num):
            total = 0
            for i in range(1, m + 1):
                row_sum = min(n, num // i)
                if not row_sum:
                    break
                total += row_sum
            return total
        l, r = 1, m * n
        while l < r:
            mid = (l + r) // 2
            if count(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return l











        