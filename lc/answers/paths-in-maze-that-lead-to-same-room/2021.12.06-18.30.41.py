"""
tracing
n = 5, corridors = [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]]
adj = {
    1: [2,4,3],
    2: [1,5,4],
    3: [1,4],
    4: [1,2,3],
    5: [2]
}

dfs(1, [1], {1})
    dfs(1, [1], {1})

dfs(2, [2], {2})
dfs(3, [3], {3})
dfs(4, [4], {4})
dfs(5, [5], {5})
"""

class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        adj, loops_of_three = defaultdict(list), set()
        for u, v in corridors:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, path=[], seen=set()):
            for nxt in adj[node]:
                if nxt in seen:
                    if len(path) == 3 and path[0] == nxt:
                        loops_of_three.add(tuple(sorted(path)))
                else:
                    dfs(nxt, path + [nxt], seen | {nxt})

        for root in adj.keys():
            dfs(root, [root], {root})

        return len(loops_of_three)