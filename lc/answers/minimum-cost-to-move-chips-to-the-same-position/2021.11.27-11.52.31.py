"""
===== Initial Thoughts =====
just use odd even... hard part is figuring out which one is best to move it to. but if there
are 100 positions max, then maybe brute force is reasonable... let's try it.

=== Brute Force Approach ===
for each position in the list, see what the cost is for moving every item there. then see if that beats
a global

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

trace...

ACTUALLY, I misunderstood the input... For some reason I was thinking each array item
represented the number of coins at that position... So I wrote this:

```
    def minCostToMoveChips(self, position: List[int]) -> int:
        N = len(position)
        res = inf
        for i in range(N):
            cost = 0
            for j in range(N):
                cost += position[j] * abs(i - j)
            res = min(res, cost)
        return res
```

Now, what might be fun is to just convert the input to this and see how it does (it is still brute force).

Honestly that's horrible since you can have lists like `[1,1000000000]` which makes everything take
so long to process.

Actually we can use a map of counts and sorta do something similar

    def minCostToMoveChips(self, position: List[int]) -> int:
        counts = Counter(position)
        res = inf
        for anchor in counts.keys():
            cost = 0
            for num in counts.keys():
                diff = abs(num - anchor) % 2
                cost += diff * counts[num]
            res = min(res, cost)
        return res

=== Implemented Approach ===
We're trying to figure out the best position to go to, but really there are only 2 positions... even/odd.
Let's aggregate things into simply even and odd, then find out which is the better...

~~Complexity Analysis
Time - 
Space - 
"""
from collections import Counter
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        counts = {0: 0, 1: 0}
        for item in position: counts[item % 2] += 1
        return min(counts[0], counts[1])
