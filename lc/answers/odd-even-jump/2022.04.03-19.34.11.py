"""
===== Initial Thoughts =====
odd - must be greater than or equal to
even - must be less than or equal to

1,2,4

=== Brute Force Approach ===
with a cache...

from math import inf
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        res = 1
        cache = {}  # position, oddness -> True/False
        for i in range(len(arr) - 1):
            steps = []
            dud = False
            is_odd = True

            while True:
                if (i, is_odd) in cache:
                    steps = []
                    dud = not cache[(i, is_odd)]
                    break
                if is_odd:
                    # next highest, lowest index
                    nxt = (inf, inf)
                    for j in range(i + 1, len(arr)):
                        if arr[j] >= arr[i]:
                            nxt = min(nxt, (arr[j], j))
                else:
                    # next lowest, lowest index
                    nxt = (-inf, -inf)
                    for j in range(i + 1, len(arr)):
                        if arr[j] <= arr[i]:
                            nxt = max(nxt, (arr[j], -j))

                if nxt == (inf, inf) or nxt == (-inf, -inf):
                    dud = True
                    break

                steps.append((i, is_odd))

                i = nxt[1] if is_odd else -nxt[1]
                if i == len(arr) - 1:
                    break
                is_odd = not is_odd

            if dud:
                for step in steps:
                    cache[step] = False
            else:
                for step in steps:
                    cache[step] = True
                res += 1
        return res

This TLE's... but what if we went backwards.
Still just as slow

what about recursion?
from math import inf
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        N = len(arr)
        @cache
        def reaches_end(i, is_odd):
            if i == N - 1:
                return True
            if is_odd:  # next highest, lowest index
                nxt = (inf, inf)
                for j in range(i + 1, len(arr)):
                    if arr[j] >= arr[i]:
                        nxt = min(nxt, (arr[j], j))
            else:  # next lowest, lowest index
                nxt = (-inf, -inf)
                for j in range(i + 1, len(arr)):
                    if arr[j] <= arr[i]:
                        nxt = max(nxt, (arr[j], -j))

            if nxt == (inf, inf) or nxt == (-inf, -inf):
                return False
            nxt_i = nxt[1] if is_odd else -nxt[1]
            return reaches_end(nxt_i, not is_odd)


        return sum([reaches_end(j) for j in range(N-1,-1,-1)])

still TLE... need to read discussions, but I know that the slow down comes from
constantly finding the next highest

Read discussions, turns out there is a clever way to do this by sorting first
then using a stack. I suspected something like this exists, but couldn't figure
it out. Interesting!

"""

def make_next_highest(lst):
    # lst is like [(1,2),(1,3),(2,0),(3,1),(4,4)]
    res = [None] * len(lst)
    stack = []
    for val, i in lst:
        while stack and stack[-1] < i:
            res[stack.pop()] = i
        stack.append(i)
    return res

from math import inf
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        N = len(arr)

        nxt_hi = make_next_highest(sorted([(val, i) for i, val in enumerate(arr)]))
        nxt_lo = make_next_highest(sorted([(-val, i) for i, val in enumerate(arr)]))

        @cache
        def reaches_end(i, is_odd):
            if i == N - 1:
                return True
            nxt = nxt_hi[i] if is_odd else nxt_lo[i]
            return reaches_end(nxt, not is_odd) if nxt else False
        return sum([reaches_end(j, True) for j in range(N-1,-1,-1)])






