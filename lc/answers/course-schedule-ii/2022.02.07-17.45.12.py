"""
===== Initial Thoughts =====
{
    0:[1,2]
    1:[3]
    2:[3]
}

lookup = {

}
levels = {

}

after a ton of work... got TLE... :(

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites: return list(range(numCourses))
        adj, levels, lookup = defaultdict(list), defaultdict(set), {}
        us, vs = set(), set()
        for v, u in prerequisites:
            adj[u].append(v)
            us.add(u)
            vs.add(v)
        starts = us - vs
        loop_detected = False
        noreq = list(set(range(numCourses)) - us - vs)
        def dfs(node, i, path):
            nonlocal loop_detected
            if node in path:
                loop_detected = True
                return
            if node in lookup:
                if i > lookup[node]:
                    levels[lookup[node]].remove(node)
                    lookup[node] = i
                    levels[i].add(node)
            else:
                lookup[node] = i
                levels[i].add(node)
            for child in adj[node]:
                dfs(child, i + 1, path | {node})

        for start in starts:
            dfs(start, 0, set())
        if loop_detected:
            return []
        res = [list(levels.get(i, [])) for i in range(numCourses)]
        res = [item for l in res for item in l]
        res = noreq + res
        return res if len(res) == numCourses else []

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

implemented as a stack and it works better probably 
because we can actually exit early when there is a loop

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites: return list(range(numCourses))
        adj, levels, lookup = defaultdict(list), defaultdict(set), {}
        us, vs = set(), set()
        for v, u in prerequisites:
            adj[u].append(v)
            us.add(u)
            vs.add(v)
        starts = us - vs
        loop_detected = False
        noreq = list(set(range(numCourses)) - us - vs)
        stack = [(start, 0, set()) for start in starts]
        while stack:
            node, i, seen = stack.pop()
            if node in seen: 
                return []
            
            if node in lookup:
                if i > lookup[node]:
                    levels[lookup[node]].remove(node)
                    lookup[node] = i
                    levels[i].add(node)
            else:
                lookup[node] = i
                levels[i].add(node)
            for child in adj[node]:
                stack.append((child, i + 1, seen | {node}))
        res = [list(levels.get(i, [])) for i in range(numCourses)]
        res = [item for l in res for item in l]
        res = noreq + res
        return res if len(res) == numCourses else []


Performance is still pretty bad

Here's Aaron's idea
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj, res = defaultdict(set), []
        for u, v in prerequisites:
            adj[u].add(v)
        remove = [i for i in range(numCourses) if i not in adj]
        while remove:
            i = remove.pop()
            res.append(i)
            for u in list(adj.keys()):
                if i in adj[u]:
                    adj[u].remove(i)
                    if len(adj[u]) == 0:
                        del adj[u]
                        remove.append(u)
        return res if len(res) == numCourses else []

Finally below... a little smarter, only scan a subset of nodes we know need to be deleted.
"""

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj, lookup, res = defaultdict(set), defaultdict(list), []
        for u, v in prerequisites:
            adj[u].add(v)
            lookup[v].append(u)
        remove = [i for i in range(numCourses) if i not in adj]
        while remove:
            i = remove.pop()
            res.append(i)
            for u in lookup[i]:
                adj[u].remove(i)
                if len(adj[u]) == 0:
                    del adj[u]
                    remove.append(u)
        return res if len(res) == numCourses else []




