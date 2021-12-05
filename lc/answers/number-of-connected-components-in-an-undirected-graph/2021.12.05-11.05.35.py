class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = list(range(n))
        def find(node):
            if uf[node] == node: return node
            root = find(uf[node])
            uf[node] = root
            return root
        for u, v in edges:
            f_u, f_v = find(u), find(v)
            if f_u != f_v:
                n -= 1
                uf[f_u] = f_v
        return n