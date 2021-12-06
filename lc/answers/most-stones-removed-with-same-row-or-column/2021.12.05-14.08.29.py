class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x, y, adj, N = defaultdict(list), defaultdict(list), defaultdict(set), len(stones)
        for i in range(N):
            x[stones[i][0]].append(i)
            y[stones[i][1]].append(i)
        for i in range(N):
            adj[i] |= set(x[stones[i][0]]) - {i}
            adj[i] |= set(y[stones[i][1]]) - {i}

        uf = list(range(N))

        def find(node):
            if node == uf[node]:
                return node
            root = find(uf[node])
            uf[node] = root
            return root
        for u, values in adj.items():
            for v in values:
                uu, vv = find(u), find(v)
                if uu != vv:
                    uf[uu] = vv
        islands = set(map(find, list(range(N))))
        return N - len(islands)
