"""
===== Initial Thoughts =====
we can brute force this but I'm sure there is another way

=== Brute Force Approach ===
just compare every domino to another domino and add 1 if it's a pair

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

succeeds all but 1 test

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        total = 0
        for i in range(len(dominoes) - 1):
            for j in range(i + 1, len(dominoes)):
                (a, b), (c, d) = dominoes[i], dominoes[j]
                if (a == c and b == d) or (a == d and b == c):
                    total += 1
        return total

=== Implemented Approach ===
create a set of a pair as we iterate over them... if we've seen the pair before
in either permutation, then we add 1... if we haven't seen it, then add it to the set so
it is counted the next time

~~Complexity Analysis
Time - O(n)
Space - O(n)
a = 0 pairs
a b = 1 pair
a b c = 3 pairs
a b c d = 6 pairs ab ac ad bc bd cd
a b c d e = 10 pairs ab ac ad ae bc bd be cd ce de
a b c d e f = 15 ab ac ad ae af bc bd be bf cd ce cf de df ef

1 -> 0 *0
2 -> 1 *.5
3 -> 3 *1
4 -> 6 *1.5
5 -> 10 *2
6 -> 15 *2.5
7 -> 21 *3
8 -> 28 *3.5
9 -> 36 *4
"""
from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = defaultdict(int)
        for (a, b) in dominoes:
            domino = (a, b) if a < b else (b, a)
            counts[domino] += 1
        total = 0
        for num in counts.values():
            multiplier = (num - 1) / 2
            total += (num * multiplier)
        return round(total)