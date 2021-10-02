"""
===== Initial Thoughts =====
man... after this I'm reading someone else's solution...

=== Brute Force Approach ===
iterate up to the number. For each number, check if it's prime by doing the hard work.
return a count 

That times out...
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        if n < 4: return n - 2
        lst = [True] * n
        lst[2::2] = [False] * len(lst[2::2])
        lst[0] = lst[1] = False
        lst[2] = True
        for i in range(3, int(n ** 0.5) + 1):
            if lst[i]:
                lst[i::i] = [False] * len(lst[i::i])
                lst[i] = True
        return sum(lst)