"""
===== Initial Thoughts =====
1: 3
2: 3

1:2
2:3
3:1

1:3
2:3
3:4

{
    1: [3],
    2: [3],
    3: []
}

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 


relations = [[1,3],[2,3],[3,4]]
al = {1:[3], 2:[3], 3:[4]}
longest([1,2,3], {})
    longest([3], {1}) => 2
        longest([4], {1,3}) => 1
    longest([3], {2}) => 2
        longest([4], {2,3}) => 1
    longest([3], {}) => 2 (eventually)

relations = [[1,2],[2,3],[3,1]]
al = {1: [2], 2:[3], 3: [1]}
longest([1,2,3], {})
    longest([2], {1})
        longest([3], {1,2}) -> -1


"""
from collections import defaultdict
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph, dp = {i + 1: [] for i in range(n)}, {}
        for l, r in relations: graph[l].append(r)
        def longest(nodes, seen=set(), best=0) -> int:
            for node in nodes:
                if node in seen: return -1
                children, new_seen = graph[node], seen | {node}
                if children:
                    result = dp[node] if node in dp else longest(children, new_seen)
                    dp[node] = result
                    if result == -1: return -1
                    best = max(best, result)
            return best + 1
        return longest(graph.keys())

        