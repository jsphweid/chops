"""
[[0,1],[0,2],[1,2]] 4
uf=[1,2,2,3] extras=1 seen={0,1,2}

100

"""

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf, extras, seen, wat = list(range(n)), 0, set(), 0
        def find(node):
            if uf[node] == node: return node
            root = find(uf[node])
            uf[node] = root
            return root
        for u, v in connections:
            seen.add(u)
            seen.add(v)
            uu, vv = find(u), find(v)
            print(uu, vv)
            if uu == vv:
                extras += 1
            else:
                wat += 1
                uf[uu] = vv
        parents = sum([1 if uf[i] == i else 0 for i in range(len(uf))])
        unconnected = parents - 1
        return unconnected if extras >= unconnected else -1
