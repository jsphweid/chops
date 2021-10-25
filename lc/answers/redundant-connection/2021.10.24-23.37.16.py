"""
[[1,2],[2,3],[3,4],[1,4],[1,5]]

{
    1: {2, 4, 5},
    2: {1, 3},
    3: {2, 4}
    4: {3, 1}
    5: {1}
}
"""
from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        m = defaultdict(set)
        for l, r in edges:
            m[l].add(r)
            m[r].add(l)

        seen = set()
        def extra_conn_exists(l, r, l_ignore, r_ignore):
            results = []
            for n in m[l]:
                if n not in seen:
                    seen.add(l)
                    if l == l_ignore and n == r_ignore: continue
                    if n == r: return True
                    results.append(extra_conn_exists(n, r, l_ignore, r_ignore))
                seen.add(l)
            return any(results)

        redundant = None
        for l, r in edges:
            seen = {l}
            if extra_conn_exists(l, r, l, r):
                redundant = [l, r]
        return redundant
