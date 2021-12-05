"""
===== Initial Thoughts =====
I just solved this yesterday (well I think I had to look up the answer eventually) but I
can't really remember the solution (!!!). I think the trick is just to find the number
of redundant connections and if that's enough to cover the computers that aren't covered.

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf, seen, extra = list(range(n)), set(), 0
        def find(node):
            if uf[node] == node: return node
            root = find(uf[node])
            uf[node] = root
            return root

        for u, v in connections:
            seen.add(u)
            seen.add(v)
            f_u, f_v = find(u), find(v)
            if f_u == f_v:
                extra += 1
            else:
                uf[f_u] = f_v
        num_unconnected = n - len(seen)
        return extra if extra >= num_unconnected else -1