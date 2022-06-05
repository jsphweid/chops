"""
===== Initial Thoughts =====
2 - 1,2
3 - 1,3
4 - 1,2,4    $$$$$
5 - 1,5
6 - 1,2,3,6
7 - 1,7
8 - 1,2,4,8
9 - 1,3,9    $$$$$
10 - 1 2 5 10
25 - 1 5 25
49 - 1 7 49
81 - 1 3,9, 27 81

call recursively on 9?

=== Brute Force Approach ===
do math

~~Complexity Analysis
Time - O(n)
Space - O(1)
"""

class Solution:
    def isThree(self, n: int) -> bool:
        divisors = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
            if len(divisors) > 3:
                return False
        return len(divisors) == 3



