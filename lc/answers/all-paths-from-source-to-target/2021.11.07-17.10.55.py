"""
[[1,2],[3],[3],[]]

recurse(0, 3, [0])

recurse(0, 3, [0])
[1,2] => [0, 1], [0, 2]
recurse(1, 3, [0, 1])
[3] [0,1,3]
recurse(2, 3, [0, 2])
[3] [0,1,2]

[[1],[]]
recurse(0, 1, [0])
[1] [0, 1]
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        def recurse(start, end, acc):
            # iterate over children
            for child in graph[start]:
                chain = acc[:] + [child]
                if child == end:
                    # if it's the end, add the new path
                    paths.append(chain)
                else:
                    # else add on to the acc and recurse deeper
                    recurse(child, end, chain)
        recurse(0, len(graph) - 1, [0])
        return paths
