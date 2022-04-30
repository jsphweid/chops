"""
===== Initial Thoughts =====
just build level by level and use recursion

=== Implemented Approach ===
from math import ceil
class Solution:
    def houseOfCards(self, n: int) -> int:
        if n == 1: return 0
        if n == 2: return 1

        # 0 bases can support 0 cards
        # 1 base can support 2 cards
        # 2+ bases can support 5,8,11,etc cards
        lookup = [0, 2] + list(range(5, n + 1, 3))
        for i in range(1, len(lookup)):
            lookup[i] += lookup[i - 1]

        @cache
        def count(n):
            total = i = 0
            while n >= 0:
                if i == 0:
                    n -= 2
                else:
                    n -= 3
                    # if we can support more
                    if n != 0 and n <= lookup[i]:
                        total += count(n)
                if n == 0:
                    total += 1
                i += 1
            return total
        return count(n)

The problem with this approach is that it's really hard to use unique 2's only once.

Gonna have to go to the discussions.

The coin change analogy makes a lot of sense.

The DP solution here https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/discuss/1817844/Coin-Change-O(N2)
is pretty interesting but hard for me to understand.

Let's do it my own way.

2, 5, 8, 11, 14, 17
recurse(0, 16)
    recurse(1, 14)
    recurse(2, 11)
    recurse(3, 8)
    recurse(4, 5)
    recurse(5, 2)
    recurse(5, -1)

~~Complexity Analysis
Time - 
Space - 
"""
class Solution:
    def houseOfCards(self, n: int) -> int:
        if n == 1: return 0
        if n == 2: return 1

        choices = [2] + list(range(5, n + 1, 3))
        choices.reverse()

        @cache
        def recurse(i, left):
            if left == 0:
                return 1
            if left < 0:
                return 0
            res = 0
            for j in range(i, len(choices)):
                res += recurse(j + 1, left - choices[j])
            return res

        return recurse(0, n)

