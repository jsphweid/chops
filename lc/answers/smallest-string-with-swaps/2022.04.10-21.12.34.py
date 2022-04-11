"""
===== Initial Thoughts =====
at first I'm thinking DFS through all possibilities keeping the smallest
but this is pretty ridiculous considering the size of that graph
can't we just swap greedily?

the problem comes with 3+ way swaps
really since we can swap infinite times then we just need to track
the distinct islands/groups of nodes and sort those greedily

this problem is really an island finding problem I believe.
We just need to find the indices and characters that belong to it. Sort
the indices of each island and write them to a final list using the indices.

To find islands we could use union find but I've kinda forgotten it.
Let's try to remember it for this problem!

~~Complexity Analysis
Time - O(nlogn) (I think, because sorting is the worst component)
Space - O(n)

s = "dcab", pairs = [[0,3],[1,2],[0,2]]
[0,0,1,0]

0: ["d", "c", "a", "b"]
0: ["a", "b", "c", "d"]

uf = [0,1,2,3]
"dcab"
[[0,3],[1,2]]

"""
from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = list(range(len(s)))
        def find(i):
            if i == uf[i]:
                return i
            res = find(uf[i])
            uf[i] = res
            return res
        for p, q in pairs:
            pp, qq = find(p), find(q)
            uf[qq] = pp
        d = defaultdict(list)
        for i, char in enumerate(s):
            d[find(i)].append(char)
        for k, v in d.items():
            d[k] = sorted(v, reverse=True)
        res = []
        for i in range(len(s)):
            res.append(d[find(i)].pop())
        return "".join(res)