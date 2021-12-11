"""
=== Brute Force Approach ===
11
9 2

~~Complexity Analysis
Time - O(n * avg_length_of_int_str)
Space - O(1)

1
2 9 -> True
"""

def is_no_zero(n: int) -> bool:
    return "0" not in set(str(n))

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if is_no_zero(i) and is_no_zero(n - i):
                return [i, n - i]
