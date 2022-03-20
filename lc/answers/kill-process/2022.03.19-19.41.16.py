"""
===== Initial Thoughts =====
should be pretty easy if we make an adjacency list
honestly it can probably be done more efficiently 
maybe we'll evolve to that

~~Complexity Analysis
Time - 
Space - 

    **Input:** pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
    **Output:** [5,10]

{3: [1,5], 1: [], 5: [10], 10: [], 0: [3]}
"""
from collections import defaultdict
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        adj = defaultdict(list)
        for p, parent in zip(pid, ppid):
            adj[parent].append(p)
        res = []
        stack = [kill]
        while stack:
            id = stack.pop()
            res.append(id)
            for child in adj[id]:
                stack.append(child)
        return res




