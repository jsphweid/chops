"""
===== Initial Thoughts =====
can't we just make the adj. list and then select the two most connected?
if there is a tie between different candidates, we'd want the one where we 
don't have to subtract 1 because the nodes are directly connected.

[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]

# some process to filter out which ones are in the running
2:[1,3,4]
1:[0,2]
5:[6,7]

0:[1]
3:[2]
4:[2]
6:[5]
7:[5]


[[0,1],[0,3],[1,2],[1,3]]
1:[0,2,3]
0:[1,3]
3:[0,1]
2:[1]

2
[(3,1),(2,0),(2,3),(1,2)]

[1,0,3]
0,1,2
1,2 2

1, 0


~~Complexity Analysis
Time - 
Space - 
"""
from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads: return 0
        adj = defaultdict(set)
        for u, v in roads:
            adj[u].add(v)
            adj[v].add(u)
        lengths = [(len(value), key) for key, value in adj.items()]
        lengths.sort(reverse=True)
        longest, second_longest = lengths[0][0], None
        most_viable = []
        for l in lengths:
            if l[0] == longest or l[0] == second_longest:
                most_viable.append(l[1])
            elif second_longest == None:
                second_longest = l[0]
                most_viable.append(l[1])
            else:
                break
        best = 0
        for i in range(len(most_viable) - 1):
            for j in range(i + 1, len(most_viable)):
                u, v = most_viable[i], most_viable[j]
                num = len(adj[u]) + len(adj[v])
                num -= 1 if u in adj[v] else 0
                best = max(best, num)
        return best