"""
tracing
[[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
al = {2:[(1,1),(3,1)],3:[(4,1)]}
all_nodes={1,2,3,4}

touched={2,1,3,4}

longest(2, 0) => 2
    max_length = 2
    longest(1, 1) => 1
    longest(3, 1) => 2
        max_length = 2
        longest(4, 2) => 2

[[1,2,1]], n = 2, k = 2
al = {1:[(2,1)]}
touched={2}
longest(2,0)

times = [[1,2,1]], n = 2, k = 1
al = {1:[(2,1)]}
all={1,2}
touched={1,2}
longest(1,0) => 1
    max_length = 0
    longest(2, 1) => 1

FAILED ON...
[[1,2,1],[2,1,3]]
al = {1:[(2,1)],2:[(1,3)]} 2 2
all = {1,2}
seen={2}
longest(2,0)
    max_length = 0
    longest()
oh there's a loop

FAILED ON [[1,2,1],[2,1,3]]
al = {1:[(2,1)],2:[(1,3)]} 2 2
seen={}
longest(2,0)
    longest(1)
we need to have an initial value in touched...

FAILED On [[1,2,1],[2,1,3]] 2 2 (again) but this time I return 0, not 4 (correct is 3...)

[[1,2,1],[2,1,3]] 2 2
al = {1:[(2,1)],2:[(1,3)]} 2 2
seen={2}
longest(2,0)
    max_length = 0
    longest(1, 3)

--- get rid of that counting variable... it's the devil!
al = {1:[(2,1)],2:[(1,3)]} 2 2
seen={2,1}
longest(2)
    max_length = 0
    3 + longest(1)
        max_length = 0
        1 + 

[[1,2,1],[2,3,2],[1,3,2]] 3 1
al = {1:[(2,1),(3,2)],2:[(3,2)]}
seen = {1,2}
longest(1)
    max_length = 0
    1 + longest(2) => 3
        max_length = 0
        2 + longest(3) => 2
    2 + longest(3) => 2

Woah, suddenly realized this problem goes a lot deeper potentially

UPDATE: so it's the next day; I read some of the discussions this morning... gonna try to implement
one of those. Actually, let's first just adjust what I have here to work. The fundamental
mechanism I'm missing is some state to hold the shortest distances for each node.

al = {2:[(1,1),(3,1)],3:[(4,1)]}
dp = [0, inf, inf, inf]
longest(1,0)
    longest()

original node has to be filled out as 0
"""

from collections import defaultdict
from math import inf
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        al, dp = defaultdict(list), [0] + [inf] * n
        dp[k] = 0
        for start, end, cost in times:
            al[start].append((end, cost))
        def longest(node, acc=0):
            for dest, cost in al[node]:
                cost += acc
                if cost < dp[dest]:
                    dp[dest] = cost
                    longest(dest, cost)
        longest(k)
        res = max(dp)
        return res if res != inf else -1




