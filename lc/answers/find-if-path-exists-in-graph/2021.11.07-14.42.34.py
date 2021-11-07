"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 


[[0,1],[0,2],[3,5],[5,4],[4,3]] 0,5
{0: {1,2}, 3: {5}, 4: {3}, 5: {4}}

n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
{0:{1},1:{2},2:{0}}

[[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]] 7 5
{0:{7,8,4},6:{1,5},2:{0},5:{8},4:{7},1:{3},3:{5}}

[[0,1],[0,2],[3,5],[5,4],[4,3]]
"""
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start == end: return True
        graph = defaultdict(set)
        for left, right in edges:
            graph[left].add(right)
            graph[right].add(left)
        explored = set()
        def recurse(curr):
            explored.add(curr)
            if end in graph[curr]:
                return True
            for item in graph[curr]:
                if item not in explored and recurse(item):
                    return True
            return False
        return recurse(start)