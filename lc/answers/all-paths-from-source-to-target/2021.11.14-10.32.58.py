"""
===== Initial Thoughts =====
[[1,2],[3],[3],[]]
{
    0: [1,2]
    1: [3]
    2: [3]
    3: []
}

it's sufficiently organized though...

[[4,3,1],[3,2,4],[3],[4],[]]

paths=[[0,4],[0,3,4]]
dfs(4, [0]) -> Done
dfs(3, [0]) [0,3]
    dfs(4, [0,3]) [0,3,4]

dfs(1, [0])
--------

dfs(0)
curr=[0]


[[1,2],[3],[3],[]]
dfs(0, path=[]) curr=[0]
    dfs(1, path=[0]) curr=[0,1]
        dfs(3, path=[0,1]) curr=[0,1,3]
    dfs(2, path=[0]) curr=[0,2]
        dfs(3, path=[0,2]) curr=[0,2,3]


"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        def dfs(node, path=[]):
            curr = path + [node]
            if node == len(graph) - 1:
                paths.append(curr)
            else:
                for n in graph[node]: dfs(n, curr)
        dfs(0)
        return paths